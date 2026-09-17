import base64, json, mimetypes, os, urllib.request
from wp_config import SITE, USER, APPPW

auth = base64.b64encode(f"{USER}:{APPPW}".encode()).decode()

FILES = [
    "treatment2-drenante.jpg",
    "treatment2-riducente.jpg",
    "treatment2-detox.jpg",
    "treatment2-liporiducente.jpg",
    "treatment2-illuminante.jpg",
    "treatment2-liftante.jpg",
    "treatment2-antimacchia.jpg",
    "treatment2-idratazione.jpg",
    "treatment2-esfoliante.jpg",
    "treatment2-antieta.jpg",
    "treatment2-pellisensibili.jpg",
    "treatment2-contornoocchi.jpg",
    "treatment2-laminazione-ciglia.jpg",
    "treatment2-tatuaggio-labbra.jpg",
    "treatment2-tatuaggio-sopracciglia.jpg",
]

ALT = {
    "treatment2-drenante.jpg": "Trattamento drenante corpo",
    "treatment2-riducente.jpg": "Trattamento riducente anti gonfiore",
    "treatment2-detox.jpg": "Advanced Body Treatment - trattamento detox",
    "treatment2-liporiducente.jpg": "Trattamento liporiducente e rimodellante",
    "treatment2-illuminante.jpg": "Trattamento illuminante viso",
    "treatment2-liftante.jpg": "Trattamento liftante viso",
    "treatment2-antimacchia.jpg": "Trattamento anti-macchia viso",
    "treatment2-idratazione.jpg": "Armonia idratazione profonda",
    "treatment2-esfoliante.jpg": "Esfoliante viso",
    "treatment2-antieta.jpg": "Trattamento anti-età",
    "treatment2-pellisensibili.jpg": "Trattamento per pelli sensibili",
    "treatment2-contornoocchi.jpg": "Trattamento contorno occhi",
    "treatment2-laminazione-ciglia.jpg": "Laminazione ciglia prima e dopo",
    "treatment2-tatuaggio-labbra.jpg": "Tatuaggio labbra prima e dopo",
    "treatment2-tatuaggio-sopracciglia.jpg": "Tatuaggio sopracciglia",
}

with open("media_map.json") as f:
    media_map = json.load(f)

for fname in FILES:
    path = os.path.join("images", fname)
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
    media_map[fname] = {"id": media_id, "url": source_url}
    print(f"Uploaded {fname} -> id={media_id} url={source_url}")

    alt = ALT.get(fname)
    if alt:
        patch_data = json.dumps({"alt_text": alt}).encode()
        preq = urllib.request.Request(
            f"{SITE}/wp-json/wp/v2/media/{media_id}",
            data=patch_data,
            method="POST",
            headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
        )
        try:
            urllib.request.urlopen(preq)
        except urllib.error.HTTPError as e:
            print(f"  alt_text patch failed for {fname}: {e.code}")

with open("media_map.json", "w") as f:
    json.dump(media_map, f, indent=2)

print("\nDone. media_map.json updated, now", len(media_map), "entries")
