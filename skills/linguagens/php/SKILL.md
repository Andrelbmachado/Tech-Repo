---
name: php
description: "Desenvolver aplicações PHP 8 modernas. Use quando: Back-end web, CMS (WordPress), APIs e frameworks (Laravel, Symfony)."
---

# Skill: PHP

Desenvolver aplicações PHP 8 modernas.

## Quando usar

Back-end web, CMS (WordPress), APIs e frameworks (Laravel, Symfony).

## Conceitos principais

- Tipos escalares, union types e `declare(strict_types=1)`
- Classes, interfaces, traits e enums
- Composer e autoload PSR-4
- Funções e closures
- Extensões

## Boas práticas

- Use `declare(strict_types=1);`
- Use prepared statements (PDO) contra SQL injection
- Escape saída HTML (`htmlspecialchars`)
- Gerencie dependências com Composer
- Rode análise estática e testes (PHPUnit)

## Comandos e padrões comuns

```bash
php -l arquivo.php
php -S localhost:8000
composer install
composer dump-autoload
vendor/bin/phpunit
```

## Armadilhas comuns

- Comparação frouxa `==`
- Concatenar entrada do usuário em SQL
- Exibir erros em produção

## Checklist

- [ ] Use `declare(strict_types=1);`
- [ ] Use prepared statements (PDO) contra SQL injection
- [ ] Escape saída HTML (`htmlspecialchars`)
- [ ] Gerencie dependências com Composer
- [ ] Rode análise estática e testes (PHPUnit)
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/php/`](../../../docs/programacao/linguagens/php/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/php/documentacao-oficial/`](../../../docs/programacao/linguagens/php/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/php/fontes.yml)

## Fontes oficiais

- [PHP manual](https://www.php.net/manual/en/) — PHP Group
- [PHP language reference](https://www.php.net/manual/en/langref.php) — PHP Group
- [PHP types](https://www.php.net/manual/en/language.types.php) — PHP Group
- [PHP functions](https://www.php.net/manual/en/language.functions.php) — PHP Group
- [PHP extensions](https://www.php.net/manual/en/extensions.php) — PHP Group
