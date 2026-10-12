---
name: haskell
description: "Programar em Haskell (Haskell 2010 + extensões GHC). Use quando: Programação funcional pura, compiladores, DSLs e sistemas com forte tipagem."
---

# Skill: Haskell

Programar em Haskell (Haskell 2010 + extensões GHC).

## Quando usar

Programação funcional pura, compiladores, DSLs e sistemas com forte tipagem.

## Conceitos principais

- Funções puras, avaliação preguiçosa e imutabilidade
- Tipos algébricos e pattern matching
- Type classes (`Functor`, `Applicative`, `Monad`)
- `IO` e efeitos
- Extensões de linguagem do GHC

## Boas práticas

- Escreva assinaturas de tipo para funções de topo
- Compile com `-Wall`
- Prefira estruturas estritas quando acumular (`foldl'`)
- Ative extensões explicitamente por módulo
- Use cabal ou stack com versões fixadas

## Comandos e padrões comuns

```bash
ghc -Wall Main.hs
ghci
cabal init && cabal build && cabal test
cabal run
```

## Armadilhas comuns

- Space leaks por avaliação preguiçosa (thunks acumulados)
- Funções parciais (`head`, `fromJust`)
- Uso indiscriminado de extensões

## Checklist

- [ ] Escreva assinaturas de tipo para funções de topo
- [ ] Compile com `-Wall`
- [ ] Prefira estruturas estritas quando acumular (`foldl'`)
- [ ] Ative extensões explicitamente por módulo
- [ ] Use cabal ou stack com versões fixadas
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/haskell/`](../../../docs/programacao/linguagens/haskell/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/haskell/documentacao-oficial/`](../../../docs/programacao/linguagens/haskell/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/haskell/fontes.yml)

## Fontes oficiais

- [Haskell 2010 Language Report](https://www.haskell.org/onlinereport/haskell2010/) — Haskell.org
- [GHC User Guide](https://ghc.gitlab.haskell.org/ghc/doc/users_guide/) — GHC team
- [GHC libraries documentation](https://downloads.haskell.org/ghc/latest/docs/libraries/) — GHC team
- [Haskell documentation portal](https://www.haskell.org/documentation/) — Haskell.org
- [Haskell 2010 report PDF](https://www.haskell.org/definition/haskell2010.pdf) — Haskell.org
