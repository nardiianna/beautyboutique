import base64, json, urllib.request
from wp_config import SITE, USER, APPPW

PAGE_ID = 47

auth = base64.b64encode(f"{USER}:{APPPW}".encode()).decode()

with open("elementor_data_contatti.json") as f:
    sections = json.load(f)

elementor_data_str = json.dumps(sections, separators=(",", ":"))

payload = {
    "title": "Contatti",
    "status": "publish",
    "template": "elementor_canvas",
    "meta": {
        "_elementor_data": elementor_data_str,
        "_elementor_edit_mode": "builder",
        "_elementor_template_type": "wp-page",
        "_elementor_version": "3.24.0",
    },
}

data = json.dumps(payload).encode()

req = urllib.request.Request(
    f"{SITE}/wp-json/wp/v2/pages/{PAGE_ID}",
    data=data,
    method="POST",
    headers={
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/json",
    },
)

try:
    with urllib.request.urlopen(req) as resp:
        body = json.loads(resp.read().decode())
        print("OK:", body.get("id"), body.get("status"), body.get("link"))
except urllib.error.HTTPError as e:
    print("FAILED:", e.code)
    print(e.read().decode()[:2000])
