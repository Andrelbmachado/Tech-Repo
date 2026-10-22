#!/usr/bin/env python3
"""Gera o corpo em Markdown do PR aberto pelo vigia de lançamentos.

Lê o relatório JSON produzido por ``watch_releases.py --json`` e escreve um
Markdown com a tabela de versões novas, os links das release notes e o
checklist de páginas a revisar por tecnologia.

Uso::

    python tools/render_release_pr.py release-report.json pr-body.md
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Páginas que precisam de revisão humana quando a versão muda.
REVIEW_PAGES = ("README.md", "versoes.md", "conceitos.md", "boas-praticas.md", "fontes.yml")


def render(report: dict) -> str:
    outdated = report.get("outdated", [])
    lines: list[str] = []
    lines.append("## Versões novas detectadas pelo vigia de lançamentos")
    lines.append("")
    lines.append(
        f"Gerado em {report.get('generated_at', '?')} a partir de fontes oficiais "
        "credenciadas (mantenedores/organismos normativos)."
    )
    lines.append("")

    if not outdated:
        lines.append("_Nenhuma versão nova; este PR não deveria ter sido aberto._")
        return "\n".join(lines) + "\n"

    lines.append("| Tecnologia | Fonte | Versão anterior | Nova versão | Release notes |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in outdated:
        previous = item.get("current_version") or "—"
        notes = item.get("release_notes") or ""
        notes_cell = f"[notas]({notes})" if notes else "—"
        lines.append(
            f"| {item.get('name', item.get('id'))} "
            f"| `{item.get('provider', '?')}` "
            f"| {previous} "
            f"| **{item.get('latest_version', '?')}** "
            f"| {notes_cell} |"
        )
    lines.append("")

    lines.append("## Checklist de revisão")
    lines.append("")
    for item in outdated:
        name = item.get("name", item.get("id"))
        path = item.get("path", "")
        folder = path.rsplit("/", 1)[0] if "/" in path else path
        lines.append(f"### {name} → {item.get('latest_version', '?')}")
        notes = item.get("release_notes")
        if notes:
            lines.append(f"- Release notes: {notes}")
        for page in REVIEW_PAGES:
            target = f"{folder}/{page}" if folder else page
            lines.append(f"- [ ] Revisar `{target}` para a nova versão")
        lines.append("")

    errors = report.get("errors", [])
    if errors:
        lines.append("## Fontes com falha nesta execução")
        lines.append("")
        for item in errors:
            lines.append(f"- `{item.get('id')}` ({item.get('provider')}): {item.get('detail')}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("Confirme cada versão na fonte oficial antes de aprovar o merge.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 2:
        print("uso: render_release_pr.py <relatorio.json> <saida.md>", file=sys.stderr)
        return 2
    report = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    Path(args[1]).write_text(render(report), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
