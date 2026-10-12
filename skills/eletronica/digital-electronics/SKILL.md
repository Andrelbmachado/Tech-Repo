---
name: digital-electronics
description: "Projetar e analisar circuitos lógicos digitais. Use quando: Lógica combinacional e sequencial, interfaces entre CIs e FPGAs."
---

# Skill: Eletrônica digital

Projetar e analisar circuitos lógicos digitais.

## Quando usar

Lógica combinacional e sequencial, interfaces entre CIs e FPGAs.

## Conceitos principais

- Álgebra booleana e portas lógicas
- Flip-flops, registradores e máquinas de estado
- Níveis lógicos e famílias (TTL, CMOS)
- Clock, setup/hold e metaestabilidade
- Conversão AD/DA

## Boas práticas

- Respeite níveis lógicos ao interligar tensões diferentes
- Use resistores de pull-up/pull-down em entradas
- Sincronize sinais assíncronos
- Faça debounce em chaves
- Consulte tempos de setup/hold no datasheet

## Armadilhas comuns

- Entradas CMOS flutuando
- Mistura de 5 V e 3,3 V sem conversão
- Glitches em lógica combinacional

## Checklist

- [ ] Respeite níveis lógicos ao interligar tensões diferentes
- [ ] Use resistores de pull-up/pull-down em entradas
- [ ] Sincronize sinais assíncronos
- [ ] Faça debounce em chaves
- [ ] Consulte tempos de setup/hold no datasheet
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/eletronica/digital-electronics/`](../../../docs/eletronica/digital-electronics/README.md)
- Documentação oficial (cópia local ou links): [`docs/eletronica/digital-electronics/documentacao-oficial/`](../../../docs/eletronica/digital-electronics/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/eletronica/digital-electronics/fontes.yml)

## Fontes oficiais

- Nenhuma fonte primária cadastrada ainda em `fontes.yml`; consulte a ficha da tecnologia e complete a curadoria antes de tratar esta skill como referência revisada.
