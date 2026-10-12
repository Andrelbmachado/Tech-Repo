---
name: network-automation
description: "Automatizar configuração de redes com NETCONF/YANG. Use quando: Gerência programática de equipamentos e configuração como código."
---

# Skill: Automação de redes

Automatizar configuração de redes com NETCONF/YANG.

## Quando usar

Gerência programática de equipamentos e configuração como código.

## Conceitos principais

- NETCONF (RFC 6241)
- Modelagem YANG 1.1 (RFC 7950)
- RESTCONF (RFC 8040)
- NMDA — datastores (RFC 8342)
- Fonte da verdade e configuração declarativa

## Boas práticas

- Versione configurações em Git
- Valide mudanças (dry-run/candidate) antes do commit
- Use modelos YANG padronizados quando houver
- Automatize rollback
- Aplique mudanças em lotes pequenos

## Armadilhas comuns

- Automação sem validação propagando erros em massa
- Credenciais em texto claro
- Divergência entre fonte da verdade e equipamentos

## Checklist

- [ ] Versione configurações em Git
- [ ] Valide mudanças (dry-run/candidate) antes do commit
- [ ] Use modelos YANG padronizados quando houver
- [ ] Automatize rollback
- [ ] Aplique mudanças em lotes pequenos
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/network-automation/`](../../../docs/redes-e-wifi/network-automation/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/network-automation/documentacao-oficial/`](../../../docs/redes-e-wifi/network-automation/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/network-automation/fontes.yml)

## Fontes oficiais

- Nenhuma fonte primária cadastrada ainda em `fontes.yml`; consulte a ficha da tecnologia e complete a curadoria antes de tratar esta skill como referência revisada.
