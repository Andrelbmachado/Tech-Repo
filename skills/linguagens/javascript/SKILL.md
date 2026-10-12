---
name: javascript
description: "Programar em JavaScript (ECMAScript) para navegador e Node.js. Use quando: Front-end web, back-end com Node.js, scripts e ferramentas."
---

# Skill: JavaScript

Programar em JavaScript (ECMAScript) para navegador e Node.js.

## Quando usar

Front-end web, back-end com Node.js, scripts e ferramentas.

## Conceitos principais

- Escopo de bloco (`let`/`const`) e closures
- Protótipos e classes
- Event loop, Promises e `async`/`await`
- Módulos ES (`import`/`export`)
- Coerção de tipos e igualdade estrita

## Boas práticas

- Use `===` e `!==`
- Prefira `const`; use `let` quando necessário; evite `var`
- Trate rejeições de Promise (`try/catch` com `await`)
- Use um linter (ESLint) e formatador
- Consulte a especificação ECMA-262 e o MDN para comportamento exato

## Comandos e padrões comuns

```bash
node app.js
node --test
npm init -y
npm install
npm run build
node --inspect app.js
```

## Armadilhas comuns

- `this` dependente do modo de chamada
- Coerção implícita (`[] + {}`)
- Promises não tratadas
- Aritmética de ponto flutuante (`0.1 + 0.2`)

## Checklist

- [ ] Use `===` e `!==`
- [ ] Prefira `const`; use `let` quando necessário; evite `var`
- [ ] Trate rejeições de Promise (`try/catch` com `await`)
- [ ] Use um linter (ESLint) e formatador
- [ ] Consulte a especificação ECMA-262 e o MDN para comportamento exato
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/javascript/`](../../../docs/programacao/linguagens/javascript/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/javascript/documentacao-oficial/`](../../../docs/programacao/linguagens/javascript/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/javascript/fontes.yml)

## Fontes oficiais

- [ECMAScript specification](https://tc39.es/ecma262/) — Ecma International / TC39
- [ECMAScript specification source](https://github.com/tc39/ecma262) — Ecma International / TC39
- [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — MDN / Mozilla
- [Node.js documentation](https://nodejs.org/docs/latest/api/) — OpenJS Foundation
- [V8 documentation](https://v8.dev/docs) — Google / V8 team
- [JavaScript on Chrome for Developers](https://developer.chrome.com/docs/devtools/) — Google
