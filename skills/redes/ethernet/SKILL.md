---
name: ethernet
description: "Projetar e diagnosticar redes Ethernet (IEEE 802.3). Use quando: LAN cabeada, switches, cabeamento e camada de enlace."
---

# Skill: Ethernet

Projetar e diagnosticar redes Ethernet (IEEE 802.3).

## Quando usar

LAN cabeada, switches, cabeamento e camada de enlace.

## Conceitos principais

- Quadro Ethernet e endereços MAC
- Switches, tabela MAC e domínios de colisão/broadcast
- Velocidades e meios físicos (cobre, fibra)
- Autonegociação e duplex
- Spanning Tree contra loops

## Boas práticas

- Use cabeamento certificado para a velocidade
- Ative STP/RSTP em redes com redundância
- Verifique duplex e velocidade nas duas pontas
- Monitore erros de interface (CRC)
- Documente portas e patch panels

## Comandos e padrões comuns

```bash
ip link
ethtool eth0
ip -s link show eth0
```

## Armadilhas comuns

- Duplex mismatch
- Loops de camada 2
- Cabos fora da categoria

## Checklist

- [ ] Use cabeamento certificado para a velocidade
- [ ] Ative STP/RSTP em redes com redundância
- [ ] Verifique duplex e velocidade nas duas pontas
- [ ] Monitore erros de interface (CRC)
- [ ] Documente portas e patch panels
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/ethernet/`](../../../docs/redes-e-wifi/ethernet/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/ethernet/documentacao-oficial/`](../../../docs/redes-e-wifi/ethernet/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/ethernet/fontes.yml)

## Fontes oficiais

- Nenhuma fonte primária cadastrada ainda em `fontes.yml`; consulte a ficha da tecnologia e complete a curadoria antes de tratar esta skill como referência revisada.
