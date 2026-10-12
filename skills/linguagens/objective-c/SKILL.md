---
name: objective-c
description: "Manter e desenvolver código Objective-C para plataformas Apple. Use quando: Manutenção de apps iOS/macOS legados e interoperabilidade com Swift."
---

# Skill: Objective-C

Manter e desenvolver código Objective-C para plataformas Apple.

## Quando usar

Manutenção de apps iOS/macOS legados e interoperabilidade com Swift.

## Conceitos principais

- Mensagens (`[obj metodo]`) e runtime dinâmico
- Classes, categorias e protocolos
- ARC (Automatic Reference Counting)
- Blocks
- Foundation e Cocoa

## Boas práticas

- Use ARC
- Use `weak` para quebrar ciclos de referência (delegates, blocks)
- Adicione nullability annotations para interoperar com Swift
- Prefixe nomes de classes
- Siga os guias Programming with Objective-C da Apple

## Comandos e padrões comuns

```bash
clang -fobjc-arc -framework Foundation main.m -o app
xcodebuild -scheme App build
xcodebuild test -scheme App
```

## Armadilhas comuns

- Ciclos de retenção com blocks capturando `self`
- Mensagens para `nil` retornam zero silenciosamente
- Colisão de nomes em categorias

## Checklist

- [ ] Use ARC
- [ ] Use `weak` para quebrar ciclos de referência (delegates, blocks)
- [ ] Adicione nullability annotations para interoperar com Swift
- [ ] Prefixe nomes de classes
- [ ] Siga os guias Programming with Objective-C da Apple
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/objective-c/`](../../../docs/programacao/linguagens/objective-c/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/objective-c/documentacao-oficial/`](../../../docs/programacao/linguagens/objective-c/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/objective-c/fontes.yml)

## Fontes oficiais

- [Programming with Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html) — Apple
- [Objective-C language reference](https://developer.apple.com/documentation/objectivec/objective-c-runtime) — Apple
- [Objective-C runtime reference](https://developer.apple.com/documentation/objectivec) — Apple
- [Cocoa fundamentals guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaFundamentals/) — Apple
- [Objective-C programming topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Introduction/introObjectiveC.html) — Apple
