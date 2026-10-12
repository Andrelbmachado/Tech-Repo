---
name: c-sharp
description: "Desenvolver aplicações .NET em C# moderno. Use quando: APIs web (ASP.NET Core), apps desktop, jogos (Unity), serviços e bibliotecas .NET."
---

# Skill: C#

Desenvolver aplicações .NET em C# moderno.

## Quando usar

APIs web (ASP.NET Core), apps desktop, jogos (Unity), serviços e bibliotecas .NET.

## Conceitos principais

- Tipos de valor vs. referência, `struct`, `record`, `class`
- Nullable reference types (`string?`)
- LINQ e expressões lambda
- `async`/`await` e `Task`
- Pattern matching e `switch` expressions

## Boas práticas

- Ative `<Nullable>enable</Nullable>` no projeto
- Use `async` de ponta a ponta; evite `.Result`/`.Wait()`
- Use `using`/`await using` para `IDisposable`
- Siga as convenções de nomenclatura .NET (PascalCase para membros públicos)
- Trate avisos do compilador e analisadores como erros no CI

## Comandos e padrões comuns

```bash
dotnet new console -n App
dotnet build
dotnet test
dotnet run --project App
dotnet format
```

## Armadilhas comuns

- Deadlocks ao bloquear código assíncrono
- Múltipla enumeração de `IEnumerable` com LINQ adiado
- Boxing acidental de structs
- Capturar exceções genéricas e ocultar erros

## Checklist

- [ ] Ative `<Nullable>enable</Nullable>` no projeto
- [ ] Use `async` de ponta a ponta; evite `.Result`/`.Wait()`
- [ ] Use `using`/`await using` para `IDisposable`
- [ ] Siga as convenções de nomenclatura .NET (PascalCase para membros públicos)
- [ ] Trate avisos do compilador e analisadores como erros no CI
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/c-sharp/`](../../../docs/programacao/linguagens/c-sharp/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/c-sharp/documentacao-oficial/`](../../../docs/programacao/linguagens/c-sharp/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/c-sharp/fontes.yml)

## Fontes oficiais

- [C# documentation](https://learn.microsoft.com/en-us/dotnet/csharp/) — Microsoft
- [C# language reference](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/) — Microsoft
- [C# fundamentals](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/) — Microsoft
- [C# language version history](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-version-history) — Microsoft
- [C# compiler options](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/) — Microsoft
