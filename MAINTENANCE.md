# Manutenção do catálogo

## Frequência

- Semanal: GitHub Actions verifica URLs em `fontes.yml`; erros HTTP e falhas de rede ficam visíveis no workflow.
- Mensal: revisar fontes de maior volatilidade, versões de runtime, documentação de nuvem e páginas de advisories.
- Trimestral: revisar normas, especificações, categorias, fontes secundárias e tecnologias sem atualização editorial.
- Sob demanda: substituir link removido, registrar mudança de status, arquivar uma fonte ou elevar uma entrada para `curated`.

## Ao revisar uma fonte

1. Confirme que o endereço é HTTPS e aponta para o documento, padrão ou landing page oficial identificada.
2. Registre versão/edição, status (vigente, supersedido, rascunho ou arquivado) e condição de acesso.
3. Atualize `verified_at` quando o conteúdo da fonte e os metadados forem conferidos.
4. Não substitua a URL de uma edição antiga quando ela for necessária para contexto; registre a edição atual como nova fonte e marque a antiga nos `notes`.
5. Reavalie `source_quota` e os resumos bilíngues. Atingir cinco links não basta se forem cópias da mesma página ou conteúdo irrelevante.

## Mudanças de status

Use `planned` para esboços sem conteúdo de curadoria, `in-progress` durante pesquisa e revisão, e `curated` quando o resumo e os metadados tiverem revisão humana. Marque a quota como `complete` somente com cinco ou mais fontes oficiais relevantes; `partial` exige justificativa; `pending` significa que a pesquisa continua.

## Links quebrados

Tente a URL canônica do mantenedor ou organismo. Registre redirecionamento permanente quando útil. Se o material tiver sido removido, procure a página oficial de arquivo ou a revisão substituta; não aponte para cópias não autorizadas. Falhas temporárias de rede não devem ser registradas como remoção sem nova checagem.
