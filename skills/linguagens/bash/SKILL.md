---
name: bash
description: "Escrever, revisar e depurar scripts de shell GNU Bash. Use quando: Automação de tarefas no terminal, scripts de build/deploy, manipulação de arquivos e processos em sistemas Unix-like."
---

# Skill: Bash

Escrever, revisar e depurar scripts de shell GNU Bash.

## Quando usar

Automação de tarefas no terminal, scripts de build/deploy, manipulação de arquivos e processos em sistemas Unix-like.

## Conceitos principais

- Expansões: parâmetros, aritmética, comandos `$(...)`, globbing e ordem de expansão
- Redirecionamentos e pipes (`>`, `>>`, `2>&1`, `<<EOF`, `|`)
- Status de saída (`$?`), `&&`, `||` e condicionais `[[ ]]`
- Arrays indexados e associativos (`declare -A`)
- Funções, escopo `local` e `trap` para limpeza

## Boas práticas

- Comece scripts com `#!/usr/bin/env bash` e `set -euo pipefail`
- Sempre coloque variáveis entre aspas: `"$var"`
- Prefira `[[ ]]` a `[ ]` e `$(...)` a crases
- Use `shellcheck` antes de versionar
- Trate argumentos com `getopts` e mostre `usage`

## Comandos e padrões comuns

```bash
set -euo pipefail
trap 'rm -f "$tmp"' EXIT
tmp=$(mktemp)
for f in "$@"; do
  [[ -f "$f" ]] || { echo "não encontrado: $f" >&2; exit 1; }
done
while IFS= read -r linha; do echo "$linha"; done < arquivo.txt
bash -n script.sh   # checa sintaxe
bash -x script.sh   # rastreia execução
```

## Armadilhas comuns

- Word splitting em variáveis sem aspas
- Fazer parsing da saída de `ls`
- `set -e` não dispara dentro de condicionais e alguns pipelines
- Diferenças entre Bash e `sh` POSIX (bashismos)

## Checklist

- [ ] Comece scripts com `#!/usr/bin/env bash` e `set -euo pipefail`
- [ ] Sempre coloque variáveis entre aspas: `"$var"`
- [ ] Prefira `[[ ]]` a `[ ]` e `$(...)` a crases
- [ ] Use `shellcheck` antes de versionar
- [ ] Trate argumentos com `getopts` e mostre `usage`
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/bash/`](../../../docs/programacao/linguagens/bash/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/bash/documentacao-oficial/`](../../../docs/programacao/linguagens/bash/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/bash/fontes.yml)

## Fontes oficiais

- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) — GNU Project
- [Bash manual: shell syntax](https://www.gnu.org/software/bash/manual/html_node/Shell-Syntax.html) — GNU Project
- [Bash manual: shell expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html) — GNU Project
- [Bash manual: redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html) — GNU Project
- [Bash manual: command history](https://www.gnu.org/s/bash/manual/html_node/Bash-History-Facilities.html) — GNU Project
