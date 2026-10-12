---
name: tcp-ip
description: "Entender e diagnosticar a pilha TCP/IP. Use quando: Troubleshooting de conectividade e desempenho de aplicações de rede."
---

# Skill: TCP/IP

Entender e diagnosticar a pilha TCP/IP.

## Quando usar

Troubleshooting de conectividade e desempenho de aplicações de rede.

## Conceitos principais

- Camadas: enlace, internet, transporte, aplicação (RFC 1122)
- TCP (RFC 9293): handshake, janelas, retransmissão
- UDP (RFC 768)
- IPv4/IPv6
- Portas e sockets

## Boas práticas

- Diagnostique camada por camada
- Capture tráfego para evidência
- Considere MTU e perdas em problemas de desempenho
- Configure timeouts e keepalives nas aplicações
- Use `ss`/`netstat` para ver sockets

## Comandos e padrões comuns

```bash
ip addr
ip route
ss -tulpn
ping -c 4 host
traceroute host
tcpdump -i eth0 port 443
```

## Armadilhas comuns

- Culpar a rede sem evidência
- Timeouts mal configurados
- Esgotamento de portas efêmeras

## Checklist

- [ ] Diagnostique camada por camada
- [ ] Capture tráfego para evidência
- [ ] Considere MTU e perdas em problemas de desempenho
- [ ] Configure timeouts e keepalives nas aplicações
- [ ] Use `ss`/`netstat` para ver sockets
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/tcp-ip/`](../../../docs/redes-e-wifi/tcp-ip/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/tcp-ip/documentacao-oficial/`](../../../docs/redes-e-wifi/tcp-ip/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/tcp-ip/fontes.yml)

## Fontes oficiais

- [Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — IETF / RFC Editor
- [Internet Protocol](https://www.rfc-editor.org/rfc/rfc791) — IETF / RFC Editor
- [IPv6 Specification](https://www.rfc-editor.org/rfc/rfc8200) — IETF / RFC Editor
- [User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — IETF / RFC Editor
- [Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1122) — IETF / RFC Editor
