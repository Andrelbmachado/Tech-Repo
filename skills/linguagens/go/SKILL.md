---
name: go
description: "Programar em Go idiomático conforme a especificação e Effective Go. Use quando: Serviços de rede, CLIs, infraestrutura cloud e sistemas concorrentes."
---

# Skill: Go

Programar em Go idiomático conforme a especificação e Effective Go.

## Quando usar

Serviços de rede, CLIs, infraestrutura cloud e sistemas concorrentes.

## Conceitos principais

- Pacotes, módulos (`go.mod`) e visibilidade por inicial maiúscula
- Interfaces implícitas e composição por embedding
- Goroutines, channels e `select`
- Tratamento de erros como valores (`error`, `errors.Is/As`)
- `context.Context` para cancelamento e prazos

## Boas práticas

- Formate com `gofmt` e verifique com `go vet`
- Trate todo `err` retornado; adicione contexto com `fmt.Errorf("...: %w", err)`
- Passe `context.Context` como primeiro parâmetro
- Teste com `go test -race`
- Mantenha interfaces pequenas e definidas pelo consumidor

## Comandos e padrões comuns

```bash
go mod init exemplo.com/app
go build ./...
go test -race ./...
go vet ./...
gofmt -l .
go run .
```

## Armadilhas comuns

- Vazamento de goroutines bloqueadas em channels
- Interface nula vs. interface com valor nulo
- Data races em mapas acessados concorrentemente
- Captura de variável de laço em closures (versões antigas)

## Checklist

- [ ] Formate com `gofmt` e verifique com `go vet`
- [ ] Trate todo `err` retornado; adicione contexto com `fmt.Errorf("...: %w", err)`
- [ ] Passe `context.Context` como primeiro parâmetro
- [ ] Teste com `go test -race`
- [ ] Mantenha interfaces pequenas e definidas pelo consumidor
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/go/`](../../../docs/programacao/linguagens/go/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/go/documentacao-oficial/`](../../../docs/programacao/linguagens/go/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/go/fontes.yml)

## Fontes oficiais

- [The Go Programming Language Specification](https://go.dev/ref/spec) — Go project
- [Effective Go](https://go.dev/doc/effective_go) — Go project
- [Go standard library](https://pkg.go.dev/std) — Go project
- [Go command documentation](https://go.dev/cmd/go/) — Go project
- [Go release history](https://go.dev/doc/devel/release) — Go project
