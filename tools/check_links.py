#!/usr/bin/env python3
"""Check source-manifest URLs. Runs on demand and in weekly scheduled CI."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "Tech-Repo-Link-Checker/1.0"


def fetch(url: str) -> tuple[int | None, str]:
    for method in ("HEAD", "GET"):
        try:
            request = Request(url, method=method, headers={"User-Agent": USER_AGENT, "Range": "bytes=0-0"})
            with urlopen(request, timeout=20) as response:
                return response.status, response.geturl()
        except HTTPError as exc:
            if method == "HEAD" and exc.code in {403, 404, 405, 501}:
                continue
            return exc.code, url
        except (URLError, TimeoutError, OSError) as exc:
            if method == "HEAD":
                continue
            return None, str(exc)
    return None, "request failed"


def main() -> int:
    entries = []
    for manifest_path in sorted((ROOT / "docs").rglob("fontes.yml")):
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
        for source in manifest.get("sources", []):
            entries.append(source["url"])
    failures = []
    inconclusive = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = {pool.submit(fetch, url): url for url in entries}
        for future in as_completed(futures):
            url = futures[future]
            try:
                status, detail = future.result()
            except Exception as exc:  # a single host must not abort the full audit
                status, detail = None, str(exc)
            if status in {404, 410}:
                failures.append((url, status, detail))
            elif status is None or status >= 400:
                inconclusive.append((url, status, detail))
    for url, status, detail in sorted(failures):
        print(f"BROKEN\t{status}\t{url}\t{detail}")
    for url, status, detail in sorted(inconclusive):
        print(f"REVIEW\t{status if status is not None else 'ERR'}\t{url}\t{detail}")
    print(f"Links examinados: {len(entries)}; removidos: {len(failures)}; revisão manual: {len(inconclusive)}.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
