---
name: git
description: "Usar Git para controle de versão, com base no Pro Git local. Use quando: Versionar código, colaborar em branches e PRs, investigar histórico."
---

# Skill: Git

Usar Git para controle de versão, com base no Pro Git local.

## Quando usar

Versionar código, colaborar em branches e PRs, investigar histórico.

## Conceitos principais

- Working tree, index (staging) e commits
- Branches, merge e rebase
- Remotos: `fetch`, `pull`, `push`
- Histórico: `log`, `diff`, `blame`, `bisect`
- Tags e releases

## Boas práticas

- Commits pequenos com mensagens descritivas
- Não reescreva histórico já publicado
- Use branches de feature e PRs
- Mantenha `.gitignore` e nunca versione segredos
- Faça `git pull --rebase` ou merge conforme a convenção do time

## Comandos e padrões comuns

```bash
git switch -c feature/x
git add -p
git commit -m "feat: descrição"
git fetch && git rebase origin/main
git push -u origin feature/x
git log --oneline --graph
git bisect start
```

## Armadilhas comuns

- `push --force` em branch compartilhada
- Commitar segredos (exige rotação, não só remoção)
- Arquivos binários grandes no repositório

## Checklist

- [ ] Commits pequenos com mensagens descritivas
- [ ] Não reescreva histórico já publicado
- [ ] Use branches de feature e PRs
- [ ] Mantenha `.gitignore` e nunca versione segredos
- [ ] Faça `git pull --rebase` ou merge conforme a convenção do time
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/engenharia-de-software/git/`](../../../docs/engenharia-de-software/git/README.md)
- Documentação oficial (cópia local ou links): [`docs/engenharia-de-software/git/documentacao-oficial/`](../../../docs/engenharia-de-software/git/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/engenharia-de-software/git/fontes.yml)

## Fontes oficiais

- [Git reference documentation](https://git-scm.com/docs) — Git project
- [Git user manual](https://git-scm.com/docs/user-manual) — Git project
- [Git book](https://git-scm.com/book/en/v2) — Scott Chacon and Ben Straub / Git project
- [Git workflows](https://git-scm.com/docs/gitworkflows) — Git project
- [Git repository layout](https://git-scm.com/docs/gitrepository-layout) — Git project
