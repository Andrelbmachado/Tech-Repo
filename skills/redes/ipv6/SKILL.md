---
name: ipv6
description: "Endereçar e operar redes IPv6 (RFC 8200). Use quando: Implantação de IPv6, dual-stack e troubleshooting."
---

# Skill: IPv6

Endereçar e operar redes IPv6 (RFC 8200).

## Quando usar

Implantação de IPv6, dual-stack e troubleshooting.

## Conceitos principais

- Endereços de 128 bits e tipos (RFC 4291)
- Neighbor Discovery (RFC 4861)
- SLAAC (RFC 4862) e DHCPv6
- ICMPv6 (RFC 4443) é essencial
- Extension headers

## Boas práticas

- Não bloqueie ICMPv6 indiscriminadamente
- Use /64 por sub-rede
- Aplique firewall equivalente ao IPv4
- Planeje com prefixo delegado
- Teste dual-stack nas aplicações

## Comandos e padrões comuns

```bash
ip -6 addr
ip -6 route
ping -6 2001:db8::1
ip -6 neigh
```

## Armadilhas comuns

- Bloquear ICMPv6 quebra PMTUD e ND
- Esquecer regras de firewall IPv6
- Supor NAT como segurança

## Checklist

- [ ] Não bloqueie ICMPv6 indiscriminadamente
- [ ] Use /64 por sub-rede
- [ ] Aplique firewall equivalente ao IPv4
- [ ] Planeje com prefixo delegado
- [ ] Teste dual-stack nas aplicações
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/ipv6/`](../../../docs/redes-e-wifi/ipv6/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/ipv6/documentacao-oficial/`](../../../docs/redes-e-wifi/ipv6/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/ipv6/fontes.yml)

## Fontes oficiais

- [IPv6 Specification](https://www.rfc-editor.org/rfc/rfc8200) — IETF / RFC Editor
- [IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291) — IETF / RFC Editor
- [Neighbor Discovery for IP version 6](https://www.rfc-editor.org/rfc/rfc4861) — IETF / RFC Editor
- [IPv6 Stateless Address Autoconfiguration](https://www.rfc-editor.org/rfc/rfc4862) — IETF / RFC Editor
- [Internet Control Message Protocol for IPv6](https://www.rfc-editor.org/rfc/rfc4443) — IETF / RFC Editor
