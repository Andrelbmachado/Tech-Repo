---
name: dart
description: "Desenvolver em Dart, incluindo apps Flutter e CLIs. Use quando: Apps multiplataforma com Flutter, ferramentas de linha de comando e servidores Dart."
---

# Skill: Dart

Desenvolver em Dart, incluindo apps Flutter e CLIs.

## Quando usar

Apps multiplataforma com Flutter, ferramentas de linha de comando e servidores Dart.

## Conceitos principais

- Null safety sólida (`?`, `!`, `late`)
- Classes, mixins e extension methods
- `Future`, `Stream`, `async`/`await`
- Pacotes via pub (`pubspec.yaml`)
- Records e pattern matching (Dart 3)

## Boas práticas

- Siga o guia Effective Dart
- Rode `dart analyze` e `dart format` no CI
- Evite `!` sem necessidade; modele nulidade corretamente
- Prefira `final` para variáveis não reatribuídas
- Fixe versões de dependências com `pubspec.lock` em apps

## Comandos e padrões comuns

```bash
dart create app
dart pub get
dart analyze
dart format .
dart test
dart run
```

## Armadilhas comuns

- Esquecer `await` em `Future`
- Uso excessivo do operador `!`
- Bloquear o isolate principal com trabalho pesado

## Checklist

- [ ] Siga o guia Effective Dart
- [ ] Rode `dart analyze` e `dart format` no CI
- [ ] Evite `!` sem necessidade; modele nulidade corretamente
- [ ] Prefira `final` para variáveis não reatribuídas
- [ ] Fixe versões de dependências com `pubspec.lock` em apps
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/dart/`](../../../docs/programacao/linguagens/dart/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/dart/documentacao-oficial/`](../../../docs/programacao/linguagens/dart/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/dart/fontes.yml)

## Fontes oficiais

- [Dart language documentation](https://dart.dev/language) — Dart team
- [Dart language specification](https://dart.dev/resources/language/spec) — Dart team
- [Dart core libraries](https://api.dart.dev/) — Dart team
- [Dart packages and pub](https://dart.dev/tools/pub) — Dart team
- [Effective Dart](https://dart.dev/effective-dart) — Dart team
