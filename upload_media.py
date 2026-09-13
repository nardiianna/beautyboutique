import base64, json, mimetypes, os, sys, urllib.request
from wp_config import SITE, USER, APPPW

auth = base64.b64encode(f"{USER}:{APPPW}".encode()).decode()

IMG_DIR = "images"

# filename -> alt text
ALT = {
    "logo-header.png": "Beauty Boutique - Centro Estetico",
    "logo-footer.png": "Beauty Boutique - Centro Estetico",
    "hero-bg.jpg": "Trattamento estetico viso",
    "icon-viso.png": "Icona trattamenti viso",
    "icon-corpo.png": "Icona trattamenti corpo",
    "icon-epilazione.png": "Icona epilazione",
    "icon-ciglia.png": "Icona ciglia e sguardo",
    "icon-benessere.png": "Icona benessere",
    "treatment-viso.jpg": "Trattamento viso",
    "treatment-corpo.jpg": "Trattamento corpo",
    "treatment-ciglia.jpg": "Trattamento ciglia",
    "treatment-benessere.jpg": "Trattamento benessere",
    "studio-centro.jpg": "Espositore dei prodotti Physio Natura nel centro estetico",
    "prodotti-physio.jpg": "Linea cosmetici Physio Natura",
    "result-ciglia.jpg": "Occhio prima e dopo la laminazione ciglia",
    "result-viso.jpg": "Pelle prima e dopo il trattamento viso",
    "cta-banner-bg.jpg": "Sfondo banner prenotazione",
    "footer-flower.png": "Decorazione floreale",
    "powered-by-nardicreates.png": "Powered by Nardi Creates",
    "bg-texture-unused.jpg": "Texture decorativa",
}

results = {}

for fname in sorted(os.listdir(IMG_DIR)):
    path = os.path.join(IMG_DIR, fname)
    if not os.path.isfile(path):
        continue
    mime = mimetypes.guess_type(fname)[0] or "application/octet-stream"
    with open(path, "rb") as f:
        data = f.read()

    req = urllib.request.Request(
        f"{SITE}/wp-json/wp/v2/media",
        data=data,
        method="POST",
        headers={
            "Authorization": f"Basic {auth}",
            "Content-Type": mime,
            "Content-Disposition": f'attachment; filename="{fname}"',
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            body = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"FAILED {fname}: {e.code} {e.read().decode()[:300]}")
        continue

    media_id = body["id"]
    source_url = body["source_url"]
    results[fname] = {"id": media_id, "url": source_url}
    print(f"Uploaded {fname} -> id={media_id} url={source_url}")

    # Set alt text if we have one
    alt = ALT.get(fname)
    if alt:
        patch_data = json.dumps({"alt_text": alt}).encode()
        preq = urllib.request.Request(
            f"{SITE}/wp-json/wp/v2/media/{media_id}",
            data=patch_data,
            method="POST",
            headers={
                "Authorization": f"Basic {auth}",
                "Content-Type": "application/json",
            },
        )
        try:
            urllib.request.urlopen(preq)
        except urllib.error.HTTPError as e:
            print(f"  alt_text patch failed for {fname}: {e.code}")

with open("media_map.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nDone. Saved media_map.json")
