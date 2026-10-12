---
name: r
description: "Analisar dados e programar em R. Use quando: Estatística, análise e visualização de dados, pesquisa científica."
---

# Skill: R

Analisar dados e programar em R.

## Quando usar

Estatística, análise e visualização de dados, pesquisa científica.

## Conceitos principais

- Vetores, listas, data frames e fatores
- Vetorização e família `apply`
- Avaliação preguiçosa de argumentos e ambientes
- Pacotes CRAN e estrutura de pacote
- Sistemas de objetos S3/S4

## Boas práticas

- Prefira operações vetorizadas a laços
- Use projetos e caminhos relativos
- Documente pacotes conforme Writing R Extensions
- Fixe versões de pacotes (ex.: renv)
- Use `set.seed()` para reprodutibilidade

## Comandos e padrões comuns

```bash
Rscript analise.R
R CMD build pacote
R CMD check pacote_1.0.tar.gz
R -e 'install.packages("pkg")'
```

## Armadilhas comuns

- Índices começam em 1
- Conversão silenciosa de fatores
- Reciclagem de vetores de tamanhos diferentes

## Checklist

- [ ] Prefira operações vetorizadas a laços
- [ ] Use projetos e caminhos relativos
- [ ] Documente pacotes conforme Writing R Extensions
- [ ] Fixe versões de pacotes (ex.: renv)
- [ ] Use `set.seed()` para reprodutibilidade
- [ ] Conferi a versão/edição aplicável em `versoes.md` e na fonte oficial
- [ ] Validei afirmações críticas na documentação oficial abaixo

## Documentação no repositório

- Ficha da tecnologia: [`docs/programacao/linguagens/r/`](../../../docs/programacao/linguagens/r/README.md)
- Documentação oficial (cópia local ou links): [`docs/programacao/linguagens/r/documentacao-oficial/`](../../../docs/programacao/linguagens/r/documentacao-oficial/README.md)
- Fontes registradas: [`fontes.yml`](../../../docs/programacao/linguagens/r/fontes.yml)

## Fontes oficiais

- [R manuals](https://cran.r-project.org/manuals.html) — R Core Team
- [An Introduction to R](https://cran.r-project.org/doc/manuals/r-release/R-intro.html) — R Core Team
- [R Language Definition](https://cran.r-project.org/doc/manuals/r-release/R-lang.html) — R Core Team
- [Writing R Extensions](https://cran.r-project.org/doc/manuals/r-release/R-exts.html) — R Core Team
- [R Installation and Administration](https://cran.r-project.org/doc/manuals/r-release/R-admin.html) — R Core Team
