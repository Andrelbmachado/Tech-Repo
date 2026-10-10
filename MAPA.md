# Mapa do repositório

## Leitura rápida

1. `README.md`: propósito e política editorial.
2. `MAPA.md`: hierarquia e navegação por área.
3. `MAPA-TECNOLOGIAS.md`: lista navegável das tecnologias cadastradas.
4. `INDICE-IA.yaml`: inventário estruturado para ingestão automatizada.
5. `CATALOG.yml`: catálogo completo com caminhos e estado de curadoria.
6. Pasta da tecnologia: resumo, metadados, fontes, versões e boas práticas.

## Hierarquia

```text
docs/
├── fundamentos/                 # conceitos transversais e fundamentos técnicos
├── programacao/
│   ├── linguagens/              # linguagens e respectivas referências
│   ├── web/                     # HTML, CSS, APIs e formatos Web
│   ├── bancos-de-dados/         # SQL e tecnologias de dados
│   └── runtimes-e-frameworks/   # ambientes, bibliotecas e frameworks
├── redes-e-wifi/                # protocolos, infraestrutura e Wi-Fi
├── ciberseguranca/              # padrões, práticas e resposta a incidentes
├── devops-e-cloud/              # nuvem, automação, entrega e operações
├── engenharia-de-software/      # métodos, arquitetura, testes e qualidade
├── eletronica/                  # circuitos, componentes e projeto eletrônico
├── sistemas-embarcados/         # firmware, microcontroladores e IoT
└── engenharia-mecanica/         # materiais, projeto, análise e processos
```

Cada tecnologia fica em uma pasta própria. O `CATALOG.yml` aponta para o diretório e registra o estado; `fontes.yml` classifica referências primárias, oficiais de fornecedor ou secundárias.

## Convenções para agentes de IA

- Leia este mapa e o índice antes de percorrer arquivos em massa.
- Use `tech.yml` como fonte de identidade e `fontes.yml` para verificar afirmações técnicas.
- Respeite idioma, versão, autoridade, status editorial e licença declarados.
- Não trate documento de fornecedor como padrão normativo, nem fonte secundária como oficial.
- `verified_at` registra quando a fonte foi conferida; não garante que o conteúdo seguirá atual.
- Veja o [mapa completo das tecnologias](MAPA-TECNOLOGIAS.md) para abrir uma entrada específica.

## Estados

- Estado editorial: `planned`, `in-progress` ou `curated`.
- Quota de fontes oficiais: `pending`, `partial` ou `complete`.
- `partial` exige justificativa; `pending` indica pesquisa ou verificação ainda não concluída.
