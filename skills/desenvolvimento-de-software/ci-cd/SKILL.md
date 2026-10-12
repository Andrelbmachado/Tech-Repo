---
name: ci-cd
description: "Configurar integração e entrega contínuas. Use quando: Automatizar build, testes, análise e deploy a cada mudança."
---

# Skill: CI/CD

Configurar integração e entrega contínuas.

## Quando usar

Automatizar build, testes, análise e deploy a cada mudança.

## Conceitos principais

- Integração contínua: integrar e testar com frequência
- Entrega vs. implantação contínua
- Pipelines: estágios, jobs, artefatos
- Ambientes e promoção
- Rollback e deploys progressivos

## Boas práticas

- Pipeline rápido com falha cedo
- Build reprodutível e artefato único promovido entre ambientes
- Segredos em cofre do CI, nunca no repositório
- Proteja a branch principal com checks obrigatórios
- Monitore e permita rollback rápido

## Comandos e padrões comuns

```yaml
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: make test
```

## Armadilhas comuns

- Pipelines lentos ignorados pelo time
- Testes instáveis tolerados
- Deploy manual divergente do pipeline

## Checklist

- [ ] Pipeline rápido com falha cedo
- [ ] Build reprodutível e artefato único promovido entre ambientes
- [ ] Segredos em cofre do CI, nunca no repositório
- [ ] Proteja a branch principal com checks obrigatórios
- [ ] Monitore e permita rollback rápido
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/devops-e-cloud/ci-cd/`](../../../docs/devops-e-cloud/ci-cd/README.md)
- Documentação oficial (cópia local ou links): [`docs/devops-e-cloud/ci-cd/documentacao-oficial/`](../../../docs/devops-e-cloud/ci-cd/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/devops-e-cloud/ci-cd/fontes.yml)

## Fontes oficiais

- Nenhuma fonte primária cadastrada ainda em `fontes.yml`; consulte a ficha da tecnologia e complete a curadoria antes de tratar esta skill como referência revisada.
