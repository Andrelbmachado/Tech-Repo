---
name: solidity
description: "Escrever e revisar contratos inteligentes em Solidity com foco em segurança. Use quando: Contratos inteligentes em blockchains compatíveis com EVM."
---

# Skill: Solidity

Escrever e revisar contratos inteligentes em Solidity com foco em segurança.

## Quando usar

Contratos inteligentes em blockchains compatíveis com EVM.

## Conceitos principais

- Contratos, estado, funções e visibilidade
- Tipos de valor/referência e localização de dados (`storage`, `memory`, `calldata`)
- Eventos, modificadores e erros customizados
- Herança e interfaces
- Gas e custo de execução

## Boas práticas

- Fixe a versão do compilador (`pragma solidity 0.8.x;`)
- Siga o padrão checks-effects-interactions
- Leia as Security Considerations oficiais
- Teste extensivamente e audite antes do deploy
- Use bibliotecas auditadas em vez de reimplementar

## Comandos e padrões comuns

```bash
solc --version
solc --optimize --bin --abi Contrato.sol -o build/
```

## Armadilhas comuns

- Reentrância
- Uso de `tx.origin` para autorização
- Laços sem limite consumindo gas
- Contratos implantados são imutáveis

## Checklist

- [ ] Fixe a versão do compilador (`pragma solidity 0.8.x;`)
- [ ] Siga o padrão checks-effects-interactions
- [ ] Leia as Security Considerations oficiais
- [ ] Teste extensivamente e audite antes do deploy
- [ ] Use bibliotecas auditadas em vez de reimplementar
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/solidity/`](../../../docs/programacao/linguagens/solidity/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/solidity/documentacao-oficial/`](../../../docs/programacao/linguagens/solidity/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/solidity/fontes.yml)

## Fontes oficiais

- [Solidity documentation](https://docs.soliditylang.org/en/latest/) — Solidity team
- [Solidity language specification](https://docs.soliditylang.org/en/latest/grammar.html) — Solidity team
- [Solidity types](https://docs.soliditylang.org/en/latest/types.html) — Solidity team
- [Solidity security considerations](https://docs.soliditylang.org/en/latest/security-considerations.html) — Solidity team
- [Solidity compiler documentation](https://docs.soliditylang.org/en/latest/using-the-compiler.html) — Solidity team
