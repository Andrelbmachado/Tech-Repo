---
name: scala
description: "Desenvolver em Scala 3 na JVM. Use quando: Back-end, processamento de dados (Spark), programação funcional na JVM."
---

# Skill: Scala

Desenvolver em Scala 3 na JVM.

## Quando usar

Back-end, processamento de dados (Spark), programação funcional na JVM.

## Conceitos principais

- Case classes, enums e pattern matching
- Traits e composição
- Givens/using (contextual abstractions)
- Coleções imutáveis
- sbt para build

## Boas práticas

- Prefira imutabilidade e `val`
- Use `Option`/`Either` em vez de `null`/exceções para fluxo
- Configure scalafmt
- Fixe versões no `build.sbt`
- Consulte o Scala 3 Reference para recursos novos

## Comandos e padrões comuns

```bash
sbt new scala/scala3.g8
sbt compile
sbt test
sbt run
scala-cli run Main.scala
```

## Armadilhas comuns

- Implícitos/givens difíceis de rastrear
- Diferenças Scala 2 vs Scala 3
- Tempo de compilação alto

## Checklist

- [ ] Prefira imutabilidade e `val`
- [ ] Use `Option`/`Either` em vez de `null`/exceções para fluxo
- [ ] Configure scalafmt
- [ ] Fixe versões no `build.sbt`
- [ ] Consulte o Scala 3 Reference para recursos novos
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/scala/`](../../../docs/programacao/linguagens/scala/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/scala/documentacao-oficial/`](../../../docs/programacao/linguagens/scala/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/scala/fontes.yml)

## Fontes oficiais

- [Scala 3 documentation](https://docs.scala-lang.org/scala3/) — Scala team
- [Scala 3 language reference](https://docs.scala-lang.org/scala3/reference/) — Scala team
- [Scala 3 API documentation](https://scala-lang.org/api/3.x/) — Scala team
- [Scala 2 documentation](https://docs.scala-lang.org/overviews/) — Scala team
- [sbt documentation](https://www.scala-sbt.org/1.x/docs/) — sbt project
