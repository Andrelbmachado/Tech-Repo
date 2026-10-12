---
name: dns
description: "Configurar e depurar DNS (RFC 1034/1035) e DNSSEC. Use quando: Resolução de nomes, zonas, registros e troubleshooting."
---

# Skill: DNS

Configurar e depurar DNS (RFC 1034/1035) e DNSSEC.

## Quando usar

Resolução de nomes, zonas, registros e troubleshooting.

## Conceitos principais

- Hierarquia, zonas e delegação
- Registros: A, AAAA, CNAME, MX, NS, TXT, SOA
- Resolvers recursivos vs. autoritativos
- TTL e cache
- DNSSEC (RFC 4033) e EDNS(0) (RFC 6891)

## Boas práticas

- Reduza o TTL antes de migrações
- Tenha pelo menos dois servidores autoritativos
- Não coloque CNAME no apex da zona
- Assine zonas com DNSSEC quando viável
- Use a terminologia da RFC 8499

## Comandos e padrões comuns

```bash
dig exemplo.com A
dig +trace exemplo.com
dig @1.1.1.1 exemplo.com MX
nslookup exemplo.com
```

## Armadilhas comuns

- Cache com TTL longo atrasando mudanças
- CNAME junto a outros registros
- Delegação inconsistente (lame delegation)

## Checklist

- [ ] Reduza o TTL antes de migrações
- [ ] Tenha pelo menos dois servidores autoritativos
- [ ] Não coloque CNAME no apex da zona
- [ ] Assine zonas com DNSSEC quando viável
- [ ] Use a terminologia da RFC 8499
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/dns/`](../../../docs/redes-e-wifi/dns/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/dns/documentacao-oficial/`](../../../docs/redes-e-wifi/dns/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/dns/fontes.yml)

## Fontes oficiais

- [Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034) — IETF / RFC Editor
- [Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035) — IETF / RFC Editor
- [DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033) — IETF / RFC Editor
- [Extension Mechanisms for DNS](https://www.rfc-editor.org/rfc/rfc6891) — IETF / RFC Editor
- [DNS Terminology](https://www.rfc-editor.org/rfc/rfc8499) — IETF / RFC Editor
