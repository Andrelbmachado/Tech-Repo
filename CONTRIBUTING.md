# Como contribuir

Contribuições podem adicionar tecnologias, corrigir metadados, substituir links quebrados ou melhorar resumos bilíngues.

## Padrão de uma tecnologia

Cada tecnologia deve ter uma pasta com `README.md`, `tech.yml`, `fontes.yml`, `versoes.md`, `conceitos.md`, `boas-praticas.md` e `relacionados.md`. IDs e diretórios usam ASCII, minúsculas e `kebab-case`.

`tech.yml` registra identidade, categoria, estado editorial, versões, resumo em português e inglês, tags e relações. `fontes.yml` registra cada referência com organização, URL, tipo, autoridade, idioma, versão/data, acesso/licença e data de verificação.

## Curadoria

- Prefira mantenedores, especificações normativas e documentação primária.
- Registre fornecedores como fontes oficiais de implementação, sem confundi-los com autoridade normativa.
- Procure cinco referências oficiais relevantes. Use `partial` com justificativa quando não houver cinco referências adequadas; use `pending` enquanto a pesquisa não estiver concluída.
- Registre data de verificação, edição/versão e condição de acesso. Não use URLs de busca como fonte.
- Escreva resumos próprios; não copie páginas ou PDFs sem licença compatível.
- Para incluir documentos reais no repositório, obtenha-os do mantenedor ou órgão oficial, confirme que a licença permite redistribuição, preserve os avisos originais e adicione `documentacao-oficial/README.md` com URL direta, versão/edição, data de obtenção, licença, formato, checksum SHA-256 e lista de conteúdo. Não transforme um link em alegação de que há cópia local.
- Não inclua padrões pagos/restritos nem documentação de fornecedor sem autorização. Nesses casos, mantenha a referência oficial e explique a condição de acesso; não contorne login, paywall ou controles de acesso.
- Prefira cópias em texto pesquisável e sem conversões que alterem o conteúdo. Trate cada atualização como nova versão identificável, preservando o histórico.
- Identifique material arquivado, rascunho, proposta e padrão vigente corretamente.

## Antes de abrir um pull request

Instale `requirements-dev.txt` e execute:

```sh
python tools/validate_catalog.py
python tools/generate_indexes.py --check
```

Use `python tools/check_links.py` para verificar links sob demanda. Pull requests devem explicar a alteração e incluir as fontes usadas.
