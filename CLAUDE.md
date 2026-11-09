# Instruções para o Claude — capas do Audaces Moldes

Quando pedirem uma **capa** (Reels/Stories) para o Audaces Moldes:

1. **Leia o `README.md`** (guia de identidade: área segura, cores, fonte, composição).
2. **Veja as referências** em `referencias/capas/` para não repetir um estilo já usado. A pessoa costuma pedir algo *diferente* dos estilos existentes — proponha variação, mantendo a identidade.
3. **Monte no Figma** (arquivo: `Ja1mfAefyD5p7gn06Lsif5`, frame `Styles` / node `1:19`). Crie um frame novo 1080×1920 ao lado dos existentes, nomeado `Style N` ou `Style N - vX`. Para variações, **duplique o frame atual** em vez de editar por cima.
4. **Elementos prontos** (PNG transparente) em `elementos/` — suba com `upload_assets` do Figma MCP. Precisa de outro elemento do Moldes? Use `scripts/extrair_elementos_ai.py` no `.ai`.
5. **Foto de pessoa:** recorte o fundo com `scripts/recortar_fundo.py` (modelo `birefnet-portrait`) e coloque o PNG em `elementos/fotos/`.

## Regras que a equipe já pediu
- **Margem de 250 px em cima e embaixo**: nenhum texto ou informação importante fora de y 250–1670. Logos podem passar.
- **Tudo centralizado** (título, subtítulo, pessoa, card, selo).
- Moldes de roupa **espalhados dos dois lados**, equilibrados, atrás da pessoa e na frente do card.
- Fonte **Sora**; azul `#0166FF`; verde-água `#6FD3C1`; fundo claro `#F2F2F3`.
- Copy: título em caixa alta Bold, subtítulo Regular, os dois em azul.
- Entregue a v1 rápida e itere — a equipe ajusta no Figma e pede v2/v3.

## Ao salvar uma capa nova como referência
Exporte 1080×1920 em PNG para `referencias/capas/style-N/NN-slug-do-titulo.png` e, se for um estilo novo, descreva-o na seção "Estrutura" do README.
