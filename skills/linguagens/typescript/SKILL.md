---
name: typescript
description: "Programar em TypeScript com tipagem estática, com base no Handbook local. Use quando: Front-end e back-end JavaScript com segurança de tipos."
---

# Skill: TypeScript

Programar em TypeScript com tipagem estática, com base no Handbook local.

## Quando usar

Front-end e back-end JavaScript com segurança de tipos.

## Conceitos principais

- Tipos estruturais, interfaces e type aliases
- Union, intersection e narrowing
- Generics e utility types
- `tsconfig.json` e opções `strict`
- Arquivos de declaração (`.d.ts`)

## Boas práticas

- Ative `"strict": true`
- Evite `any`; prefira `unknown` com narrowing
- Rode `tsc --noEmit` no CI
- Modele estados com discriminated unions
- Mantenha tipos próximos ao domínio

## Comandos e padrões comuns

```bash
npm install --save-dev typescript
npx tsc --init
npx tsc --noEmit
npx tsc -p .
```

## Armadilhas comuns

- Tipos são apagados em runtime (valide dados externos)
- Asserções `as` escondendo erros
- `any` contaminando o código

## Checklist

- [ ] Ative `"strict": true`
- [ ] Evite `any`; prefira `unknown` com narrowing
- [ ] Rode `tsc --noEmit` no CI
- [ ] Modele estados com discriminated unions
- [ ] Mantenha tipos próximos ao domínio
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/typescript/`](../../../docs/programacao/linguagens/typescript/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/typescript/documentacao-oficial/`](../../../docs/programacao/linguagens/typescript/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/typescript/fontes.yml)

## Fontes oficiais

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) — Microsoft / TypeScript team
- [TypeScript documentation](https://www.typescriptlang.org/docs/) — Microsoft / TypeScript team
- [TSConfig Reference](https://www.typescriptlang.org/tsconfig/) — Microsoft / TypeScript team
- [TypeScript release notes](https://www.typescriptlang.org/docs/handbook/release-notes/overview.html) — Microsoft / TypeScript team
- [TypeScript GitHub repository](https://github.com/microsoft/TypeScript) — Microsoft / TypeScript team
