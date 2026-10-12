---
name: python
description: "Programar em Python 3 idiomático, com base na documentação oficial local (3.15). Use quando: Automação, ciência de dados, back-end, scripts, IA e ensino."
---

# Skill: Python

Programar em Python 3 idiomático, com base na documentação oficial local (3.15).

## Quando usar

Automação, ciência de dados, back-end, scripts, IA e ensino.

## Conceitos principais

- Tipos embutidos, mutabilidade e modelo de dados
- Funções, closures, decorators e geradores
- Classes e protocolos (dunder methods)
- Exceções e gerenciadores de contexto (`with`)
- Módulos, pacotes, `venv` e empacotamento

## Boas práticas

- Siga a PEP 8 e use type hints
- Use ambientes virtuais (`python -m venv`)
- Use `with` para arquivos e recursos
- Escreva testes (`unittest`/pytest)
- Prefira a biblioteca padrão antes de adicionar dependências

## Comandos e padrões comuns

```bash
python -m venv .venv && . .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest
python -m pdb script.py
python -m py_compile script.py
```

## Armadilhas comuns

- Argumentos padrão mutáveis (`def f(x=[])`)
- Capturar `Exception` genérica e silenciar
- Instalar pacotes no Python do sistema
- Comparar floats com `==`

## Checklist

- [ ] Siga a PEP 8 e use type hints
- [ ] Use ambientes virtuais (`python -m venv`)
- [ ] Use `with` para arquivos e recursos
- [ ] Escreva testes (`unittest`/pytest)
- [ ] Prefira a biblioteca padrão antes de adicionar dependências
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/python/`](../../../docs/programacao/linguagens/python/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/python/documentacao-oficial/`](../../../docs/programacao/linguagens/python/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/python/fontes.yml)

## Fontes oficiais

- [Python 3 Documentation](https://docs.python.org/3/) — Python Software Foundation
- [The Python Tutorial](https://docs.python.org/3/tutorial/) — Python Software Foundation
- [Python Standard Library](https://docs.python.org/3/library/) — Python Software Foundation
- [Python Language Reference](https://docs.python.org/3/reference/) — Python Software Foundation
- [Python Packaging User Guide](https://packaging.python.org/) — Python Packaging Authority
- [Python 3.15 documentation — plain text archive](https://docs.python.org/3.15/download.html) — Python Software Foundation
