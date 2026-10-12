---
name: c
description: "Programar, revisar e depurar código em C padrão ISO (C11/C17/C23). Use quando: Sistemas, firmware, drivers, bibliotecas de baixo nível e código com requisitos de desempenho e memória."
---

# Skill: C

Programar, revisar e depurar código em C padrão ISO (C11/C17/C23).

## Quando usar

Sistemas, firmware, drivers, bibliotecas de baixo nível e código com requisitos de desempenho e memória.

## Conceitos principais

- Tipos, ponteiros, arrays e aritmética de ponteiros
- Gerenciamento manual de memória (`malloc`/`free`)
- Unidades de tradução, headers, pré-processador e linkagem
- Comportamento indefinido (UB) e comportamento definido pela implementação
- Biblioteca padrão (`stdio.h`, `string.h`, `stdlib.h`)

## Boas práticas

- Compile com avisos altos: `-Wall -Wextra -Wpedantic` e o padrão explícito (`-std=c17`)
- Use sanitizers (`-fsanitize=address,undefined`) em testes
- Verifique todo retorno de `malloc`, `fopen` etc.
- Prefira funções com limite (`snprintf`, `strncpy` com cuidado)
- Documente posse (quem libera) de cada ponteiro

## Comandos e padrões comuns

```bash
gcc -std=c17 -Wall -Wextra -Wpedantic -O2 -g main.c -o app
clang -fsanitize=address,undefined -g main.c -o app && ./app
gdb ./app
valgrind --leak-check=full ./app
```

## Armadilhas comuns

- Buffer overflow e acesso fora dos limites
- Uso após `free` e double free
- Overflow de inteiro com sinal é UB
- Esquecer o terminador `\0` em strings

## Checklist

- [ ] Compile com avisos altos: `-Wall -Wextra -Wpedantic` e o padrão explícito (`-std=c17`)
- [ ] Use sanitizers (`-fsanitize=address,undefined`) em testes
- [ ] Verifique todo retorno de `malloc`, `fopen` etc.
- [ ] Prefira funções com limite (`snprintf`, `strncpy` com cuidado)
- [ ] Documente posse (quem libera) de cada ponteiro
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/c/`](../../../docs/programacao/linguagens/c/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/c/documentacao-oficial/`](../../../docs/programacao/linguagens/c/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/c/fontes.yml)

## Fontes oficiais

- [WG14 C language documents](https://www.open-std.org/jtc1/sc22/wg14/) — ISO/IEC JTC 1/SC 22/WG 14
- [GCC C implementation documentation](https://gcc.gnu.org/onlinedocs/) — GNU Project
- [Clang documentation](https://clang.llvm.org/docs/) — LLVM Project
- [C language reference](https://learn.microsoft.com/en-us/cpp/c-language/) — Microsoft
- [GNU C Language Manual](https://www.gnu.org/software/c-intro-and-ref/manual/) — GNU Project
- [C reference](https://en.cppreference.com/w/c) — cppreference.com
