---
name: api-documentation
description: "Projetar e documentar APIs HTTP com OpenAPI 3.1 (cópia local). Use quando: Especificar contratos de API REST, gerar documentação e clientes."
---

# Skill: Documentação de APIs (OpenAPI)

Projetar e documentar APIs HTTP com OpenAPI 3.1 (cópia local).

## Quando usar

Especificar contratos de API REST, gerar documentação e clientes.

## Conceitos principais

- Documento OpenAPI: `openapi`, `info`, `paths`, `components`
- Operações, parâmetros, request bodies e responses
- Schemas (JSON Schema 2020-12 no OAS 3.1)
- Security schemes
- Versionamento de API

## Boas práticas

- Trate a especificação como contrato (design-first)
- Reutilize schemas em `components`
- Documente erros e códigos de status
- Valide a especificação no CI
- Versione mudanças incompatíveis

## Comandos e padrões comuns

```yaml
openapi: 3.1.1
info: {title: Exemplo, version: 1.0.0}
paths:
  /itens/{id}:
    get:
      parameters:
        - {name: id, in: path, required: true, schema: {type: string}}
      responses:
        "200": {description: OK}
        "404": {description: Não encontrado}
```

## Armadilhas comuns

- Documentação divergente da implementação
- Mudanças quebradas sem nova versão
- Respostas de erro não documentadas

## Checklist

- [ ] Trate a especificação como contrato (design-first)
- [ ] Reutilize schemas em `components`
- [ ] Documente erros e códigos de status
- [ ] Valide a especificação no CI
- [ ] Versione mudanças incompatíveis
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/engenharia-de-software/api-documentation/`](../../../docs/engenharia-de-software/api-documentation/README.md)
- Documentação oficial (cópia local ou links): [`docs/engenharia-de-software/api-documentation/documentacao-oficial/`](../../../docs/engenharia-de-software/api-documentation/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/engenharia-de-software/api-documentation/fontes.yml)

## Fontes oficiais

- Nenhuma fonte primária cadastrada ainda em `fontes.yml`; consulte a ficha da tecnologia e complete a curadoria antes de tratar esta skill como referência revisada.
