---
name: bgp
description: "Configurar e analisar BGP-4 (RFC 4271) e extensões. Use quando: Roteamento entre sistemas autônomos, multihoming e peering."
---

# Skill: BGP

Configurar e analisar BGP-4 (RFC 4271) e extensões.

## Quando usar

Roteamento entre sistemas autônomos, multihoming e peering.

## Conceitos principais

- Sessões eBGP/iBGP sobre TCP 179
- Atributos de caminho (AS_PATH, NEXT_HOP, LOCAL_PREF, MED)
- Processo de decisão
- Multiprotocol BGP (RFC 4760) e ASN de 4 bytes (RFC 6793)
- Roles e prevenção de route leaks (RFC 9234)

## Boas práticas

- Filtre prefixos de entrada e saída
- Siga RFC 7454 (BGP Operations and Security)
- Use max-prefix e autenticação de sessão
- Valide origem (RPKI) quando possível
- Documente políticas por vizinho

## Armadilhas comuns

- Route leaks por falta de filtros
- Sequestro de prefixos
- Next-hop inalcançável em iBGP

## Checklist

- [ ] Filtre prefixos de entrada e saída
- [ ] Siga RFC 7454 (BGP Operations and Security)
- [ ] Use max-prefix e autenticação de sessão
- [ ] Valide origem (RPKI) quando possível
- [ ] Documente políticas por vizinho
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/bgp/`](../../../docs/redes-e-wifi/bgp/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/bgp/documentacao-oficial/`](../../../docs/redes-e-wifi/bgp/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/bgp/fontes.yml)

## Fontes oficiais

- [A Border Gateway Protocol 4 (BGP-4)](https://www.rfc-editor.org/rfc/rfc4271) — IETF / RFC Editor
- [Multiprotocol Extensions for BGP-4](https://www.rfc-editor.org/rfc/rfc4760) — IETF / RFC Editor
- [BGP Support for Four-Octet AS Number Space](https://www.rfc-editor.org/rfc/rfc6793) — IETF / RFC Editor
- [A BGP Route Leak Prevention and Detection](https://www.rfc-editor.org/rfc/rfc9234) — IETF / RFC Editor
- [BGP Operations and Security](https://www.rfc-editor.org/rfc/rfc7454) — IETF / RFC Editor
