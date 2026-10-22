# PLANO — Tech-Repo

## Fase 1 — Vigia de lançamentos (prioridade)
- [x] `tools/watch_releases.py`: lê o bloco `release_watch` de cada `tech.yml` e consulta feeds oficiais (feed de downloads do python.org, API de releases do GitHub, endoflife.date). *(Decisão: a configuração de vigia fica em `tech.yml` — onde já mora a versão — e não em `fontes.yml`, que não tem campo de feed. Feito via provedores em vez de RSS bruto.)*
- [x] Guardar a última versão conhecida em `tech.yml` (`release_watch.current_version`, `release_watch.verificado_em`; também atualiza `latest_verified_version`). Semeado em python, go, rust e typescript.
- [x] Workflow agendado (diário) `.github/workflows/releases.yml` que, ao detectar versão nova, cria a branch `bot/atualiza-versoes` e abre um PR com: versão atualizada, link das release notes e checklist de páginas a revisar (`tools/render_release_pr.py`).
- [x] Só fontes credenciadas (mantenedores/organismos normativos) disparam PR: cada provedor aponta para a origem oficial do projeto e o provedor `github` trava o dono do repositório via `maintainer_owner`.

### Fase 1 — pendências e próximos passos
- [ ] Ampliar `release_watch` para as demais tecnologias com versão volátil (runtimes, navegadores, normas com ciclo de revisão).
- [ ] Mapear automaticamente as páginas afetadas por versão em vez do checklist fixo atual.
- [ ] Opcional: provedor para feeds Atom/RSS genéricos quando o projeto não estiver no endoflife.date nem publicar releases no GitHub.

## Fase 2 — Conteúdo
- [ ] Rascunho do lado EN dos READMEs com tradução offline (Hy-MT2 GGUF) e revisão humana.
- [ ] Catalogar o repositório de leis brasileiras em Markdown como fonte.
- [ ] Página de "melhores práticas" transversais (segurança, testes, CI/CD).

## Fase 3 — Para IAs
- [ ] Manter `INDICE-IA.yaml` gerado automaticamente.
- [ ] Regra de abstenção para agentes que consultam o repo (responder "não documentado" quando não houver fonte).
