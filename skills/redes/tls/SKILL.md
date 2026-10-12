---
name: tls
description: "Configurar e auditar TLS 1.3/1.2 (RFC 8446, RFC 9325). Use quando: HTTPS, certificados e segurança de transporte."
---

# Skill: TLS

Configurar e auditar TLS 1.3/1.2 (RFC 8446, RFC 9325).

## Quando usar

HTTPS, certificados e segurança de transporte.

## Conceitos principais

- Handshake TLS 1.3
- Certificados X.509 e cadeia de confiança
- Cipher suites e forward secrecy
- SNI (RFC 6066) e ALPN (RFC 7301)
- Descontinuação de TLS 1.0/1.1 (RFC 8996)

## Boas práticas

- Siga as recomendações da RFC 9325
- Desative TLS 1.0/1.1
- Automatize renovação de certificados
- Sirva a cadeia intermediária completa
- Valide certificados no cliente (nunca desative a verificação)

## Comandos e padrões comuns

```bash
openssl s_client -connect exemplo.com:443 -servername exemplo.com
openssl x509 -in cert.pem -noout -text
curl -v https://exemplo.com
```

## Armadilhas comuns

- Desativar verificação de certificado
- Certificados expirados
- Cadeia incompleta

## Checklist

- [ ] Siga as recomendações da RFC 9325
- [ ] Desative TLS 1.0/1.1
- [ ] Automatize renovação de certificados
- [ ] Sirva a cadeia intermediária completa
- [ ] Valide certificados no cliente (nunca desative a verificação)
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/tls/`](../../../docs/redes-e-wifi/tls/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/tls/documentacao-oficial/`](../../../docs/redes-e-wifi/tls/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/tls/fontes.yml)

## Fontes oficiais

- [The Transport Layer Security Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446) — IETF / RFC Editor
- [Recommendations for Secure Use of TLS and DTLS](https://www.rfc-editor.org/rfc/rfc9325) — IETF / RFC Editor
- [Deprecating TLS 1.0 and TLS 1.1](https://www.rfc-editor.org/rfc/rfc8996) — IETF / RFC Editor
- [TLS Extensions](https://www.rfc-editor.org/rfc/rfc6066) — IETF / RFC Editor
- [TLS Application-Layer Protocol Negotiation Extension](https://www.rfc-editor.org/rfc/rfc7301) — IETF / RFC Editor
