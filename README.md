# Beauty Boutique — sito WordPress

Script Python che generano il contenuto Elementor per samanthabeautyboutique.it
e lo pubblicano via REST API di WordPress (senza passare dall'editor).

## File

- `common.py` — helper condivisi (widget, colonne, sezioni, tipografia, colori)
- `site_header.py` — header condiviso tra le pagine (nav, menu mobile a panino, CSS/JS responsive)
- `gen_elementor.py` → genera `elementor_data.json` per la Home
- `gen_contatti.py` → genera `elementor_data_contatti.json` per la pagina Contatti
- `push_page.py` / `push_contatti.py` — pubblicano i JSON generati sulle rispettive pagine WordPress
- `upload_media.py` — carica le immagini in `images/` nella Libreria Media di WP
- `media_map.json` — mappa nome-file locale → id/URL media su WordPress
- `extract_images.py` — script usato una tantum per estrarre le immagini base64 dal sito di riferimento originale

## Setup

Crea un file `wp_config.py` (non versionato) con:

```python
SITE = "https://www.samanthabeautyboutique.it"
USER = "wp_xxxxxxx"
APPPW = "xxxx xxxx xxxx xxxx xxxx xxxx"  # Application Password di WordPress
```

## Uso

```bash
python3 gen_elementor.py && python3 push_page.py
python3 gen_contatti.py && python3 push_contatti.py
```

Dopo ogni push, va svuotata la cache CSS di Elementor:

```bash
curl -u "$USER:$APPPW" -X DELETE "$SITE/wp-json/elementor/v1/cache"
```

## Note tecniche

- Le pagine usano il template "Elementor Canvas" per evitare l'header/footer duplicato del tema.
- Elementor riconosce solo alcune percentuali di colonna standard (20, 25, 30, 33, 40, 50, 60, 66, 70, 75, 80, ecc.) — valori fuori da questo elenco non hanno una regola CSS di larghezza e rompono il layout.
- Un blocco `<style>`/`<script>` custom è iniettato nell'header (vedi `site_header.py`) per gli aggiustamenti responsive che i controlli nativi di Elementor non coprivano in modo affidabile.
