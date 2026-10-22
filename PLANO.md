# PLANO — Tech-Repo

Plano executável por fases. Cada tarefa tem entregável, critério de pronto e dependência. Tudo marcado `[ ]` é **planejado** e ainda não existe no código.

## Ponto de partida (21/10/2026)

O que já existe e serve de base:

- `tools/validate_catalog.py` — valida campos de `tech.yml`/`fontes.yml`, arquivos obrigatórios e quota; roda em todo PR (`.github/workflows/validate.yml`).
- `tools/generate_indexes.py` — gera `CATALOG.yml`, `MAPA-TECNOLOGIAS.md` e `INDICE-IA.yaml` a partir dos `tech.yml`; `--check` falha se estiverem desatualizados.
- `tools/check_links.py` — testa URLs dos `fontes.yml`; roda semanalmente (`.github/workflows/links.yml`).
- 104 tecnologias: 64 `in-progress`, 40 `planned`, 0 `curated`. Quota: 3 `complete`, 13 `partial`, 88 `pending`.
- `tech.yml` já tem `latest_verified_version` (texto livre, ex.: Python `"3.15 (cópia de documentação; confirmar status de lançamento)"`), `last_reviewed` e `next_review`.

Lacunas observadas: `latest_verified_version` não é legível por máquina; `DOCUMENTACAO-OFICIAL.md` é mantido à mão (não sai do gerador); categorias `fundamentos`, `programacao/bancos-de-dados` e `programacao/runtimes-e-frameworks` têm README mas nenhuma tecnologia.

---

## Fase 1 — Vigia de lançamentos (prioridade)

Objetivo: detectar versão nova em fonte oficial e abrir PR automaticamente, sem nunca editar conteúdo sem revisão humana.

- [ ] **1.1 Schema do vigia.** Adicionar bloco opcional `release_watch` ao `tech.yml`:
  ```yaml
  release_watch:
    provider: "github-releases"   # github-releases | endoflife-date | rss
    target: "python/cpython"      # repo, produto do endoflife.date ou URL do feed
    version_pattern: "^v?(\\d+\\.\\d+\\.\\d+)$"
    include_prereleases: false
  current_version: "3.14.0"        # semver puro, legível por máquina
  ```
  Estender `validate_catalog.py` para validar `provider`, presença de `target` e que `target` aponta para domínio presente em `fontes.yml` com `authority: primary` ou `official-vendor`.
  *Pronto quando:* validador aceita/rejeita casos de teste; `latest_verified_version` continua existindo (texto humano).

- [ ] **1.2 Piloto em 5 tecnologias** com fonte fácil: Python, Go, Rust, TypeScript e Linux (todas já no catálogo; Node.js ainda não tem entrada). Preencher `release_watch` e `current_version`.
  *Depende de:* 1.1.

- [ ] **1.3 `tools/watch_releases.py`.** Para cada `tech.yml` com `release_watch`: consulta o provedor (GitHub API `/repos/{target}/releases/latest` com `GITHUB_TOKEN`; `https://endoflife.date/api/{target}.json`; RSS/Atom via `urllib` + `xml.etree`), compara com `current_version` e emite JSON `[{id, current, latest, release_url}]`. Flags: `--dry-run` (só relata), `--only <id>`. Sem dependências novas além de `pyyaml`.
  *Pronto quando:* `python tools/watch_releases.py --dry-run` lista corretamente as 5 do piloto; falha de rede em uma fonte não derruba as outras (mesmo padrão de `check_links.py`).
  *Depende de:* 1.2.

- [ ] **1.4 Workflow `.github/workflows/watch-releases.yml`.** Cron diário + `workflow_dispatch`, `permissions: contents: write, pull-requests: write`. Para cada versão nova: branch `release/<id>-<versao>`, atualiza `current_version` e `last_reviewed`, roda `generate_indexes.py`, abre PR com link das release notes e checklist (`versoes.md`, `README.md`, `documentacao-oficial/`). Não abre PR duplicado se a branch já existir.
  *Pronto quando:* execução manual gera 1 PR de teste válido que passa no `validate.yml`.
  *Depende de:* 1.3.

- [ ] **1.5 Expandir** `release_watch` para todas as tecnologias versionadas (linguagens, runtimes, SOs). Tecnologias sem versão (normas, conceitos) ficam fora e isso é documentado em `MAINTENANCE.md`.

**Regra:** só `target` ligado a fonte `primary`/`official-vendor` dispara PR. Fontes secundárias nunca.

---

## Fase 2 — Curadoria de conteúdo

Objetivo: sair de 0 entradas `curated`.

- [ ] **2.1 Fechar quota das entradas `partial` (13)**: completar fontes ou justificar `exception_reason`. *Pronto quando:* `validate_catalog.py` passa e cada `partial` tem justificativa específica.
- [ ] **2.2 Primeiras 10 entradas `curated`**, começando pelas 3 com quota `complete` (Linux, Licenças de software, Periféricos) e pelas com cópia local. Critério de `curated`: resumo próprio revisado, `fontes.yml` com `verified_at` ≤ 90 dias, `next_review` preenchido.
- [ ] **2.3 Lado EN dos READMEs**: rascunho por tradução offline (Hy-MT2 GGUF) marcado como `draft`, revisão humana antes de virar `curated`.
- [ ] **2.4 Gerar `DOCUMENTACAO-OFICIAL.md`** a partir de `generate_indexes.py` (hoje é manual) e incluí-lo no `--check`.
- [ ] **2.5 Preencher categorias vazias** (`fundamentos`, `bancos-de-dados`, `runtimes-e-frameworks`) com ao menos 1 entrada `planned` cada, ou remover da hierarquia.
- [ ] **2.6 Catalogar o repositório de leis brasileiras em Markdown** como fonte (verificar licença antes).
- [ ] **2.7 Página de boas práticas transversais** (segurança, testes, CI/CD) ligando entradas existentes de `ciberseguranca/`, `devops-e-cloud/` e `engenharia-de-software/`.

---

## Fase 3 — Para IAs

- [ ] **3.1 Enriquecer `INDICE-IA.yaml`** com `current_version`, `last_reviewed` e `next_review` (já é gerado automaticamente; só ampliar campos em `generate_indexes.py`).
- [ ] **3.2 Regra de abstenção** em `AGENTS.md` e `MAPA.md`: agente responde "não documentado no Tech-Repo" quando não houver fonte em `fontes.yml`, e sinaliza quando a entrada não for `curated`.
- [ ] **3.3 Alerta de revisão vencida**: `validate_catalog.py --warn-stale` lista entradas com `next_review` no passado (aviso, não erro).

---

## Ordem sugerida

1.1 → 1.2 → 1.3 → 1.4 (vigia funcionando no piloto) → 2.1/2.2 em paralelo com 1.5 → 2.4 → Fase 3.

Cada tarefa vira um PR pequeno a partir de `main`, passando em `validate.yml` antes do merge.
