---
name: http-3
description: "Usar e depurar HTTP/3 sobre QUIC (RFC 9114, 9000). Use quando: Transporte web de baixa latência sobre UDP."
---

# Skill: HTTP/3

Usar e depurar HTTP/3 sobre QUIC (RFC 9114, 9000).

## Quando usar

Transporte web de baixa latência sobre UDP.

## Conceitos principais

- QUIC (RFC 9000): transporte sobre UDP com TLS 1.3 embutido
- Streams independentes sem HOL blocking de transporte
- QPACK (RFC 9204)
- Descoberta via Alt-Svc
- Migração de conexão

## Boas práticas

- Libere UDP/443 no firewall
- Mantenha fallback para HTTP/2
- Anuncie com cabeçalho Alt-Svc ou registro HTTPS
- Monitore taxa de uso de QUIC
- Teste com `curl --http3`

## Comandos e padrões comuns

```bash
curl -sI --http3 https://exemplo.com
```

## Armadilhas comuns

- UDP bloqueado em redes corporativas
- Middleboxes sem visibilidade
- Diferenças de suporte entre clientes

## Checklist

- [ ] Libere UDP/443 no firewall
- [ ] Mantenha fallback para HTTP/2
- [ ] Anuncie com cabeçalho Alt-Svc ou registro HTTPS
- [ ] Monitore taxa de uso de QUIC
- [ ] Teste com `curl --http3`
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/http-3/`](../../../docs/redes-e-wifi/http-3/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/http-3/documentacao-oficial/`](../../../docs/redes-e-wifi/http-3/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/http-3/fontes.yml)

## Fontes oficiais

- [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114) — IETF / RFC Editor
- [QUIC: A UDP-Based Multiplexed and Secure Transport](https://www.rfc-editor.org/rfc/rfc9000) — IETF / RFC Editor
- [QPACK: Field Compression for HTTP/3](https://www.rfc-editor.org/rfc/rfc9204) — IETF / RFC Editor
- [HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — IETF / RFC Editor
- [HTTP/3: Extensible Prioritization Scheme](https://www.rfc-editor.org/rfc/rfc9218) — IETF / RFC Editor
