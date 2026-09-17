import base64, json, urllib.request
from wp_config import SITE, USER, APPPW

auth = base64.b64encode(f"{USER}:{APPPW}".encode()).decode()
HEADERS = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}

with open("elementor_data_trattamenti.json") as f:
    sections = json.load(f)

elementor_data_str = json.dumps(sections, separators=(",", ":"))

payload = {
    "title": "Trattamenti",
    "slug": "trattamenti",
    "status": "publish",
    "template": "elementor_canvas",
    "meta": {
        "_elementor_data": elementor_data_str,
        "_elementor_edit_mode": "builder",
        "_elementor_template_type": "wp-page",
        "_elementor_version": "3.24.0",
    },
}

lookup_req = urllib.request.Request(
    f"{SITE}/wp-json/wp/v2/pages?slug=trattamenti&status=any",
    headers={"Authorization": f"Basic {auth}"},
)
with urllib.request.urlopen(lookup_req) as resp:
    existing = json.loads(resp.read().decode())

page_id = existing[0]["id"] if existing else None
url = f"{SITE}/wp-json/wp/v2/pages/{page_id}" if page_id else f"{SITE}/wp-json/wp/v2/pages"

data = json.dumps(payload).encode()
req = urllib.request.Request(url, data=data, method="POST", headers=HEADERS)

try:
    with urllib.request.urlopen(req) as resp:
        body = json.loads(resp.read().decode())
        print("OK:", body.get("id"), body.get("status"), body.get("link"))
except urllib.error.HTTPError as e:
    print("FAILED:", e.code)
    print(e.read().decode()[:2000])
