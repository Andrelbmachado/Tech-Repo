---
name: vlan
description: "Segmentar redes com VLANs (IEEE 802.1Q). Use quando: Segmentação de LAN, trunks e isolamento de tráfego."
---

# Skill: VLAN

Segmentar redes com VLANs (IEEE 802.1Q).

## Quando usar

Segmentação de LAN, trunks e isolamento de tráfego.

## Conceitos principais

- Tag 802.1Q e VLAN ID
- Portas access vs. trunk
- VLAN nativa
- Roteamento entre VLANs
- Domínios de broadcast

## Boas práticas

- Não use a VLAN 1 para dados
- Restrinja VLANs permitidas em trunks
- Altere a VLAN nativa para uma não utilizada
- Documente o plano de VLANs
- Desative portas não usadas

## Comandos e padrões comuns

```bash
sudo ip link add link eth0 name eth0.10 type vlan id 10
ip -d link show eth0.10
```

## Armadilhas comuns

- VLAN hopping via VLAN nativa
- Trunks permitindo todas as VLANs
- VLAN nativa divergente entre pontas

## Checklist

- [ ] Não use a VLAN 1 para dados
- [ ] Restrinja VLANs permitidas em trunks
- [ ] Altere a VLAN nativa para uma não utilizada
- [ ] Documente o plano de VLANs
- [ ] Desative portas não usadas
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/vlan/`](../../../docs/redes-e-wifi/vlan/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/vlan/documentacao-oficial/`](../../../docs/redes-e-wifi/vlan/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/vlan/fontes.yml)

## Fontes oficiais

- Nenhuma fonte primária cadastrada ainda em `fontes.yml`; consulte a ficha da tecnologia e complete a curadoria antes de tratar esta skill como referência revisada.
