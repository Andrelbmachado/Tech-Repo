#!/usr/bin/env python3
"""Validate technology metadata, source manifests, and generated indexes."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TECH_FIELDS = {"id", "name", "category", "status", "summary_pt", "summary_en", "official_website", "maintainer", "latest_verified_version", "source_quota", "tags", "related_technologies", "last_reviewed", "next_review"}
SOURCE_FIELDS = {"title", "organization", "url", "source_type", "authority", "language", "version", "publication_date", "license_or_access", "verified_at", "notes"}
SOURCE_TYPES = {"specification", "api", "guide", "runtime", "vendor", "standard", "community"}
CATEGORY_READMES = [
    "fundamentos", "programacao", "redes-e-wifi", "ciberseguranca", "devops-e-cloud",
    "engenharia-de-software", "eletronica", "sistemas-embarcados", "engenharia-mecanica",
    "hardware", "software",
]


def main() -> int:
    errors: list[str] = []
    ids: set[str] = set()
    paths = sorted((ROOT / "docs").rglob("tech.yml"))
    for category in CATEGORY_READMES:
        if not (ROOT / "docs" / category / "README.md").is_file():
            errors.append(f"docs/{category}: README.md da categoria ausente")
    for category in ("linguagens", "web", "bancos-de-dados", "runtimes-e-frameworks"):
        if not (ROOT / "docs/programacao" / category / "README.md").is_file():
            errors.append(f"docs/programacao/{category}: README.md da categoria ausente")
    for metadata_path in paths:
        folder = metadata_path.parent
        rel = folder.relative_to(ROOT).as_posix()
        try:
            meta = yaml.safe_load(metadata_path.read_text(encoding="utf-8")) or {}
            manifest_path = folder / "fontes.yml"
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else None
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{rel}: YAML inválido ou ausente: {exc}")
            continue
        missing = TECH_FIELDS - set(meta)
        if missing:
            errors.append(f"{rel}/tech.yml: campos ausentes: {', '.join(sorted(missing))}")
        tech_id = str(meta.get("id", ""))
        if not SLUG.fullmatch(tech_id) or folder.name != tech_id:
            errors.append(f"{rel}: id inválido ou diferente do slug da pasta: {tech_id}")
        if tech_id in ids:
            errors.append(f"{rel}: id duplicado: {tech_id}")
        ids.add(tech_id)
        if meta.get("status") not in {"curated", "in-progress", "planned"}:
            errors.append(f"{rel}: status editorial inválido")
        quota = meta.get("source_quota") or {}
        if quota.get("required") != 5 or quota.get("status") not in {"complete", "partial", "pending"}:
            errors.append(f"{rel}: declare quota required=5 e status complete/partial/pending")
        if quota.get("status") == "partial" and not str(quota.get("exception_reason", "")).strip():
            errors.append(f"{rel}: quota partial precisa de exception_reason")
        for filename in ("README.md", "versoes.md", "conceitos.md", "boas-praticas.md", "relacionados.md"):
            if not (folder / filename).is_file():
                errors.append(f"{rel}: arquivo ausente: {filename}")
        if not isinstance(manifest, dict) or not isinstance(manifest.get("sources"), list):
            errors.append(f"{rel}/fontes.yml: esperado objeto com lista sources")
            continue
        official_count = 0
        local_urls: set[str] = set()
        for index, source in enumerate(manifest["sources"], start=1):
            if not isinstance(source, dict):
                errors.append(f"{rel}/fontes.yml[{index}]: entrada deve ser objeto")
                continue
            missing_source = SOURCE_FIELDS - set(source)
            if missing_source:
                errors.append(f"{rel}/fontes.yml[{index}]: campos ausentes: {', '.join(sorted(missing_source))}")
            url = str(source.get("url", "")).strip()
            parsed = urlparse(url)
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{rel}/fontes.yml[{index}]: URL HTTPS inválida: {url}")
            if url in local_urls:
                errors.append(f"{rel}: URL repetida no manifesto: {url}")
            local_urls.add(url)
            authority = source.get("authority")
            if authority not in {"primary", "official-vendor", "secondary"}:
                errors.append(f"{rel}/fontes.yml[{index}]: autoridade inválida")
            if authority in {"primary", "official-vendor"}:
                official_count += 1
            if source.get("source_type") not in SOURCE_TYPES:
                errors.append(f"{rel}/fontes.yml[{index}]: source_type inválido")
            if source.get("language") not in {"pt", "en", "other"}:
                errors.append(f"{rel}/fontes.yml[{index}]: language deve ser pt, en ou other")
        if quota.get("official_count") != official_count:
            errors.append(f"{rel}: official_count={quota.get('official_count')} mas fontes oficiais encontradas={official_count}")
        if quota.get("status") == "complete" and official_count < 5:
            errors.append(f"{rel}: status complete requer cinco ou mais fontes oficiais")
        if quota.get("status") == "partial" and official_count >= 5:
            errors.append(f"{rel}: status partial tem cinco fontes oficiais ou mais")
    check = subprocess.run([sys.executable, str(ROOT / "tools/generate_indexes.py"), "--check"], cwd=ROOT, capture_output=True, text=True)
    if check.returncode:
        errors.append((check.stdout + check.stderr).strip() or "índices gerados estão desatualizados")
    if errors:
        print("\n".join(f"ERRO: {error}" for error in errors))
        return 1
    print(f"Catálogo válido: {len(paths)} tecnologias.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
