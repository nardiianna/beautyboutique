import re, base64, os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

out_dir = 'images'
os.makedirs(out_dir, exist_ok=True)

# Find all data URIs with some preceding context for naming
pattern = re.compile(r'(.{0,120}?)(data:image/(jpeg|png|gif|webp);base64,)([A-Za-z0-9+/=]+)')

results = []
idx = 0
for m in pattern.finditer(content):
    context = m.group(1)
    ext = 'jpg' if m.group(3) == 'jpeg' else m.group(3)
    b64data = m.group(4)
    idx += 1
    fname = f'img_{idx:02d}.{ext}'
    try:
        data = base64.b64decode(b64data)
    except Exception as e:
        print(f"skip {idx}: {e}")
        continue
    with open(os.path.join(out_dir, fname), 'wb') as out:
        out.write(data)
    results.append((fname, len(data), context.strip()[-100:]))

for r in results:
    print(r[0], r[1], 'bytes', '| context:', r[2])
