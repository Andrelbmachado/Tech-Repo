#!/usr/bin/env python3
"""Vigia de lançamentos das tecnologias do catálogo.

Lê o bloco opcional ``release_watch`` de cada ``tech.yml``, consulta a fonte
oficial declarada (endoflife.date, API de releases do GitHub ou o feed de
downloads de python.org) e compara a última versão estável conhecida com a
registrada no repositório.

Somente fontes credenciadas (mantenedores/organismos normativos) são aceitas:
cada provedor abaixo aponta diretamente para a origem oficial do projeto, e o
provedor ``github`` exige que o repositório pertença ao mantenedor declarado.

Modos de uso::

    python tools/watch_releases.py            # relata desatualizações (exit 1 se houver)
    python tools/watch_releases.py --check     # idem, sem escrever
    python tools/watch_releases.py --write      # grava versao_atual/verificado_em em tech.yml
    python tools/watch_releases.py --json saida.json  # relatório estruturado para o workflow
    python tools/watch_releases.py --only python go    # limita às tecnologias indicadas

A saída JSON alimenta o workflow agendado que abre um PR quando surge versão
nova.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "Tech-Repo-Release-Watcher/1.0"
TIMEOUT = 30

# Regex de versão semântica relaxada (1, 1.2, 1.2.3, com prefixo opcional "v").
VERSION_RE = re.compile(r"^v?(\d+)(?:\.(\d+))?(?:\.(\d+))?")


class WatchError(Exception):
    """Falha recuperável ao consultar uma fonte; não interrompe as demais."""


def today() -> str:
    """Data corrente em ISO. Isolada para facilitar testes."""
    return date.today().isoformat()


def http_json(url: str) -> object:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urlopen(request, timeout=TIMEOUT) as response:
            return json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        raise WatchError(f"falha de rede: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise WatchError(f"resposta não-JSON: {exc}") from exc


def version_key(raw: str) -> tuple[int, int, int]:
    """Converte uma string de versão em tupla comparável; levanta se inválida."""
    match = VERSION_RE.match(str(raw).strip())
    if not match:
        raise WatchError(f"versão não reconhecida: {raw!r}")
    major, minor, patch = (int(part) if part else 0 for part in match.groups())
    return major, minor, patch


def normalize_version(raw: str) -> str:
    """Remove prefixo 'v' e espaços para armazenar de forma consistente."""
    text = str(raw).strip()
    return text[1:] if text[:1].lower() == "v" and text[1:2].isdigit() else text


# ---------------------------------------------------------------------------
# Provedores de fonte oficial
# ---------------------------------------------------------------------------


def latest_endoflife(watch: dict) -> tuple[str, str]:
    """endoflife.date: versão mais recente do produto indicado.

    Params: ``product`` (ex.: "python"). Retorna (versão, url das notas).
    """
    product = str(watch.get("product", "")).strip()
    if not product:
        raise WatchError("endoflife requer 'product'")
    data = http_json(f"https://endoflife.date/api/{product}.json")
    if not isinstance(data, list) or not data:
        raise WatchError("endoflife retornou lista vazia")
    # Ciclos vêm do mais novo para o mais antigo; escolhe o maior 'latest'.
    best_raw: str | None = None
    best_key: tuple[int, int, int] | None = None
    for cycle in data:
        if not isinstance(cycle, dict):
            continue
        candidate = cycle.get("latest") or cycle.get("cycle")
        if candidate is None:
            continue
        try:
            key = version_key(str(candidate))
        except WatchError:
            continue
        if best_key is None or key > best_key:
            best_key, best_raw = key, str(candidate)
    if best_raw is None:
        raise WatchError("endoflife sem versão utilizável")
    notes = f"https://endoflife.date/{product}"
    return normalize_version(best_raw), notes


def latest_github(watch: dict) -> tuple[str, str]:
    """API pública de releases do GitHub.

    Params: ``repo`` ("owner/name") e opcional ``maintainer_owner`` para travar
    o dono esperado (garante fonte credenciada). Retorna (versão, url das notas).
    """
    repo = str(watch.get("repo", "")).strip()
    if "/" not in repo:
        raise WatchError("github requer 'repo' no formato owner/name")
    owner = repo.split("/", 1)[0]
    expected_owner = str(watch.get("maintainer_owner", owner)).strip()
    if owner.lower() != expected_owner.lower():
        raise WatchError(f"repo {repo} fora do dono credenciado {expected_owner}")
    data = http_json(f"https://api.github.com/repos/{repo}/releases/latest")
    if not isinstance(data, dict) or not data.get("tag_name"):
        raise WatchError("github sem tag_name na release mais recente")
    if data.get("prerelease") or data.get("draft"):
        raise WatchError("release mais recente é prerelease/draft")
    tag = str(data["tag_name"])
    notes = str(data.get("html_url") or f"https://github.com/{repo}/releases")
    return normalize_version(tag), notes


def latest_python(watch: dict) -> tuple[str, str]:
    """Feed oficial de releases do python.org (endpoint JSON do site).

    Usa a fonte credenciada da PSF. Retorna (versão estável mais recente, url).
    """
    data = http_json("https://www.python.org/api/v2/downloads/release/?is_published=true")
    if not isinstance(data, list):
        raise WatchError("python.org retornou formato inesperado")
    best_raw: str | None = None
    best_key: tuple[int, int, int] | None = None
    for release in data:
        if not isinstance(release, dict):
            continue
        name = str(release.get("name", ""))  # ex.: "Python 3.13.1"
        if not release.get("is_published") or release.get("pre_release"):
            continue
        match = re.search(r"(\d+\.\d+(?:\.\d+)?)", name)
        if not match:
            continue
        try:
            key = version_key(match.group(1))
        except WatchError:
            continue
        if best_key is None or key > best_key:
            best_key, best_raw = key, match.group(1)
    if best_raw is None:
        raise WatchError("python.org sem release estável utilizável")
    return normalize_version(best_raw), "https://www.python.org/downloads/"


PROVIDERS = {
    "endoflife": latest_endoflife,
    "github": latest_github,
    "python": latest_python,
}


# ---------------------------------------------------------------------------
# Varredura do catálogo
# ---------------------------------------------------------------------------


def watched_records() -> list[tuple[Path, dict, dict]]:
    """Retorna (caminho tech.yml, metadados, bloco release_watch) das tecnologias vigiadas."""
    found = []
    for metadata_path in sorted((ROOT / "docs").rglob("tech.yml")):
        meta = yaml.safe_load(metadata_path.read_text(encoding="utf-8")) or {}
        watch = meta.get("release_watch")
        if isinstance(watch, dict) and watch.get("provider"):
            found.append((metadata_path, meta, watch))
    return found


def evaluate(meta: dict, watch: dict) -> dict:
    """Consulta a fonte e devolve o resultado da comparação para uma tecnologia."""
    tech_id = str(meta.get("id", "?"))
    provider = str(watch.get("provider", ""))
    result: dict = {"id": tech_id, "name": meta.get("name", tech_id), "provider": provider}
    fetcher = PROVIDERS.get(provider)
    if fetcher is None:
        result.update(status="error", detail=f"provedor desconhecido: {provider}")
        return result
    try:
        latest, notes_url = fetcher(watch)
        latest_cmp = version_key(latest)
    except WatchError as exc:
        result.update(status="error", detail=str(exc))
        return result
    current = normalize_version(watch.get("current_version") or "") or None
    result.update(latest_version=latest, release_notes=notes_url, current_version=current)
    if current is None:
        result.update(status="new", detail="sem versão registrada")
        return result
    try:
        current_cmp = version_key(current)
    except WatchError:
        result.update(status="new", detail=f"versão registrada ilegível: {current}")
        return result
    if latest_cmp > current_cmp:
        result.update(status="outdated", detail=f"{current} -> {latest}")
    else:
        result.update(status="current", detail=f"atual em {latest}")
    return result


def apply_write(metadata_path: Path, result: dict) -> None:
    """Atualiza release_watch.current_version e verificado_em no tech.yml, preservando o restante."""
    meta = yaml.safe_load(metadata_path.read_text(encoding="utf-8")) or {}
    watch = meta.setdefault("release_watch", {})
    watch["current_version"] = result["latest_version"]
    watch["verificado_em"] = today()
    meta["latest_verified_version"] = result["latest_version"]
    metadata_path.write_text(
        yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, default_flow_style=False),
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="apenas relatar (padrão)")
    parser.add_argument("--write", action="store_true", help="gravar nova versão no tech.yml")
    parser.add_argument("--json", metavar="ARQUIVO", help="gravar relatório estruturado em JSON")
    parser.add_argument("--only", nargs="+", metavar="ID", help="limitar às tecnologias indicadas")
    args = parser.parse_args(argv)

    records = watched_records()
    if args.only:
        wanted = {slug.lower() for slug in args.only}
        records = [row for row in records if str(row[1].get("id", "")).lower() in wanted]

    results: list[dict] = []
    for metadata_path, meta, watch in records:
        result = evaluate(meta, watch)
        result["path"] = metadata_path.relative_to(ROOT).as_posix()
        if args.write and result["status"] in {"outdated", "new"}:
            apply_write(metadata_path, result)
            result["written"] = True
        results.append(result)

    outdated = [r for r in results if r["status"] in {"outdated", "new"}]
    errors = [r for r in results if r["status"] == "error"]

    for result in results:
        print(f"{result['status'].upper():9}\t{result['id']}\t{result['detail']}")
    print(
        f"Tecnologias vigiadas: {len(results)}; "
        f"novas/desatualizadas: {len(outdated)}; erros: {len(errors)}."
    )

    if args.json:
        payload = {
            "generated_at": today(),
            "outdated": outdated,
            "errors": errors,
            "all": results,
        }
        Path(args.json).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    # Erros de rede não falham o processo (como check_links); desatualização sim,
    # salvo no modo --write, cujo propósito é justamente aplicar a atualização.
    if outdated and not args.write:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
