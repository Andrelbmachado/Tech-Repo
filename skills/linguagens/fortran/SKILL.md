---
name: fortran
description: "Programar em Fortran moderno (2008/2018/2023) para computação científica. Use quando: Simulação numérica, HPC, álgebra linear e código científico legado."
---

# Skill: Fortran

Programar em Fortran moderno (2008/2018/2023) para computação científica.

## Quando usar

Simulação numérica, HPC, álgebra linear e código científico legado.

## Conceitos principais

- Módulos, `implicit none` e tipos derivados
- Arrays multidimensionais e operações de array inteiro
- `intent(in/out/inout)` em argumentos
- Coarrays e `do concurrent` para paralelismo
- Interoperabilidade com C (`iso_c_binding`)

## Boas práticas

- Sempre use `implicit none`
- Organize código em módulos em vez de `common` blocks
- Declare `intent` em todos os argumentos
- Compile com verificação: `-fcheck=all -Wall` em depuração
- Use `kind` explícito (`real64` de `iso_fortran_env`)

## Comandos e padrões comuns

```bash
gfortran -std=f2018 -Wall -fcheck=all -g prog.f90 -o prog
gfortran -O3 -march=native prog.f90 -o prog
fpm new app && fpm build && fpm test
```

## Armadilhas comuns

- Arrays são column-major (ordem de laços importa)
- Tipagem implícita esconde erros de digitação
- Mistura de precisões reais sem `kind` explícito

## Checklist

- [ ] Sempre use `implicit none`
- [ ] Organize código em módulos em vez de `common` blocks
- [ ] Declare `intent` em todos os argumentos
- [ ] Compile com verificação: `-fcheck=all -Wall` em depuração
- [ ] Use `kind` explícito (`real64` de `iso_fortran_env`)
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/fortran/`](../../../docs/programacao/linguagens/fortran/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/fortran/documentacao-oficial/`](../../../docs/programacao/linguagens/fortran/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/fortran/fontes.yml)

## Fontes oficiais

- [Fortran standards committee resources](https://j3-fortran.org/) — J3 / US Fortran standards committee
- [GNU Fortran documentation](https://gcc.gnu.org/onlinedocs/gfortran/) — GNU Project
- [Intel Fortran compiler documentation](https://www.intel.com/content/www/us/en/developer/tools/oneapi/fortran-compiler.html) — Intel
- [LLVM Flang documentation](https://flang.llvm.org/docs/) — LLVM Project
- [Fortran-lang guides](https://fortran-lang.org/learn/) — Fortran-lang community
