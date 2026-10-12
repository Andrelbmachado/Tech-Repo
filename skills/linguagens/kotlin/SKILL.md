---
name: kotlin
description: "Desenvolver em Kotlin para JVM, Android e multiplataforma. Use quando: Apps Android, back-end JVM, Kotlin Multiplatform."
---

# Skill: Kotlin

Desenvolver em Kotlin para JVM, Android e multiplataforma.

## Quando usar

Apps Android, back-end JVM, Kotlin Multiplatform.

## Conceitos principais

- Null safety (`?`, `?.`, `?:`)
- Data classes, sealed classes e objetos
- Extension functions e lambdas
- Coroutines e structured concurrency
- Interoperabilidade com Java

## Boas práticas

- Siga as Coding Conventions oficiais
- Prefira `val` a `var`
- Evite `!!`
- Use escopos de coroutine estruturados; evite `GlobalScope`
- Use Gradle Kotlin DSL com versões fixas

## Comandos e padrões comuns

```bash
kotlinc main.kt -include-runtime -d app.jar && java -jar app.jar
./gradlew build
./gradlew test
```

## Armadilhas comuns

- Platform types vindos do Java escondem nulos
- Vazamento de coroutines sem escopo
- Abuso de `!!`

## Checklist

- [ ] Siga as Coding Conventions oficiais
- [ ] Prefira `val` a `var`
- [ ] Evite `!!`
- [ ] Use escopos de coroutine estruturados; evite `GlobalScope`
- [ ] Use Gradle Kotlin DSL com versões fixas
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/kotlin/`](../../../docs/programacao/linguagens/kotlin/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/kotlin/documentacao-oficial/`](../../../docs/programacao/linguagens/kotlin/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/kotlin/fontes.yml)

## Fontes oficiais

- [Kotlin documentation](https://kotlinlang.org/docs/home.html) — JetBrains / Kotlin team
- [Kotlin language specification](https://kotlinlang.org/spec/) — JetBrains / Kotlin team
- [Kotlin API reference](https://kotlinlang.org/docs/api-references.html) — JetBrains / Kotlin team
- [Kotlin coding conventions](https://kotlinlang.org/docs/coding-conventions.html) — JetBrains / Kotlin team
- [Kotlin releases](https://kotlinlang.org/docs/releases.html) — JetBrains / Kotlin team
