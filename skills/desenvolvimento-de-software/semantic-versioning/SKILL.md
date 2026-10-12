---
name: semantic-versioning
description: "Versionar releases com SemVer 2.0.0 (cópia local). Use quando: Definir números de versão de bibliotecas e APIs públicas."
---

# Skill: Versionamento Semântico

Versionar releases com SemVer 2.0.0 (cópia local).

## Quando usar

Definir números de versão de bibliotecas e APIs públicas.

## Conceitos principais

- MAJOR.MINOR.PATCH
- MAJOR: mudança incompatível; MINOR: funcionalidade compatível; PATCH: correção compatível
- Pré-releases (`1.0.0-alpha.1`) e metadados de build (`+build`)
- `0.y.z` indica API instável
- Precedência de versões

## Boas práticas

- Declare explicitamente a API pública
- Nunca modifique uma versão já publicada
- Mantenha um CHANGELOG
- Use tags Git (`v1.2.3`)
- Comece em `1.0.0` quando a API estiver em produção

## Comandos e padrões comuns

```bash
git tag -a v1.4.0 -m "v1.4.0"
git push origin v1.4.0
```

## Armadilhas comuns

- Quebrar compatibilidade em MINOR/PATCH
- Permanecer em 0.x indefinidamente
- Republicar uma versão com conteúdo diferente

## Checklist

- [ ] Declare explicitamente a API pública
- [ ] Nunca modifique uma versão já publicada
- [ ] Mantenha um CHANGELOG
- [ ] Use tags Git (`v1.2.3`)
- [ ] Comece em `1.0.0` quando a API estiver em produção
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/engenharia-de-software/semantic-versioning/`](../../../docs/engenharia-de-software/semantic-versioning/README.md)
- Documentação oficial (cópia local ou links): [`docs/engenharia-de-software/semantic-versioning/documentacao-oficial/`](../../../docs/engenharia-de-software/semantic-versioning/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/engenharia-de-software/semantic-versioning/fontes.yml)

## Fontes oficiais

- Nenhuma fonte primária cadastrada ainda em `fontes.yml`; consulte a ficha da tecnologia e complete a curadoria antes de tratar esta skill como referência revisada.
