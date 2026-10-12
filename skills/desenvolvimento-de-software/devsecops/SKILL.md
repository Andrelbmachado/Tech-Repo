---
name: devsecops
description: "Integrar segurança ao ciclo de desenvolvimento (NIST SSDF, OWASP). Use quando: Desenvolvimento seguro, revisão de segurança e automação de controles no pipeline."
---

# Skill: DevSecOps e desenvolvimento seguro

Integrar segurança ao ciclo de desenvolvimento (NIST SSDF, OWASP).

## Quando usar

Desenvolvimento seguro, revisão de segurança e automação de controles no pipeline.

## Conceitos principais

- NIST SP 800-218 (SSDF): preparar a organização, proteger o software, produzir software bem protegido, responder a vulnerabilidades
- OWASP Top 10 e ASVS (cópias locais em ciberseguranca)
- Modelagem de ameaças
- SAST, DAST, SCA e varredura de segredos
- Cadeia de suprimentos de software (SBOM)

## Boas práticas

- Valide e codifique toda entrada/saída
- Automatize SCA e varredura de segredos no CI
- Aplique menor privilégio a serviços e pipelines
- Use o ASVS como checklist de requisitos
- Tenha processo de resposta a vulnerabilidades

## Armadilhas comuns

- Segurança só no fim do projeto
- Dependências desatualizadas
- Segredos em código ou logs

## Checklist

- [ ] Valide e codifique toda entrada/saída
- [ ] Automatize SCA e varredura de segredos no CI
- [ ] Aplique menor privilégio a serviços e pipelines
- [ ] Use o ASVS como checklist de requisitos
- [ ] Tenha processo de resposta a vulnerabilidades
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/devops-e-cloud/devsecops/`](../../../docs/devops-e-cloud/devsecops/README.md)
- Documentação oficial (cópia local ou links): [`docs/devops-e-cloud/devsecops/documentacao-oficial/`](../../../docs/devops-e-cloud/devsecops/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/devops-e-cloud/devsecops/fontes.yml)

## Fontes oficiais

- Nenhuma fonte primária cadastrada ainda em `fontes.yml`; consulte a ficha da tecnologia e complete a curadoria antes de tratar esta skill como referência revisada.
