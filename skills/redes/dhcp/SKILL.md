---
name: dhcp
description: "Configurar e diagnosticar DHCP (RFC 2131) e DHCPv6 (RFC 8415). Use quando: Atribuição automática de endereços e parâmetros de rede."
---

# Skill: DHCP

Configurar e diagnosticar DHCP (RFC 2131) e DHCPv6 (RFC 8415).

## Quando usar

Atribuição automática de endereços e parâmetros de rede.

## Conceitos principais

- Fluxo DORA: Discover, Offer, Request, Ack
- Leases e renovação
- Opções DHCP (RFC 2132)
- Relay agent e opção 82 (RFC 3046)
- DHCPv6 e alternativas (SLAAC)

## Boas práticas

- Reserve endereços para servidores/infraestrutura
- Use relay entre sub-redes
- Proteja com DHCP snooping no switch
- Dimensione o pool e o tempo de lease
- Monitore esgotamento de pool

## Comandos e padrões comuns

```bash
sudo dhclient -v eth0
sudo tcpdump -i eth0 port 67 or port 68
```

## Armadilhas comuns

- Servidores DHCP não autorizados
- Pool esgotado
- Conflito com IPs estáticos

## Checklist

- [ ] Reserve endereços para servidores/infraestrutura
- [ ] Use relay entre sub-redes
- [ ] Proteja com DHCP snooping no switch
- [ ] Dimensione o pool e o tempo de lease
- [ ] Monitore esgotamento de pool
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/dhcp/`](../../../docs/redes-e-wifi/dhcp/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/dhcp/documentacao-oficial/`](../../../docs/redes-e-wifi/dhcp/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/dhcp/fontes.yml)

## Fontes oficiais

- [Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131) — IETF / RFC Editor
- [DHCP Options and BOOTP Vendor Extensions](https://www.rfc-editor.org/rfc/rfc2132) — IETF / RFC Editor
- [Dynamic Host Configuration Protocol for IPv6](https://www.rfc-editor.org/rfc/rfc8415) — IETF / RFC Editor
- [DHCP Relay Agent Information Option](https://www.rfc-editor.org/rfc/rfc3046) — IETF / RFC Editor
- [DHCP Failover Protocol](https://www.rfc-editor.org/rfc/rfc8156) — IETF / RFC Editor
