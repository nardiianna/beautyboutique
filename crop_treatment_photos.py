import os
from PIL import Image
import numpy as np

SRC = ("/Users/anna.nardi/Library/Mobile Documents/com~apple~CloudDocs/"
       "Lavolo/Nardi creates/SITI/Beauty Boutique/immagini real/trattamenti")
OUT = "images"

# (source relative path, output filename)
JOBS = [
    ("corpo/WhatsApp Image 2026-09-16 at 17.56.41 (1).jpeg", "treatment2-drenante.jpg"),
    ("corpo/WhatsApp Image 2026-09-16 at 17.56.41 (2).jpeg", "treatment2-riducente.jpg"),
    ("corpo/WhatsApp Image 2026-09-16 at 17.56.41 (3).jpeg", "treatment2-detox.jpg"),
    ("corpo/WhatsApp Image 2026-09-16 at 17.56.41 (4).jpeg", "treatment2-liporiducente.jpg"),
    ("viso/WhatsApp Image 2026-09-16 at 17.56.10.jpeg", "treatment2-illuminante.jpg"),
    ("viso/WhatsApp Image 2026-09-16 at 17.56.11 (2).jpeg", "treatment2-liftante.jpg"),
    ("viso/WhatsApp Image 2026-09-16 at 17.56.11 (3).jpeg", "treatment2-antimacchia.jpg"),
    ("viso/WhatsApp Image 2026-09-16 at 17.56.11 (7).jpeg", "treatment2-idratazione.jpg"),
    ("viso/WhatsApp Image 2026-09-16 at 17.56.11 (5).jpeg", "treatment2-esfoliante.jpg"),
    ("viso/WhatsApp Image 2026-09-16 at 17.56.11 (4).jpeg", "treatment2-antieta.jpg"),
    ("viso/WhatsApp Image 2026-09-16 at 17.56.11 (6).jpeg", "treatment2-pellisensibili.jpg"),
    ("viso/WhatsApp Image 2026-09-16 at 17.56.11 (1).jpeg", "treatment2-contornoocchi.jpg"),
]

def find_boundary(arr, threshold=15, confirm=30):
    h = arr.shape[0]
    row_med = np.median(arr, axis=(1, 2))
    candidate = None
    for y in range(h - 1, -1, -1):
        if row_med[y] >= threshold:
            if candidate is None:
                candidate = y
            elif candidate - y + 1 >= confirm:
                return candidate + 1
        else:
            candidate = None
    return 0

for rel, out_name in JOBS:
    path = os.path.join(SRC, rel)
    im = Image.open(path).convert("RGB")
    arr = np.asarray(im).astype(np.float32)
    boundary = find_boundary(arr)
    cropped = im.crop((0, 0, im.width, boundary))
    out_path = os.path.join(OUT, out_name)
    cropped.save(out_path, quality=90)
    print(f"{rel} -> {out_name}: {im.height} -> {boundary}px ({im.width}x{boundary})")
