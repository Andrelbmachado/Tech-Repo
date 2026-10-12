---
name: ipv4
description: "Endereçar e diagnosticar redes IPv4 (RFC 791). Use quando: Planejamento de sub-redes, roteamento e troubleshooting."
---

# Skill: IPv4

Endereçar e diagnosticar redes IPv4 (RFC 791).

## Quando usar

Planejamento de sub-redes, roteamento e troubleshooting.

## Conceitos principais

- Cabeçalho IPv4, TTL e fragmentação
- CIDR e máscaras (RFC 4632)
- ARP (RFC 826)
- Endereços privados (RFC 1918)
- NAT

## Boas práticas

- Planeje sub-redes com CIDR e documente
- Use faixas RFC 1918 internamente
- Evite sobreposição de faixas entre sites/VPNs
- Verifique MTU e fragmentação
- Use `ping`/`traceroute` para isolar falhas

## Comandos e padrões comuns

```bash
ip -4 addr
ip route get 8.8.8.8
ping -c 4 192.0.2.1
arp -n
```

## Armadilhas comuns

- Sobreposição de redes privadas
- Máscara incorreta
- Problemas de MTU bloqueando ICMP

## Checklist

- [ ] Planeje sub-redes com CIDR e documente
- [ ] Use faixas RFC 1918 internamente
- [ ] Evite sobreposição de faixas entre sites/VPNs
- [ ] Verifique MTU e fragmentação
- [ ] Use `ping`/`traceroute` para isolar falhas
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/ipv4/`](../../../docs/redes-e-wifi/ipv4/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/ipv4/documentacao-oficial/`](../../../docs/redes-e-wifi/ipv4/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/ipv4/fontes.yml)

## Fontes oficiais

- [Internet Protocol](https://www.rfc-editor.org/rfc/rfc791) — IETF / RFC Editor
- [Requirements for Internet Gateways](https://www.rfc-editor.org/rfc/rfc1009) — IETF / RFC Editor
- [Classless Inter-domain Routing](https://www.rfc-editor.org/rfc/rfc4632) — IETF / RFC Editor
- [Address Resolution Protocol](https://www.rfc-editor.org/rfc/rfc826) — IETF / RFC Editor
- [IPv4 Addressing Guidelines](https://www.rfc-editor.org/rfc/rfc1918) — IETF / RFC Editor
