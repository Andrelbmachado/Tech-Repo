# Manutenção do catálogo

## Frequência

- Diário: GitHub Actions (`Watch releases`) consulta as fontes oficiais das tecnologias com bloco `release_watch` e abre um PR quando surge versão nova.
- Semanal: GitHub Actions verifica URLs em `fontes.yml`; erros HTTP e falhas de rede ficam visíveis no workflow.
- Mensal: revisar fontes de maior volatilidade, versões de runtime, documentação de nuvem e páginas de advisories.
- Trimestral: revisar normas, especificações, categorias, fontes secundárias e tecnologias sem atualização editorial.
- Sob demanda: substituir link removido, registrar mudança de status, arquivar uma fonte ou elevar uma entrada para `curated`.

## Ao revisar uma fonte

1. Confirme que o endereço é HTTPS e aponta para o documento, padrão ou landing page oficial identificada.
2. Registre versão/edição, status (vigente, supersedido, rascunho ou arquivado) e condição de acesso.
3. Atualize `verified_at` quando o conteúdo da fonte e os metadados forem conferidos.
4. Não substitua a URL de uma edição antiga quando ela for necessária para contexto; registre a edição atual como nova fonte e marque a antiga nos `notes`.
5. Reavalie `source_quota` e os resumos bilíngues. Atingir cinco links não basta se forem cópias da mesma página ou conteúdo irrelevante.

## Mudanças de status

Use `planned` para esboços sem conteúdo de curadoria, `in-progress` durante pesquisa e revisão, e `curated` quando o resumo e os metadados tiverem revisão humana. Marque a quota como `complete` somente com cinco ou mais fontes oficiais relevantes; `partial` exige justificativa; `pending` significa que a pesquisa continua.

## Vigia de lançamentos (`release_watch`)

Para acompanhar versões automaticamente, declare um bloco `release_watch` no `tech.yml` da tecnologia. Provedores disponíveis em `tools/watch_releases.py`:

- `endoflife` — usa `product` (ex.: `go`, `rust`), consulta `endoflife.date`.
- `github` — usa `repo` (`owner/name`) e opcional `maintainer_owner` para travar o dono credenciado; lê a release mais recente (ignora prerelease/draft).
- `python` — feed oficial de downloads do python.org (sem parâmetros).

Exemplo:

```yaml
release_watch:
  provider: "endoflife"
  product: "go"
  current_version: ""   # preenchido pelo workflow ao detectar/aplicar
  verificado_em: ""
  notes: "endoflife.date acompanha os lançamentos estáveis do Go."
```

Execução local: `python tools/watch_releases.py` (relata), `--write` (grava no `tech.yml`), `--json saida.json` (relatório para o PR), `--only <id...>` (limita). Só adicione provedores que apontem para a origem oficial do projeto.

## Links quebrados

Tente a URL canônica do mantenedor ou organismo. Registre redirecionamento permanente quando útil. Se o material tiver sido removido, procure a página oficial de arquivo ou a revisão substituta; não aponte para cópias não autorizadas. Falhas temporárias de rede não devem ser registradas como remoção sem nova checagem.
