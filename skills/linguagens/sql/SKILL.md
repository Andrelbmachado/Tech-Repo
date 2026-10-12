---
name: sql
description: "Escrever e otimizar consultas SQL e esquemas relacionais. Use quando: Consultas, modelagem e manutenção em PostgreSQL, MySQL, SQL Server, SQLite."
---

# Skill: SQL

Escrever e otimizar consultas SQL e esquemas relacionais.

## Quando usar

Consultas, modelagem e manutenção em PostgreSQL, MySQL, SQL Server, SQLite.

## Conceitos principais

- DDL, DML, DCL e transações
- JOINs, agregações, `GROUP BY`, `HAVING`
- Subconsultas, CTEs e window functions
- Índices e planos de execução
- Constraints e normalização

## Boas práticas

- Use consultas parametrizadas (nunca concatene entrada)
- Analise planos com `EXPLAIN`
- Declare chaves primárias, estrangeiras e constraints
- Use transações para operações compostas
- Confirme o dialeto (diferenças entre SGBDs)

## Comandos e padrões comuns

```sql
BEGIN;
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;
EXPLAIN SELECT * FROM pedidos WHERE cliente_id = 42;
WITH t AS (SELECT cliente_id, SUM(valor) AS total FROM pedidos GROUP BY cliente_id)
SELECT * FROM t WHERE total > 1000;
```

## Armadilhas comuns

- SQL injection
- `NULL` em comparações (`= NULL` é sempre desconhecido)
- `SELECT *` em produção
- Dialetos divergentes do padrão ISO

## Checklist

- [ ] Use consultas parametrizadas (nunca concatene entrada)
- [ ] Analise planos com `EXPLAIN`
- [ ] Declare chaves primárias, estrangeiras e constraints
- [ ] Use transações para operações compostas
- [ ] Confirme o dialeto (diferenças entre SGBDs)
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/sql/`](../../../docs/programacao/linguagens/sql/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/sql/documentacao-oficial/`](../../../docs/programacao/linguagens/sql/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/sql/fontes.yml)

## Fontes oficiais

- [SQL standard catalog entry](https://www.iso.org/standard/76583.html) — ISO
- [PostgreSQL SQL documentation](https://www.postgresql.org/docs/current/sql.html) — PostgreSQL Global Development Group
- [MySQL Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/) — Oracle / MySQL
- [Transact-SQL reference](https://learn.microsoft.com/en-us/sql/t-sql/language-reference) — Microsoft
- [SQLite SQL language](https://www.sqlite.org/lang.html) — SQLite project
