---
name: http-2
description: "Usar e depurar HTTP/2 (RFC 9113). Use quando: Desempenho web, multiplexação e servidores/proxies HTTP."
---

# Skill: HTTP/2

Usar e depurar HTTP/2 (RFC 9113).

## Quando usar

Desempenho web, multiplexação e servidores/proxies HTTP.

## Conceitos principais

- Semântica HTTP comum (RFC 9110)
- Framing binário, streams e multiplexação
- HPACK (compressão de cabeçalhos)
- Controle de fluxo
- Priorização (RFC 9218)

## Boas práticas

- Use TLS com ALPN `h2`
- Não dependa de técnicas HTTP/1.1 como domain sharding
- Configure limites de streams
- Considere as notas de segurança (seção 9 da RFC 9113)
- Teste com `curl --http2`

## Comandos e padrões comuns

```bash
curl -sI --http2 https://exemplo.com
```

## Armadilhas comuns

- Head-of-line blocking no TCP
- Proxies degradando para HTTP/1.1
- Ataques de abuso de streams

## Checklist

- [ ] Use TLS com ALPN `h2`
- [ ] Não dependa de técnicas HTTP/1.1 como domain sharding
- [ ] Configure limites de streams
- [ ] Considere as notas de segurança (seção 9 da RFC 9113)
- [ ] Teste com `curl --http2`
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/http-2/`](../../../docs/redes-e-wifi/http-2/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/http-2/documentacao-oficial/`](../../../docs/redes-e-wifi/http-2/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/http-2/fontes.yml)

## Fontes oficiais

- [HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) — IETF / RFC Editor
- [HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — IETF / RFC Editor
- [HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112) — IETF / RFC Editor
- [HTTP/2 Prioritization](https://www.rfc-editor.org/rfc/rfc9218) — IETF / RFC Editor
- [Using TLS to Secure HTTP/2](https://www.rfc-editor.org/rfc/rfc9113#section-9) — IETF / RFC Editor
