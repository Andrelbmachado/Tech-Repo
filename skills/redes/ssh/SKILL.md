---
name: ssh
description: "Usar e endurecer SSH (RFC 4251–4254). Use quando: Acesso remoto seguro, túneis e transferência de arquivos."
---

# Skill: SSH

Usar e endurecer SSH (RFC 4251–4254).

## Quando usar

Acesso remoto seguro, túneis e transferência de arquivos.

## Conceitos principais

- Arquitetura: transporte, autenticação e conexão
- Chaves de host e verificação de fingerprint
- Autenticação por chave pública
- Canais, port forwarding e agent forwarding
- SCP/SFTP

## Boas práticas

- Use autenticação por chave e desative senha quando possível
- Desative login direto de root
- Verifique fingerprints na primeira conexão
- Use algoritmos modernos (ex.: Ed25519)
- Limite agent forwarding a hosts confiáveis

## Comandos e padrões comuns

```bash
ssh-keygen -t ed25519
ssh-copy-id usuario@host
ssh -L 8080:localhost:80 usuario@host
ssh -v usuario@host
```

## Armadilhas comuns

- Ignorar aviso de mudança de chave de host
- Chaves privadas sem senha compartilhadas
- Agent forwarding em hosts não confiáveis

## Checklist

- [ ] Use autenticação por chave e desative senha quando possível
- [ ] Desative login direto de root
- [ ] Verifique fingerprints na primeira conexão
- [ ] Use algoritmos modernos (ex.: Ed25519)
- [ ] Limite agent forwarding a hosts confiáveis
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/ssh/`](../../../docs/redes-e-wifi/ssh/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/ssh/documentacao-oficial/`](../../../docs/redes-e-wifi/ssh/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/ssh/fontes.yml)

## Fontes oficiais

- [The Secure Shell Protocol Architecture](https://www.rfc-editor.org/rfc/rfc4251) — IETF / RFC Editor
- [SSH Authentication Protocol](https://www.rfc-editor.org/rfc/rfc4252) — IETF / RFC Editor
- [SSH Transport Layer Protocol](https://www.rfc-editor.org/rfc/rfc4253) — IETF / RFC Editor
- [SSH Connection Protocol](https://www.rfc-editor.org/rfc/rfc4254) — IETF / RFC Editor
- [SSH Protocol Assigned Numbers](https://www.rfc-editor.org/rfc/rfc4250) — IETF / RFC Editor
