# Audaces Moldes — Kit de capas

Referências, arquivos-fonte e elementos visuais para criar **capas de Reels/Stories do Audaces Moldes**.

- **Figma das capas:** https://www.figma.com/design/Ja1mfAefyD5p7gn06Lsif5/Sem-t%C3%ADtulo?node-id=1-19 (frame `Styles`)
- **Arte-base da marca:** `illustrator/Moldes - Splash A360.ai` (preview em `illustrator/preview-splash-a360.png`)

## Estrutura

```
illustrator/            Arquivo .ai original do Moldes (Splash A360) + preview PNG
referencias/capas/      Capas já publicadas, separadas por estilo (1080x1920)
  style-1/              Fundo azul / foto de produto + bloco azul com título
  style-2/              Especialista em foto + bloco azul recortado no topo
  style-3/              Fundo claro texturizado + ilustrações de moldes do .ai
  style-4/              Fundo claro + modelo recortada dentro de card do Moldes
elementos/
  logos/                "A" da Audaces, ícone do Moldes, lockup Audaces Moldes (PNG transparente)
  moldes/               Moldes e cards de croqui extraídos do .ai (PNG transparente)
  fotos/                Fotos de pessoas já recortadas
scripts/                Recorte de fundo de fotos e extração de elementos do .ai
```

## Guia rápido da identidade

| Item | Valor |
|---|---|
| Formato | 1080 × 1920 px (9:16) |
| **Área segura** | **250 px em cima e 250 px embaixo** — textos e informações importantes ficam entre y=250 e y=1670. Logos podem ultrapassar. |
| Composição | Elementos **centralizados** (título, modelo, card e selo no eixo central) |
| Fonte | **Sora** — Bold para título (≈116 px, caixa alta, entrelinha 100%), Regular para subtítulo (≈44 px, entrelinha 125%) |
| Azul Audaces (textos/logo) | `#0166FF` |
| Verde-água Moldes | `#6FD3C1` (traços, pontilhados, acentos) · escuro `#2E8C7C` |
| Fundo claro (style 3/4) | `#F2F2F3` |
| Borda dos cards (degradê) | `#F5A8BA` → `#C9B5F0` → `#8FDCCB`, 10 px, cantos 64 px |
| Logo topo | "A" Audaces azul, 72 px, centralizado, y≈96 |
| Selo | Pílula branca com lockup **Audaces Moldes**, sombra suave, dentro da área segura |

### Linguagem visual do Moldes
- Moldes de modelagem em traço verde-água com preenchimento em **degradê granulado lilás/rosa/verde-água**.
- Cards brancos arredondados com borda em degradê (croquis técnicos dentro).
- Linhas pontilhadas verde-água, listras paralelas, padrão de pontos (halftone).
- Moldes "flutuando" levemente rotacionados (±5–10°), distribuídos dos dois lados, atrás da pessoa.

## Copy → capa
Cada capa tem: **título** (curto, caixa alta, 1–2 linhas), **subtítulo** (1–2 linhas) e presença da marca (logo/selo/ícone do Moldes).

Exemplo (style-4): `MODELAGENS COMPLEXAS` / `Como o digital contribui no desenvolvimento`.

## Scripts

```bash
pip install rembg pillow numpy
```

```bash
python scripts/recortar_fundo.py foto.jpg elementos/fotos/nome-recortado.png
```

```bash
python scripts/extrair_elementos_ai.py "illustrator/Moldes - Splash A360.ai" saida/
```
