---
name: julia
description: "Programar em Julia para computação científica e numérica. Use quando: Análise numérica, ciência de dados, simulação e otimização com alto desempenho."
---

# Skill: Julia

Programar em Julia para computação científica e numérica.

## Quando usar

Análise numérica, ciência de dados, simulação e otimização com alto desempenho.

## Conceitos principais

- Multiple dispatch e tipos paramétricos
- Compilação JIT e estabilidade de tipos
- Arrays 1-indexados e broadcasting (`.`)
- Ambientes e pacotes com Pkg
- Macros e metaprogramação

## Boas práticas

- Siga as Performance Tips oficiais: evite globais não tipadas
- Escreva funções type-stable (verifique com `@code_warntype`)
- Use ambientes de projeto (`Project.toml`)
- Documente com docstrings
- Meça com `@time`/BenchmarkTools, descontando a compilação

## Comandos e padrões comuns

```julia
julia --project=.
using Pkg; Pkg.add("Example"); Pkg.test()
@time f(x)
@code_warntype f(x)
```

## Armadilhas comuns

- Variáveis globais lentas
- Instabilidade de tipos
- Tempo de primeira execução (latência de compilação)

## Checklist

- [ ] Siga as Performance Tips oficiais: evite globais não tipadas
- [ ] Escreva funções type-stable (verifique com `@code_warntype`)
- [ ] Use ambientes de projeto (`Project.toml`)
- [ ] Documente com docstrings
- [ ] Meça com `@time`/BenchmarkTools, descontando a compilação
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/julia/`](../../../docs/programacao/linguagens/julia/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/julia/documentacao-oficial/`](../../../docs/programacao/linguagens/julia/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/julia/fontes.yml)

## Fontes oficiais

- [Julia documentation](https://docs.julialang.org/en/v1/) — Julia project
- [Julia language manual](https://docs.julialang.org/en/v1/manual/getting-started/) — Julia project
- [Julia standard library](https://docs.julialang.org/en/v1/manual/installation/) — Julia project
- [Julia developer documentation](https://docs.julialang.org/en/v1/manual/documentation/) — Julia project
- [Julia performance tips](https://docs.julialang.org/en/v1/manual/performance-tips/) — Julia project
