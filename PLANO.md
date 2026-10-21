# PLANO — Tech-Repo

## Fase 1 — Vigia de lançamentos (prioridade)
- [ ] `tools/watch_releases.py`: lê `fontes.yml` de cada tecnologia e consulta feeds oficiais (RSS/Atom de python.org, API de releases do GitHub, endoflife.date).
- [ ] Guardar a última versão conhecida em `tech.yml` (`versao_atual`, `verificado_em`).
- [ ] Workflow agendado (diário) que, ao detectar versão nova, cria uma branch e abre um PR com: versão atualizada, link das release notes e checklist de páginas a revisar.
- [ ] Só fontes credenciadas (mantenedores/organismos normativos) disparam PR.

## Fase 2 — Conteúdo
- [ ] Rascunho do lado EN dos READMEs com tradução offline (Hy-MT2 GGUF) e revisão humana.
- [ ] Catalogar o repositório de leis brasileiras em Markdown como fonte.
- [ ] Página de "melhores práticas" transversais (segurança, testes, CI/CD).

## Fase 3 — Para IAs
- [ ] Manter `INDICE-IA.yaml` gerado automaticamente.
- [ ] Regra de abstenção para agentes que consultam o repo (responder "não documentado" quando não houver fonte).
