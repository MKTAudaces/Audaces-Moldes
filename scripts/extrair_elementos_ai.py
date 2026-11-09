"""Rasteriza o .ai do Moldes e extrai elementos com fundo transparente.

O arquivo .ai e compativel com PDF, entao o poppler (pdftocairo) consegue renderiza-lo.
O fundo branco da arte e convertido em transparencia ("color to alpha"), o que
preserva os degradês e traços finos dos moldes.

Uso:
    python scripts/extrair_elementos_ai.py "illustrator/Moldes - Splash A360.ai" saida/
Requer: poppler-utils (pdftocairo), pillow, numpy.

As caixas abaixo estao em coordenadas de um preview de 1074x833 px
(render a 133 dpi); sao multiplicadas por 3 para o render de 400 dpi.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

ai, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)
tmp = tempfile.mkdtemp()
subprocess.run(["pdftocairo", "-png", "-r", "400", "-transp", "-singlefile", ai, f"{tmp}/ai"], check=True)
im = Image.open(f"{tmp}/ai.png").convert("RGBA")

a = np.asarray(im).astype(np.float32) / 255.0
rgb = a[..., :3] * a[..., 3:4] + (1 - a[..., 3:4])
alpha = np.clip(np.max(1 - rgb, axis=2) * 1.15, 0, 1)
safe = np.where(alpha > 1e-4, alpha, 1)
col = np.clip((rgb - (1 - alpha[..., None])) / safe[..., None], 0, 1)
keyed = Image.fromarray((np.dstack([col, alpha]) * 255).astype(np.uint8), "RGBA")

K = 3
BOXES = {
    "molde-saia": (565, 183, 778, 378),
    "molde-blusa": (588, 428, 737, 618),
    "card-croqui-casaco": (827, 166, 1004, 394),
    "card-croqui-casaco-costas": (823, 413, 1007, 650),
    "moldes-base-corpo": (398, 172, 562, 418),
    "listras-teal": (340, 436, 432, 480),
    "molde-gola": (490, 378, 642, 420),
    "molde-frente": (432, 412, 530, 632),
}
for nome, (x0, y0, x1, y1) in BOXES.items():
    c = keyed.crop((x0 * K, y0 * K, x1 * K, y1 * K))
    c.crop(c.getbbox()).save(f"{outdir}/{nome}.png")
    print(nome)
# Obs.: os cards de croqui ficam com o miolo transparente; coloque um retangulo
# branco com cantos arredondados atras deles (ver elementos/moldes/card-croqui-casaco.png).
