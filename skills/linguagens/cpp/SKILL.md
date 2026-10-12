---
name: cpp
description: "Programar em C++ moderno (C++17/20/23) com segurança de recursos. Use quando: Software de alto desempenho, jogos, sistemas embarcados, motores e bibliotecas."
---

# Skill: C++

Programar em C++ moderno (C++17/20/23) com segurança de recursos.

## Quando usar

Software de alto desempenho, jogos, sistemas embarcados, motores e bibliotecas.

## Conceitos principais

- RAII e tempo de vida de objetos
- Smart pointers (`std::unique_ptr`, `std::shared_ptr`)
- Semântica de movimento e regra de 0/3/5
- Templates, `constexpr` e concepts (C++20)
- STL: containers, algoritmos e iteradores

## Boas práticas

- Prefira RAII e smart pointers a `new`/`delete` manuais
- Compile com `-std=c++20 -Wall -Wextra` e sanitizers
- Prefira algoritmos da STL a laços manuais
- Use `const` e referências para evitar cópias
- Use um sistema de build (CMake) e testes automatizados

## Comandos e padrões comuns

```bash
g++ -std=c++20 -Wall -Wextra -O2 -g main.cpp -o app
clang++ -std=c++20 -fsanitize=address,undefined main.cpp -o app
cmake -S . -B build && cmake --build build && ctest --test-dir build
```

## Armadilhas comuns

- Iteradores invalidados após modificar containers
- Referências pendentes (dangling) a temporários
- Comportamento indefinido herdado de C
- Ciclos de `shared_ptr` causando vazamentos

## Checklist

- [ ] Prefira RAII e smart pointers a `new`/`delete` manuais
- [ ] Compile com `-std=c++20 -Wall -Wextra` e sanitizers
- [ ] Prefira algoritmos da STL a laços manuais
- [ ] Use `const` e referências para evitar cópias
- [ ] Use um sistema de build (CMake) e testes automatizados
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/cpp/`](../../../docs/programacao/linguagens/cpp/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/cpp/documentacao-oficial/`](../../../docs/programacao/linguagens/cpp/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/cpp/fontes.yml)

## Fontes oficiais

- [C++ Standards](https://isocpp.org/std) — ISO C++
- [WG21 papers and drafts](https://www.open-std.org/jtc1/sc22/wg21/) — ISO/IEC JTC 1/SC 22/WG 21
- [GCC C++ documentation](https://gcc.gnu.org/onlinedocs/libstdc++/) — GNU Project
- [Clang documentation](https://clang.llvm.org/docs/) — LLVM Project
- [C++ language reference](https://learn.microsoft.com/en-us/cpp/cpp/cpp-language-reference) — Microsoft
- [C++ language reference](https://en.cppreference.com/w/cpp/language) — cppreference.com
