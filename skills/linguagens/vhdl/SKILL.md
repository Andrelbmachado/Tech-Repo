---
name: vhdl
description: "Descrever e verificar hardware digital em VHDL. Use quando: Projeto de FPGAs/ASICs, especialmente em indústria aeroespacial e defesa."
---

# Skill: VHDL

Descrever e verificar hardware digital em VHDL.

## Quando usar

Projeto de FPGAs/ASICs, especialmente em indústria aeroespacial e defesa.

## Conceitos principais

- Entity e architecture
- Processos e listas de sensibilidade
- Sinais vs. variáveis
- Tipos fortes (`std_logic`, `numeric_std`)
- Testbenches e simulação

## Boas práticas

- Use `ieee.numeric_std` (não `std_logic_arith`)
- Use processos com clock e reset bem definidos
- Evite latches cobrindo todos os ramos
- Consulte o guia de síntese do fabricante
- Simule antes de sintetizar

## Comandos e padrões comuns

```bash
ghdl -a --std=08 top.vhd tb.vhd
ghdl -e --std=08 tb
ghdl -r --std=08 tb --wave=tb.ghw
```

## Armadilhas comuns

- Lista de sensibilidade incompleta (diferença simulação/síntese)
- Bibliotecas não padronizadas
- Confusão entre atualização de sinal e variável

## Checklist

- [ ] Use `ieee.numeric_std` (não `std_logic_arith`)
- [ ] Use processos com clock e reset bem definidos
- [ ] Evite latches cobrindo todos os ramos
- [ ] Consulte o guia de síntese do fabricante
- [ ] Simule antes de sintetizar
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/vhdl/`](../../../docs/programacao/linguagens/vhdl/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/vhdl/documentacao-oficial/`](../../../docs/programacao/linguagens/vhdl/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/vhdl/fontes.yml)

## Fontes oficiais

- [IEEE 1076 VHDL standard page](https://standards.ieee.org/ieee/1076/6841/) — IEEE Standards Association
- [Accellera standards and resources](https://www.accellera.org/downloads/standards) — Accellera Systems Initiative
- [Vivado Design Suite documentation](https://docs.amd.com/r/en-US/ug901-vivado-synthesis) — AMD
- [Quartus Prime documentation](https://www.intel.com/content/www/us/en/docs/programmable/683236/current/overview.html) — Intel
- [VHDL Language Reference Manual page](https://standards.ieee.org/standard/1076-2019.html) — IEEE Standards Association
