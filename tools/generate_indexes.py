#!/usr/bin/env python3
"""Generate catalog, human map, and AI index from tech.yml records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def records() -> list[dict]:
    result = []
    for metadata_path in sorted((ROOT / "docs").rglob("tech.yml")):
        data = yaml.safe_load(metadata_path.read_text(encoding="utf-8")) or {}
        data["path"] = metadata_path.parent.relative_to(ROOT).as_posix()
        local_docs = metadata_path.parent / "documentacao-oficial" / "README.md"
        data["local_official_docs"] = local_docs.is_file()
        if local_docs.is_file():
            data["local_official_docs_path"] = local_docs.relative_to(ROOT).as_posix()
        result.append(data)
    return result


def outputs(items: list[dict]) -> dict[Path, str]:
    catalog_lines = ["schema_version: 1", "repository: Tech-Repo", "generated_by: tools/generate_indexes.py", "technologies:"]
    ai_lines = ["schema_version: 1", "repository: Tech-Repo", "catalog: CATALOG.yml", "map: MAPA.md", "technology_map: MAPA-TECNOLOGIAS.md", "technology_record_files: [tech.yml, fontes.yml, README.md]", "local_documentation_directory: documentacao-oficial/", "local_documentation_manifest: documentacao-oficial/README.md", "technologies:"]
    map_lines = ["# Mapa de tecnologias", "", "Gerado a partir dos arquivos `tech.yml`. Edite os metadados da tecnologia, não esta lista.", ""]
    by_category: dict[str, list[dict]] = {}
    for item in items:
        quota = item.get("source_quota") or {}
        common = [
            f"  - id: {quote(str(item['id']))}",
            f"    name: {quote(str(item['name']))}",
            f"    category: {quote(str(item['category']))}",
            f"    status: {quote(str(item['status']))}",
            f"    path: {quote(str(item['path']))}",
        ]
        catalog_lines.extend(common + [f"    source_quota_status: {quote(str(quota.get('status', 'pending')))}"])
        ai_lines.extend(common + [f"    official_source_count: {int(quota.get('official_count', 0))}", f"    source_quota_status: {quote(str(quota.get('status', 'pending')))}", f"    has_local_official_docs: {'true' if item['local_official_docs'] else 'false'}"])
        if item["local_official_docs"]:
            ai_lines.append(f"    local_official_docs_manifest: {quote(str(item['local_official_docs_path']))}")
        by_category.setdefault(str(item["category"]), []).append(item)
    for category, category_items in sorted(by_category.items()):
        map_lines.extend([f"## {category}", ""])
        for item in category_items:
            quota = item.get("source_quota") or {}
            map_lines.append(f"- [{item['name']}]({item['path']}/README.md) — `{item['status']}`, fontes: `{quota.get('status', 'pending')}`")
        map_lines.append("")
    return {
        ROOT / "CATALOG.yml": "\n".join(catalog_lines) + "\n",
        ROOT / "MAPA-TECNOLOGIAS.md": "\n".join(map_lines),
        ROOT / "INDICE-IA.yaml": "\n".join(ai_lines) + "\n",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()
    generated = outputs(records())
    stale = []
    for path, content in generated.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.write_text(content, encoding="utf-8")
    if stale:
        print("Índices desatualizados: " + ", ".join(stale))
        return 1
    if not args.check:
        print(f"Índices gerados para {len(records())} tecnologias.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
