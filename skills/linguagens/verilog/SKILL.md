---
name: verilog
description: "Descrever e verificar hardware digital em Verilog/SystemVerilog. Use quando: Projeto de FPGAs e ASICs, simulação e síntese lógica."
---

# Skill: Verilog / SystemVerilog

Descrever e verificar hardware digital em Verilog/SystemVerilog.

## Quando usar

Projeto de FPGAs e ASICs, simulação e síntese lógica.

## Conceitos principais

- Módulos, portas e hierarquia
- Lógica combinacional (`always @*`/`always_comb`) vs. sequencial (`always_ff`)
- Atribuições bloqueantes (`=`) vs. não bloqueantes (`<=`)
- Testbenches e simulação
- Restrições de síntese e timing

## Boas práticas

- Use `<=` em lógica sequencial e `=` em combinacional
- Evite latches inferidos (cubra todos os casos)
- Sincronize sinais entre domínios de clock
- Consulte o guia de síntese do fabricante (Vivado/Quartus)
- Escreva testbenches auto-verificáveis

## Comandos e padrões comuns

```bash
iverilog -g2012 -o sim top.sv tb.sv && vvp sim
verilator --lint-only top.sv
```

## Armadilhas comuns

- Latches inferidos
- Construções não sintetizáveis em código de RTL
- Metaestabilidade em cruzamento de domínios de clock

## Checklist

- [ ] Use `<=` em lógica sequencial e `=` em combinacional
- [ ] Evite latches inferidos (cubra todos os casos)
- [ ] Sincronize sinais entre domínios de clock
- [ ] Consulte o guia de síntese do fabricante (Vivado/Quartus)
- [ ] Escreva testbenches auto-verificáveis
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/verilog/`](../../../docs/programacao/linguagens/verilog/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/verilog/documentacao-oficial/`](../../../docs/programacao/linguagens/verilog/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/verilog/fontes.yml)

## Fontes oficiais

- [IEEE 1800 SystemVerilog standard page](https://standards.ieee.org/ieee/1800/7743/) — IEEE Standards Association
- [Accellera standards and resources](https://www.accellera.org/downloads/standards) — Accellera Systems Initiative
- [Vivado Design Suite documentation](https://docs.amd.com/r/en-US/ug901-vivado-synthesis) — AMD
- [Quartus Prime documentation](https://www.intel.com/content/www/us/en/docs/programmable/683236/current/overview.html) — Intel
- [Verilog language reference](https://standards.ieee.org/standard/1364-2005.html) — IEEE Standards Association
