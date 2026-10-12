---
name: swift
description: "Desenvolver em Swift para plataformas Apple e servidor. Use quando: Apps iOS/macOS/watchOS, Swift no servidor e ferramentas."
---

# Skill: Swift

Desenvolver em Swift para plataformas Apple e servidor.

## Quando usar

Apps iOS/macOS/watchOS, Swift no servidor e ferramentas.

## Conceitos principais

- Optionals e `if let`/`guard let`
- Value types (`struct`, `enum`) vs. `class`
- Protocolos e generics
- Concorrência: `async`/`await`, actors, `Sendable`
- Swift Package Manager

## Boas práticas

- Siga as API Design Guidelines
- Prefira `struct` e `let`
- Evite force unwrap (`!`)
- Use `[weak self]` em closures que podem reter ciclos
- Teste com XCTest/Swift Testing

## Comandos e padrões comuns

```bash
swift package init --type executable
swift build
swift test
swift run
```

## Armadilhas comuns

- Force unwrap de `nil`
- Ciclos de retenção em closures
- Data races sem checagem de concorrência estrita

## Checklist

- [ ] Siga as API Design Guidelines
- [ ] Prefira `struct` e `let`
- [ ] Evite force unwrap (`!`)
- [ ] Use `[weak self]` em closures que podem reter ciclos
- [ ] Teste com XCTest/Swift Testing
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/swift/`](../../../docs/programacao/linguagens/swift/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/swift/documentacao-oficial/`](../../../docs/programacao/linguagens/swift/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/swift/fontes.yml)

## Fontes oficiais

- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/) — Apple / Swift project
- [Swift language reference](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/aboutthelanguagereference/) — Apple / Swift project
- [Swift standard library](https://developer.apple.com/documentation/swift) — Apple / Swift project
- [Swift Package Manager](https://docs.swift.org/main/documentation/packagemanagerdocs/) — Apple / Swift project
- [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/) — Apple / Swift project
