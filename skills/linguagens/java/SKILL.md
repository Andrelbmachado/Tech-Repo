---
name: java
description: "Desenvolver em Java SE moderno (LTS) com a JDK. Use quando: Aplicações corporativas, back-end, Android (legado), sistemas distribuídos."
---

# Skill: Java

Desenvolver em Java SE moderno (LTS) com a JDK.

## Quando usar

Aplicações corporativas, back-end, Android (legado), sistemas distribuídos.

## Conceitos principais

- Classes, interfaces, records e sealed classes
- Generics e coleções (`java.util`)
- Streams e lambdas
- Concorrência (`java.util.concurrent`, virtual threads)
- Módulos (JPMS) e classpath

## Boas práticas

- Use a versão LTS mais recente suportada pelo projeto
- Use Maven ou Gradle com versões fixas
- Prefira imutabilidade (records, `final`)
- Use try-with-resources para recursos
- Escreva testes com JUnit e rode no CI

## Comandos e padrões comuns

```bash
javac -d out src/Main.java && java -cp out Main
java Main.java   # execução direta de arquivo único
mvn -q verify
./gradlew test
jshell
```

## Armadilhas comuns

- `NullPointerException` por falta de validação
- Comparar strings com `==`
- Quebrar `equals`/`hashCode`
- Bloquear threads da plataforma em I/O excessivo

## Checklist

- [ ] Use a versão LTS mais recente suportada pelo projeto
- [ ] Use Maven ou Gradle com versões fixas
- [ ] Prefira imutabilidade (records, `final`)
- [ ] Use try-with-resources para recursos
- [ ] Escreva testes com JUnit e rode no CI
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/java/`](../../../docs/programacao/linguagens/java/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/java/documentacao-oficial/`](../../../docs/programacao/linguagens/java/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/java/fontes.yml)

## Fontes oficiais

- [Java Documentation](https://docs.oracle.com/en/java/) — Oracle
- [Java Language Specification](https://docs.oracle.com/javase/specs/) — Oracle
- [Java SE API Specification](https://docs.oracle.com/en/java/javase/26/docs/api/) — Oracle
- [Dev.java learning resources](https://dev.java/learn/) — Oracle
- [OpenJDK documentation](https://openjdk.org/) — OpenJDK
