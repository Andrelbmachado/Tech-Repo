---
name: network-routing
description: "Projetar e diagnosticar roteamento (OSPF, BGP e estático). Use quando: Escolha de protocolos e troubleshooting de rotas."
---

# Skill: Roteamento de redes

Projetar e diagnosticar roteamento (OSPF, BGP e estático).

## Quando usar

Escolha de protocolos e troubleshooting de rotas.

## Conceitos principais

- Tabela de roteamento e longest prefix match
- Rotas estáticas vs. dinâmicas
- OSPFv2 (RFC 2328) e OSPFv3 (RFC 5340)
- BGP (RFC 4271)
- Distância administrativa e métricas

## Boas práticas

- Sumarize rotas onde possível
- Autentique adjacências
- Documente o desenho de áreas/AS
- Monitore flaps de rota
- Use `traceroute` para validar caminhos

## Comandos e padrões comuns

```bash
ip route
traceroute host
ip route get 203.0.113.1
```

## Armadilhas comuns

- Loops de roteamento
- Rotas assimétricas e firewalls stateful
- Redistribuição mútua sem filtros

## Checklist

- [ ] Sumarize rotas onde possível
- [ ] Autentique adjacências
- [ ] Documente o desenho de áreas/AS
- [ ] Monitore flaps de rota
- [ ] Use `traceroute` para validar caminhos
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/redes-e-wifi/network-routing/`](../../../docs/redes-e-wifi/network-routing/README.md)
- Documentação oficial (cópia local ou links): [`docs/redes-e-wifi/network-routing/documentacao-oficial/`](../../../docs/redes-e-wifi/network-routing/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/redes-e-wifi/network-routing/fontes.yml)

## Fontes oficiais

- Nenhuma fonte primária cadastrada ainda em `fontes.yml`; consulte a ficha da tecnologia e complete a curadoria antes de tratar esta skill como referência revisada.
