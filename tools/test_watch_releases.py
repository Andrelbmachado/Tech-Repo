#!/usr/bin/env python3
"""Testes offline do vigia de lançamentos e do gerador de corpo de PR.

Não acessam a rede: as funções de provedor são exercitadas substituindo
``http_json``. Os testes rodam mesmo sem PyYAML instalado — um stub mínimo é
injetado quando o módulo real está ausente, pois a lógica testada não depende
de YAML.
"""

from __future__ import annotations

import sys
import types
import unittest
from pathlib import Path

# Garante que 'import yaml' em watch_releases funcione sem a dependência real.
try:  # pragma: no cover - depende do ambiente
    import yaml  # noqa: F401
except ModuleNotFoundError:  # pragma: no cover
    stub = types.ModuleType("yaml")
    stub.safe_load = lambda *a, **k: {}
    stub.safe_dump = lambda *a, **k: ""
    sys.modules["yaml"] = stub

sys.path.insert(0, str(Path(__file__).resolve().parent))

import render_release_pr as pr  # noqa: E402
import watch_releases as wr  # noqa: E402


class VersionParsing(unittest.TestCase):
    def test_version_key_orders_correctly(self):
        self.assertGreater(wr.version_key("3.13.1"), wr.version_key("3.13.0"))
        self.assertGreater(wr.version_key("1.70"), wr.version_key("1.69.5"))
        self.assertGreater(wr.version_key("2"), wr.version_key("1.99.99"))

    def test_version_key_handles_v_prefix(self):
        self.assertEqual(wr.version_key("v5.4.2"), (5, 4, 2))

    def test_version_key_rejects_garbage(self):
        with self.assertRaises(wr.WatchError):
            wr.version_key("estável")

    def test_normalize_version_strips_v(self):
        self.assertEqual(wr.normalize_version("v1.2.3"), "1.2.3")
        self.assertEqual(wr.normalize_version(" 3.13 "), "3.13")
        # Não remove 'v' quando não é prefixo de versão.
        self.assertEqual(wr.normalize_version("version"), "version")


class Providers(unittest.TestCase):
    def setUp(self):
        self._orig = wr.http_json

    def tearDown(self):
        wr.http_json = self._orig

    def test_endoflife_picks_newest_cycle(self):
        wr.http_json = lambda url: [
            {"cycle": "1.21", "latest": "1.21.5"},
            {"cycle": "1.22", "latest": "1.22.3"},
            {"cycle": "1.20", "latest": "1.20.9"},
        ]
        version, notes = wr.latest_endoflife({"product": "go"})
        self.assertEqual(version, "1.22.3")
        self.assertIn("endoflife.date/go", notes)

    def test_endoflife_requires_product(self):
        with self.assertRaises(wr.WatchError):
            wr.latest_endoflife({})

    def test_github_latest_stable(self):
        wr.http_json = lambda url: {
            "tag_name": "v5.4.2",
            "html_url": "https://github.com/microsoft/TypeScript/releases/tag/v5.4.2",
            "prerelease": False,
            "draft": False,
        }
        version, notes = wr.latest_github({"repo": "microsoft/TypeScript"})
        self.assertEqual(version, "5.4.2")
        self.assertIn("releases/tag/v5.4.2", notes)

    def test_github_rejects_prerelease(self):
        wr.http_json = lambda url: {"tag_name": "v6.0.0-beta", "prerelease": True}
        with self.assertRaises(wr.WatchError):
            wr.latest_github({"repo": "microsoft/TypeScript"})

    def test_github_enforces_maintainer_owner(self):
        with self.assertRaises(wr.WatchError):
            wr.latest_github({"repo": "fork/TypeScript", "maintainer_owner": "microsoft"})

    def test_python_feed_picks_newest_published(self):
        wr.http_json = lambda url: [
            {"name": "Python 3.13.1", "is_published": True, "pre_release": False},
            {"name": "Python 3.14.0a1", "is_published": True, "pre_release": True},
            {"name": "Python 3.12.7", "is_published": True, "pre_release": False},
        ]
        version, notes = wr.latest_python({})
        self.assertEqual(version, "3.13.1")
        self.assertIn("python.org/downloads", notes)


class Evaluate(unittest.TestCase):
    def setUp(self):
        self._orig = dict(wr.PROVIDERS)

    def tearDown(self):
        wr.PROVIDERS.clear()
        wr.PROVIDERS.update(self._orig)

    def _stub(self, version):
        wr.PROVIDERS["endoflife"] = lambda watch: (version, "https://exemplo/notas")

    def test_outdated_detected(self):
        self._stub("1.22.3")
        result = wr.evaluate(
            {"id": "go", "name": "Go"},
            {"provider": "endoflife", "product": "go", "current_version": "1.21.0"},
        )
        self.assertEqual(result["status"], "outdated")
        self.assertEqual(result["latest_version"], "1.22.3")

    def test_current_when_equal(self):
        self._stub("1.22.3")
        result = wr.evaluate(
            {"id": "go", "name": "Go"},
            {"provider": "endoflife", "product": "go", "current_version": "1.22.3"},
        )
        self.assertEqual(result["status"], "current")

    def test_new_when_no_current(self):
        self._stub("1.22.3")
        result = wr.evaluate(
            {"id": "go", "name": "Go"},
            {"provider": "endoflife", "product": "go", "current_version": ""},
        )
        self.assertEqual(result["status"], "new")

    def test_unknown_provider_is_error(self):
        result = wr.evaluate({"id": "x", "name": "X"}, {"provider": "inexistente"})
        self.assertEqual(result["status"], "error")

    def test_provider_failure_is_error(self):
        def boom(watch):
            raise wr.WatchError("sem rede")

        wr.PROVIDERS["endoflife"] = boom
        result = wr.evaluate(
            {"id": "go", "name": "Go"},
            {"provider": "endoflife", "product": "go", "current_version": "1.0"},
        )
        self.assertEqual(result["status"], "error")
        self.assertIn("sem rede", result["detail"])


class RenderPR(unittest.TestCase):
    def test_render_contains_table_and_checklist(self):
        report = {
            "generated_at": "2026-10-22",
            "outdated": [
                {
                    "id": "go",
                    "name": "Go",
                    "provider": "endoflife",
                    "current_version": "1.21.0",
                    "latest_version": "1.22.3",
                    "release_notes": "https://endoflife.date/go",
                    "path": "docs/programacao/linguagens/go/tech.yml",
                }
            ],
            "errors": [],
        }
        body = pr.render(report)
        self.assertIn("1.22.3", body)
        self.assertIn("[ ] Revisar", body)
        self.assertIn("docs/programacao/linguagens/go/README.md", body)
        self.assertIn("https://endoflife.date/go", body)

    def test_render_empty_is_safe(self):
        body = pr.render({"generated_at": "2026-10-22", "outdated": [], "errors": []})
        self.assertIn("Nenhuma versão nova", body)


if __name__ == "__main__":
    unittest.main()
