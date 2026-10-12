---
name: zig
description: "Programar em Zig com controle explícito de memória. Use quando: Sistemas, substituição/integração com C, ferramentas e cross-compilation."
---

# Skill: Zig

Programar em Zig com controle explícito de memória.

## Quando usar

Sistemas, substituição/integração com C, ferramentas e cross-compilation.

## Conceitos principais

- Alocadores explícitos
- `comptime` e genéricos
- Error unions (`!T`) e `try`/`catch`
- `defer` e `errdefer`
- Build system (`build.zig`)

## Boas práticas

- Passe alocadores como parâmetro
- Use `defer`/`errdefer` para liberar recursos
- Use o modo Debug/ReleaseSafe em testes
- Escreva blocos `test` junto ao código
- Fixe a versão do Zig (linguagem pré-1.0 muda entre versões)

## Comandos e padrões comuns

```bash
zig init
zig build
zig build test
zig run main.zig
zig test main.zig
```

## Armadilhas comuns

- Mudanças incompatíveis entre versões
- Vazamentos ao esquecer `defer`
- Comportamento ilegal desativado em ReleaseFast

## Checklist

- [ ] Passe alocadores como parâmetro
- [ ] Use `defer`/`errdefer` para liberar recursos
- [ ] Use o modo Debug/ReleaseSafe em testes
- [ ] Escreva blocos `test` junto ao código
- [ ] Fixe a versão do Zig (linguagem pré-1.0 muda entre versões)
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/zig/`](../../../docs/programacao/linguagens/zig/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/zig/documentacao-oficial/`](../../../docs/programacao/linguagens/zig/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/zig/fontes.yml)

## Fontes oficiais

- [Zig language reference](https://ziglang.org/documentation/) — Zig project
- [Zig standard library](https://ziglang.org/documentation/master/std/) — Zig project
- [Zig build system](https://ziglang.org/learn/build-system/) — Zig project
- [Zig language overview](https://ziglang.org/learn/overview/) — Zig project
- [Zig release notes](https://ziglang.org/download/) — Zig project
