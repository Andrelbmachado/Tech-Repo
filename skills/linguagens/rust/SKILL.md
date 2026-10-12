---
name: rust
description: "Programar em Rust seguro e idiomático, com base no Rust Book local. Use quando: Sistemas, CLIs, serviços de rede, WebAssembly e embarcados com segurança de memória."
---

# Skill: Rust

Programar em Rust seguro e idiomático, com base no Rust Book local.

## Quando usar

Sistemas, CLIs, serviços de rede, WebAssembly e embarcados com segurança de memória.

## Conceitos principais

- Ownership, borrowing e lifetimes
- `enum`, `match` e `Option`/`Result`
- Traits e generics
- Módulos, crates e Cargo
- Concorrência segura (`Send`/`Sync`) e `async`

## Boas práticas

- Propague erros com `?` em vez de `unwrap()`
- Rode `cargo clippy` e `cargo fmt`
- Minimize e documente blocos `unsafe`
- Escreva testes unitários e de documentação
- Fixe dependências com `Cargo.lock` em binários

## Comandos e padrões comuns

```bash
cargo new app
cargo build --release
cargo test
cargo clippy -- -D warnings
cargo fmt
cargo doc --open
```

## Armadilhas comuns

- `unwrap()`/`expect()` em código de produção
- Brigar com o borrow checker clonando tudo
- `unsafe` sem invariantes documentadas

## Checklist

- [ ] Propague erros com `?` em vez de `unwrap()`
- [ ] Rode `cargo clippy` e `cargo fmt`
- [ ] Minimize e documente blocos `unsafe`
- [ ] Escreva testes unitários e de documentação
- [ ] Fixe dependências com `Cargo.lock` em binários
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/rust/`](../../../docs/programacao/linguagens/rust/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/rust/documentacao-oficial/`](../../../docs/programacao/linguagens/rust/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/rust/fontes.yml)

## Fontes oficiais

- [The Rust Programming Language](https://doc.rust-lang.org/book/) — Rust project
- [The Rust Reference](https://doc.rust-lang.org/reference/) — Rust project
- [Rust standard library](https://doc.rust-lang.org/std/) — Rust project
- [The Cargo Book](https://doc.rust-lang.org/cargo/) — Rust project
- [The rustc book](https://doc.rust-lang.org/rustc/) — Rust project
