---
name: erlang
description: "Desenvolver sistemas OTP em Erlang. Use quando: Telecom, mensageria, sistemas distribuídos de alta disponibilidade na BEAM."
---

# Skill: Erlang

Desenvolver sistemas OTP em Erlang.

## Quando usar

Telecom, mensageria, sistemas distribuídos de alta disponibilidade na BEAM.

## Conceitos principais

- Processos, mensagens e `receive`
- Pattern matching e atribuição única
- Princípios de design OTP: `gen_server`, `supervisor`, `application`
- Distribuição entre nós e hot code loading
- Stdlib: `lists`, `maps`, `ets`

## Boas práticas

- Siga os Design Principles do OTP
- Use supervisores e deixe processos falharem
- Use `rebar3` para build, testes e releases
- Consulte o Efficiency Guide antes de otimizar
- Use `dialyzer` com specs de tipo

## Comandos e padrões comuns

```bash
rebar3 new app minha_app
rebar3 compile
rebar3 eunit
rebar3 dialyzer
erl -sname n1
```

## Armadilhas comuns

- Caixa de mensagens crescendo sem `receive` para tudo
- Criar átomos a partir de entrada externa
- Chamadas síncronas em cadeia causando deadlocks

## Checklist

- [ ] Siga os Design Principles do OTP
- [ ] Use supervisores e deixe processos falharem
- [ ] Use `rebar3` para build, testes e releases
- [ ] Consulte o Efficiency Guide antes de otimizar
- [ ] Use `dialyzer` com specs de tipo
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/erlang/`](../../../docs/programacao/linguagens/erlang/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/erlang/documentacao-oficial/`](../../../docs/programacao/linguagens/erlang/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/erlang/fontes.yml)

## Fontes oficiais

- [Erlang documentation](https://www.erlang.org/doc/) — Erlang/OTP team
- [Erlang reference manual](https://www.erlang.org/doc/system/reference_manual.html) — Erlang/OTP team
- [Erlang/OTP design principles](https://www.erlang.org/doc/system/design_principles.html) — Erlang/OTP team
- [Erlang standard library](https://www.erlang.org/doc/apps/stdlib/) — Erlang/OTP team
- [Erlang efficiency guide](https://www.erlang.org/docs/26/efficiency_guide/users_guide.html) — Erlang/OTP team
