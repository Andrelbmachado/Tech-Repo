---
name: elixir
description: "Desenvolver sistemas concorrentes e tolerantes a falhas em Elixir/OTP. Use quando: Serviços web (Phoenix), sistemas distribuídos, processamento concorrente na BEAM."
---

# Skill: Elixir

Desenvolver sistemas concorrentes e tolerantes a falhas em Elixir/OTP.

## Quando usar

Serviços web (Phoenix), sistemas distribuídos, processamento concorrente na BEAM.

## Conceitos principais

- Dados imutáveis e pattern matching
- Processos leves e troca de mensagens
- OTP: `GenServer`, `Supervisor`, aplicações
- Mix: projetos, dependências e tarefas
- Pipe operator `|>` e protocolos

## Boas práticas

- Estruture com árvores de supervisão ("let it crash")
- Use `mix format` e `mix test` no CI
- Documente módulos com `@moduledoc`/`@doc`
- Evite os anti-padrões listados na documentação oficial
- Use `with` para encadear operações que podem falhar

## Comandos e padrões comuns

```bash
mix new app --sup
mix deps.get
mix test
mix format
iex -S mix
```

## Armadilhas comuns

- Gargalo por um único `GenServer` serializando tudo
- Átomos criados dinamicamente (não são coletados)
- Mensagens acumulando na caixa de entrada do processo

## Checklist

- [ ] Estruture com árvores de supervisão ("let it crash")
- [ ] Use `mix format` e `mix test` no CI
- [ ] Documente módulos com `@moduledoc`/`@doc`
- [ ] Evite os anti-padrões listados na documentação oficial
- [ ] Use `with` para encadear operações que podem falhar
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/elixir/`](../../../docs/programacao/linguagens/elixir/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/elixir/documentacao-oficial/`](../../../docs/programacao/linguagens/elixir/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/elixir/fontes.yml)

## Fontes oficiais

- [Elixir getting started](https://elixir-lang.org/getting-started/introduction.html) — Elixir core team
- [Elixir documentation](https://elixir-lang.org/docs.html) — Elixir core team
- [Elixir module documentation](https://hexdocs.pm/elixir/) — Elixir core team
- [Mix and OTP guide](https://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html) — Elixir core team
- [Elixir style guide](https://hexdocs.pm/elixir/main/code-anti-patterns.html) — Elixir core team
