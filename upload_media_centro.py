import base64, json, mimetypes, os, urllib.request
from wp_config import SITE, USER, APPPW

auth = base64.b64encode(f"{USER}:{APPPW}".encode()).decode()

FILES = [
    "centro-reception.jpg",
    "centro-angolo-verde.jpg",
    "centro-scaffale-prodotti.jpg",
    "centro-cabina-trattamenti.jpg",
    "centro-sterilizzatore-1.jpg",
    "centro-sterilizzatore-2.jpg",
    "centro-insegna.jpg",
    "centro-postazione-unghie.jpg",
]

ALT = {
    "centro-reception.jpg": "Reception del centro estetico Beauty Boutique",
    "centro-angolo-verde.jpg": "Angolo relax del centro estetico Beauty Boutique",
    "centro-scaffale-prodotti.jpg": "Scaffale prodotti Physio Natura in vetrina",
    "centro-cabina-trattamenti.jpg": "Cabina trattamenti viso e corpo",
    "centro-sterilizzatore-1.jpg": "Sterilizzatore medicale per strumenti estetici",
    "centro-sterilizzatore-2.jpg": "Sterilizzatore medicale per strumenti estetici",
    "centro-insegna.jpg": "Insegna Beauty Boutique Centro Estetico all'ingresso",
    "centro-postazione-unghie.jpg": "Postazione manicure del centro estetico",
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
