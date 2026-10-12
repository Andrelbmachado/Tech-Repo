---
name: ruby
description: "Programar em Ruby e aplicações Rails. Use quando: Aplicações web (Rails), scripts, automação e DSLs."
---

# Skill: Ruby

Programar em Ruby e aplicações Rails.

## Quando usar

Aplicações web (Rails), scripts, automação e DSLs.

## Conceitos principais

- Tudo é objeto; métodos e mensagens
- Blocks, procs e lambdas
- Módulos e mixins
- Símbolos, Array e Hash
- Gems e Bundler

## Boas práticas

- Siga o estilo da comunidade e use RuboCop
- Gerencie dependências com Bundler (`Gemfile.lock`)
- Escreva testes (Minitest/RSpec)
- Use `frozen_string_literal`
- Evite monkey patching em código de biblioteca

## Comandos e padrões comuns

```bash
ruby -c script.rb
ruby script.rb
irb
bundle install
bundle exec rake test
ri Array#map
```

## Armadilhas comuns

- Monkey patching conflitante
- `nil` inesperado propagando
- Diferenças entre `proc` e `lambda` em `return`

## Checklist

- [ ] Siga o estilo da comunidade e use RuboCop
- [ ] Gerencie dependências com Bundler (`Gemfile.lock`)
- [ ] Escreva testes (Minitest/RSpec)
- [ ] Use `frozen_string_literal`
- [ ] Evite monkey patching em código de biblioteca
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/ruby/`](../../../docs/programacao/linguagens/ruby/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/ruby/documentacao-oficial/`](../../../docs/programacao/linguagens/ruby/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/ruby/fontes.yml)

## Fontes oficiais

- [Ruby documentation](https://www.ruby-lang.org/en/documentation/) — Ruby project
- [Ruby core API documentation](https://docs.ruby-lang.org/en/master/) — Ruby core team
- [Ruby syntax reference](https://docs.ruby-lang.org/en/master/syntax_rdoc.html) — Ruby core team
- [Ruby standard libraries](https://docs.ruby-lang.org/en/master/Array.html) — Ruby core team
- [Ruby command-line options](https://docs.ruby-lang.org/en/master/Hash.html) — Ruby core team
