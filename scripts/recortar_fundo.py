"""Recorta o fundo de uma foto (ex.: modelo para capa) e salva PNG transparente.

Uso:
    pip install rembg pillow
    python scripts/recortar_fundo.py entrada.jpg saida.png [modelo]

Modelo padrao: birefnet-portrait (melhor para pessoas; ~1 GB, baixado na 1a execucao).
Alternativas: birefnet-general (objetos), u2net (mais leve).
"""
import sys
from PIL import Image
from rembg import remove, new_session

entrada, saida = sys.argv[1], sys.argv[2]
modelo = sys.argv[3] if len(sys.argv) > 3 else "birefnet-portrait"
img = Image.open(entrada).convert("RGB")
out = remove(
    img,
    session=new_session(modelo),
    alpha_matting=True,
    alpha_matting_foreground_threshold=240,
    alpha_matting_background_threshold=15,
    alpha_matting_erode_size=8,
)
out.crop(out.getbbox()).save(saida) if "--trim" in sys.argv else out.save(saida)
print("ok ->", saida)
