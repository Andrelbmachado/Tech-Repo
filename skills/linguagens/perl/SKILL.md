---
name: perl
description: "Escrever e manter scripts e módulos Perl 5. Use quando: Processamento de texto, administração de sistemas, legado web e bioinformática."
---

# Skill: Perl

Escrever e manter scripts e módulos Perl 5.

## Quando usar

Processamento de texto, administração de sistemas, legado web e bioinformática.

## Conceitos principais

- Escalares, arrays e hashes (sigilos `$ @ %`)
- Contexto escalar vs. lista
- Expressões regulares integradas
- Referências e estruturas aninhadas
- Módulos e CPAN

## Boas práticas

- Sempre `use strict; use warnings;`
- Use `my` para escopo léxico
- Use open de três argumentos com handles léxicos
- Consulte `perldoc` (perlfunc, perlfaq)
- Teste com `prove`

## Comandos e padrões comuns

```bash
perl -c script.pl
perl -w script.pl
perldoc perlfunc
perldoc -f open
prove -l t/
```

## Armadilhas comuns

- Confusão de contexto escalar/lista
- Código ilegível por excesso de magia
- Interpolação acidental em strings

## Checklist

- [ ] Sempre `use strict; use warnings;`
- [ ] Use `my` para escopo léxico
- [ ] Use open de três argumentos com handles léxicos
- [ ] Consulte `perldoc` (perlfunc, perlfaq)
- [ ] Teste com `prove`
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/perl/`](../../../docs/programacao/linguagens/perl/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/perl/documentacao-oficial/`](../../../docs/programacao/linguagens/perl/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/perl/fontes.yml)

## Fontes oficiais

- [Perl documentation](https://perldoc.perl.org/) — Perl project
- [Perl language reference](https://perldoc.perl.org/perl) — Perl project
- [Perl functions](https://perldoc.perl.org/perlfunc) — Perl project
- [Perl FAQs](https://perldoc.perl.org/perlfaq) — Perl project
- [Perl core modules](https://perldoc.perl.org/modules) — Perl project
