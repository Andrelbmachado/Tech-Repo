# Tech-Repo 📚

[![Validate catalog](https://github.com/Andrelbmachado/Tech-Repo/actions/workflows/validate.yml/badge.svg)](https://github.com/Andrelbmachado/Tech-Repo/actions/workflows/validate.yml)
[![Check source links](https://github.com/Andrelbmachado/Tech-Repo/actions/workflows/links.yml/badge.svg)](https://github.com/Andrelbmachado/Tech-Repo/actions/workflows/links.yml)
![Docs: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey)
![Tools: MIT](https://img.shields.io/badge/tools-MIT-blue)

**Um só lugar para documentação de engenharia, programação e boas práticas — com fontes oficiais rastreáveis, para pessoas e para IAs.**

Cada tecnologia tem uma pasta própria com resumo original, metadados estruturados (`tech.yml`), manifesto de fontes oficiais (`fontes.yml`) e, quando a licença permite, uma cópia local da documentação oficial. Nada é declarado "revisado" sem ter sido: o status de curadoria de cada entrada é explícito.

**Navegação rápida:** [Mapa](MAPA.md) · [Tecnologias](MAPA-TECNOLOGIAS.md) · [Documentação oficial](DOCUMENTACAO-OFICIAL.md) · [Índice para IA](INDICE-IA.yaml) · [Catálogo](CATALOG.yml) · [Plano](PLANO.md) · [Manutenção](MAINTENANCE.md) · [Contribuir](CONTRIBUTING.md) · [Segurança](SECURITY.md)

---

## O que já existe

| Item | Situação atual |
|---|---|
| Tecnologias catalogadas | **104**, em 11 categorias (ver [MAPA-TECNOLOGIAS.md](MAPA-TECNOLOGIAS.md)) |
| Status editorial | 64 `in-progress` · 40 `planned` · **0 `curated`** (nenhuma entrada teve revisão humana final ainda) |
| Quota de 5 fontes oficiais | 3 `complete` · 13 `partial` · 88 `pending` |
| Documentação oficial offline | 50 tecnologias com cópia local · 54 somente com links ([índice](DOCUMENTACAO-OFICIAL.md)) |
| Validação automática | ✅ `tools/validate_catalog.py` + `tools/generate_indexes.py --check` em todo PR ([workflow](.github/workflows/validate.yml)) |
| Checagem de links | ✅ `tools/check_links.py` semanal (segunda, 08:23 UTC) e sob demanda ([workflow](.github/workflows/links.yml)) |
| Índices gerados | ✅ `CATALOG.yml`, `MAPA-TECNOLOGIAS.md` e `INDICE-IA.yaml` gerados a partir dos `tech.yml` |

> Números de 21/10/2026. A fonte da verdade é o `CATALOG.yml`; esta tabela é atualizada manualmente.

## O que está planejado

Itens abaixo **ainda não existem no código** — o detalhamento por fase está no [PLANO.md](PLANO.md).

- 🛠️ **Planejado — vigia de lançamentos:** automação que consulta fontes oficiais (python.org, go.dev, releases do GitHub, endoflife.date) e abre PRs atualizando versões e páginas afetadas.
- 🛠️ **Planejado — curadoria:** primeiras entradas `curated`, quota de fontes fechada e resumos em inglês revisados.
- 🛠️ **Planejado — modo IA:** regra de abstenção e índice enriquecido para agentes que consultam o repositório.

## Como consultar

1. Escolha uma área no [mapa](MAPA.md) ou procure a tecnologia em [MAPA-TECNOLOGIAS.md](MAPA-TECNOLOGIAS.md).
2. Leia o `README.md` da tecnologia para a visão resumida.
3. Consulte `tech.yml` (identidade, status, versão verificada) e `fontes.yml` (autoridade, licença, data de verificação de cada fonte).
4. Confirme informações sensíveis a versão na documentação original indicada em `fontes.yml`.
5. Para uso offline, abra `documentacao-oficial/README.md` da tecnologia: ele diz se há cópia local (com origem, versão, licença e checksum) ou apenas links.

### Estrutura de uma tecnologia

```text
docs/<categoria>/<tecnologia>/
├── README.md              # resumo original
├── tech.yml               # id, status, versão verificada, quota de fontes, revisão
├── fontes.yml             # referências oficiais/secundárias com licença e verified_at
├── versoes.md · conceitos.md · boas-praticas.md · relacionados.md
└── documentacao-oficial/  # manifesto + cópia local (quando a licença permite)
```

### Para agentes de IA

Comece por [`INDICE-IA.yaml`](INDICE-IA.yaml): ele lista cada tecnologia com caminho, status, número de fontes oficiais e se há documentação local. Respeite o `status` — entradas `planned` ou `in-progress` não são referência revisada. Convenções completas em [MAPA.md](MAPA.md#convenções-para-agentes-de-ia) e [AGENTS.md](AGENTS.md).

## Rodando as validações localmente

```sh
python -m pip install -r requirements-dev.txt
python tools/validate_catalog.py        # valida tech.yml, fontes.yml e arquivos obrigatórios
python tools/generate_indexes.py        # regenera CATALOG.yml, MAPA-TECNOLOGIAS.md e INDICE-IA.yaml
python tools/generate_indexes.py --check
python tools/check_links.py             # opcional: testa todas as URLs dos fontes.yml
```

## Política editorial

- **Prioridade de fontes:** mantenedores e organismos normativos; depois documentação oficial de fornecedores, projetos open source e fontes comunitárias identificadas.
- **Quota:** cada tecnologia busca cinco referências oficiais relevantes. Sem cinco fontes adequadas, registre `partial` com justificativa; durante a pesquisa, use `pending`.
- **Cópias de terceiros:** só quando a licença permite, preservando avisos e registrando origem, edição, data, licença e checksum. Um link em `fontes.yml` não significa que o documento foi baixado.
- **Padrões pagos ou restritos** são referenciados sem cópia integral.
- **Idioma:** a meta é resumos bilíngues (pt/en). Hoje o português é a base; o lado em inglês de muitas entradas ainda é provisório.

### Estados

- **Editorial:** `planned` (reserva de entrada) → `in-progress` (material inicial em elaboração) → `curated` (revisão humana concluída).
- **Quota de fontes:** `pending` → `partial` (com justificativa) ou `complete` (≥ 5 fontes oficiais).

## Contribuindo

Veja [CONTRIBUTING.md](CONTRIBUTING.md). Em resumo: siga o padrão de pastas, cite fontes oficiais, rode as validações e explique no PR as fontes usadas. Problemas de segurança: [SECURITY.md](SECURITY.md).

## Licenças

Documentação e resumos originais: [CC BY 4.0](LICENSE), salvo indicação específica. Ferramentas em `tools/`: [MIT](LICENSE-CODE). Conteúdo externo mantém a licença de seus autores; consulte os metadados de cada fonte.

---

> Este README e o PLANO.md foram revisados em 21/10/2026. Itens marcados como **planejado** ainda não existem no código.
