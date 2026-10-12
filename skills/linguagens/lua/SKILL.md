---
name: lua
description: "Programar em Lua 5.4 e embutir Lua em aplicações. Use quando: Scripting embutido (jogos, Neovim, Redis, nginx/OpenResty), configuração e extensões."
---

# Skill: Lua

Programar em Lua 5.4 e embutir Lua em aplicações.

## Quando usar

Scripting embutido (jogos, Neovim, Redis, nginx/OpenResty), configuração e extensões.

## Conceitos principais

- Tabelas como estrutura única (arrays e dicionários)
- Metatables e metamétodos
- Closures e upvalues
- Coroutines
- API C para embutir

## Boas práticas

- Declare variáveis com `local`
- Use `ipairs` para sequências e `pairs` para mapas
- Lembre que índices começam em 1
- Verifique a versão do Lua do ambiente (5.1/LuaJIT vs 5.4)
- Trate erros com `pcall`/`error`

## Comandos e padrões comuns

```bash
lua script.lua
luac -p script.lua   # checa sintaxe
lua -i
```

## Armadilhas comuns

- Globais acidentais por esquecer `local`
- Operador `#` em tabelas com buracos
- Diferenças entre versões 5.1/5.2/5.3/5.4

## Checklist

- [ ] Declare variáveis com `local`
- [ ] Use `ipairs` para sequências e `pairs` para mapas
- [ ] Lembre que índices começam em 1
- [ ] Verifique a versão do Lua do ambiente (5.1/LuaJIT vs 5.4)
- [ ] Trate erros com `pcall`/`error`
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/lua/`](../../../docs/programacao/linguagens/lua/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/lua/documentacao-oficial/`](../../../docs/programacao/linguagens/lua/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/lua/fontes.yml)

## Fontes oficiais

- [Lua 5.4 Reference Manual](https://www.lua.org/manual/5.4/) — Lua.org
- [Lua 5.3 Reference Manual](https://www.lua.org/manual/5.3/) — Lua.org
- [Lua 5.2 Reference Manual](https://www.lua.org/manual/5.2/) — Lua.org
- [Lua 5.1 Reference Manual](https://www.lua.org/manual/5.1/) — Lua.org
- [Programming in Lua](https://www.lua.org/pil/) — Lua.org
