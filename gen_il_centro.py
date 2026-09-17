import json
from common import *
from site_header import build_header

SECTIONS = []

NAV_ITEMS = [
    ("/#home", "Home", False),
    ("/trattamenti/", "Trattamenti", False),
    ("/il-centro/", "Il Centro", True),
    ("/#prodotti", "Prodotti", False),
    ("/contatti/", "Contatti", False),
]
header_section, mobile_panel_section = build_header(NAV_ITEMS, logo_href="/")
SECTIONS.append(header_section)
SECTIONS.append(mobile_panel_section)

# ============ HERO ============
hero_settings = sec_bg(image_fname="centro-hero-slider.jpg", position="right center")
hero_settings.update(section_pad(90, 90))
hero_settings["_element_id"] = "centro-hero"
hero_card = pad(34, 34, 34, 34)
hero_card["background_background"] = "classic"
hero_card["background_color"] = "rgba(251,246,238,.9)"
hero_card["border_radius"] = {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True}
hero_card["_element_id"] = "centro-hero-card"

SECTIONS.append(section([
    column(60, [
        eyebrow("Il Centro"),
        heading("Un ambiente<br>pensato per te.", "h1", size=44),
        spacer(14),
        text('<div style="max-width:40ch;">Un luogo dove bellezza, benessere e professionalità si incontrano. '
             'Ti accogliamo in un\'atmosfera curata e rilassante, pensata nei minimi dettagli per farti sentire '
             'a tuo agio.</div>', size=15.5, line_height=1.6),
        spacer(20),
        text(f'<span style="font-family:\'{FONT_BODY}\',sans-serif;font-size:11.5px;letter-spacing:.16em;'
             f'text-transform:uppercase;color:{INK_FAINT};border-top:1px solid {LINE};padding-top:14px;'
             f'display:inline-block;">Bellezza &middot; Benessere &middot; Armonia</span>'),
    ], hero_card),
    column(40, []),
], hero_settings))

# ============ UN'ESPERIENZA DI BENESSERE ============
# Inline SVGs (24x24, stroke-based line icons) so icons render without depending
# on Font Awesome, which this site never loads (no Elementor "icon" widgets used).
ICONS = {
    "leaf": '<path d="M11 20a7 7 0 0 1-7-7V7a1 1 0 0 1 1-1h6a7 7 0 0 1 0 14z"/><path d="M4 13h7"/>',
    "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.8 1-1a5.5 5.5 0 0 0 0-7.8z"/>',
    "sparkle": '<path d="M12 2.5l1.8 5.7L19.5 10l-5.7 1.8L12 17.5l-1.8-5.7L4.5 10l5.7-1.8z"/>',
    "door": '<path d="M3.5 11L12 4l8.5 7"/><path d="M5.5 9.8V20h13V9.8"/>',
    "droplet": '<path d="M12 2.5S5.5 11 5.5 15.5a6.5 6.5 0 0 0 13 0C18.5 11 12 2.5 12 2.5z"/>',
}

def svg_icon(name, size=16, color=None, stroke=1.6, filled=False):
    fill = color or "none"
    stroke_attr = "none" if filled else (color or "currentColor")
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{fill if filled else "none"}" '
            f'stroke="{stroke_attr}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round" '
            f'style="display:block;">{ICONS[name]}</svg>')

def checklist_item(icon_name, label):
    return text(
        f'<div style="display:flex;align-items:center;gap:12px;">'
        f'<span style="color:{GOLD};width:18px;flex:none;">{svg_icon(icon_name, 16)}</span>'
        f'<span style="font-family:\'{FONT_BODY}\',sans-serif;font-size:14.5px;color:{INK_SOFT};">{label}</span></div>'
    )

esperienza_copy = [
    eyebrow("Più di un centro estetico"),
    heading("Un'esperienza<br>di benessere", "h2", size=34),
    spacer(16),
    text("Atmosfera rilassante, ambienti curati e un team sempre attento alle tue esigenze. Ogni spazio "
         "del nostro centro è pensato per offrirti un'esperienza piacevole, in cui ti sentirai ascoltata, "
         "seguita e valorizzata.", size=15.5, line_height=1.6),
    spacer(20),
    checklist_item("leaf", "Un ambiente accogliente"),
    spacer(12),
    checklist_item("heart", "Professionalità e ascolto"),
    spacer(12),
    checklist_item("sparkle", "Attenzione ad ogni dettaglio"),
]
esperienza_settings = sec_bg(color=BG_ALT)
esperienza_settings["_element_id"] = "centro-esperienza"
esperienza_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(50, [image_widget("centro-angolo-verde.jpg", radius=16)]),
    column(50, esperienza_copy, {"content_position": "center"}),
], esperienza_settings))

# ============ UNO SGUARDO ALL'INTERNO ============
galleria_head = section([
    column(100, [
        eyebrow("Il nostro centro"),
        heading("Uno sguardo<br>all'interno", "h2", size=34),
        spacer(14),
        text("Scopri gli spazi dove prendiamo cura di te, ogni giorno.", size=15.5, line_height=1.6),
    ]),
], {}, inner=True)

def photo_box(fname, ratio_pct=125, radius=14):
    url = M[fname]["url"]
    return text(f'<div style="width:100%;padding-top:{ratio_pct}%;position:relative;border-radius:{radius}px;'
                f'overflow:hidden;background-image:url(\'{url}\');background-size:cover;'
                f'background-position:center;"></div>')

galleria_grid = section([
    column(25, [photo_box("centro-cabina-trattamenti.jpg")]),
    column(25, [photo_box("centro-insegna.jpg")]),
    column(25, [photo_box("centro-scaffale-prodotti.jpg")]),
    column(25, [photo_box("centro-postazione-unghie.jpg")]),
], {"_element_id": "centro-galleria-grid"}, inner=True)

galleria_settings = sec_bg(color=BG)
galleria_settings["_element_id"] = "centro-galleria"
galleria_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(100, [galleria_head, spacer(36), galleria_grid]),
], galleria_settings))

# ============ SPAZI PENSATI PER IL TUO BENESSERE ============
spazi_head = section([
    column(100, [heading("Spazi pensati per il tuo benessere", "h2", size=30, align="center")]),
], {}, inner=True)

def spazio_item(icon_name, title, desc):
    return column(33, [
        text(f'<div style="display:flex;justify-content:center;color:{GOLD_DEEP};">{svg_icon(icon_name, 30, stroke=1.4)}</div>',
             align="center"),
        spacer(16),
        heading(title, "h4", size=13, weight=600, font=FONT_BODY, letter_spacing=1.3,
                transform="uppercase", color=INK, align="center"),
        spacer(10),
        text(desc, size=13.5, align="center", line_height=1.55),
    ], {"text_align": "center", **pad(0, 30, 0, 30)})

spazi_grid = section([
    spazio_item("door", "Accoglienza",
                "Ti diamo il benvenuto in un ambiente caldo e rilassante, dove sentirti subito a tuo agio."),
    spazio_item("droplet", "Trattamenti",
                "Cabine curate e attrezzate per offrirti trattamenti viso e corpo in totale comfort e privacy."),
    spazio_item("sparkle", "Cura dei dettagli",
                "Ogni elemento, dall'arredo alla luce, è scelto per creare un'atmosfera armoniosa e piacevole."),
], {"_element_id": "centro-spazi-grid"}, inner=True)

spazi_settings = sec_bg(color=BG_ALT)
spazi_settings["_element_id"] = "centro-spazi"
spazi_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(100, [spazi_head, spacer(40), spazi_grid]),
], spazi_settings))

# ============ TECNOLOGIA ============
tecnologia_copy = [
    eyebrow("Tecnologia al servizio della tua bellezza"),
    heading("Strumenti professionali<br>per risultati su misura", "h2", size=32),
    spacer(16),
    text("Utilizziamo apparecchiature professionali di ultima generazione per supportare i nostri trattamenti "
         "estetici e offrirti percorsi personalizzati, efficaci e sicuri. La tecnologia si unisce alla nostra "
         "esperienza per valorizzare la tua bellezza naturale.", size=15.5, line_height=1.6),
    spacer(20),
    btn("Scopri i trattamenti →", "/trattamenti/"),
]
tecnologia_settings = sec_bg(color=BG)
tecnologia_settings["_element_id"] = "centro-tecnologia"
tecnologia_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(40, [photo_box("centro-sterilizzatore-2.jpg", ratio_pct=100, radius=16)]),
    column(60, tecnologia_copy, {"content_position": "center"}),
], tecnologia_settings))

# ============ PRODOTTI ============
prodotti_copy = [
    eyebrow("Qualità anche nei dettagli"),
    heading("Prodotti di eccellenza", "h2", size=32),
    spacer(16),
    text("Nel nostro centro trovi una selezione di prodotti professionali, come la linea Physio Natura, "
         "scelti per la loro qualità e attenzione alla pelle. Ti consigliamo i prodotti più adatti alle tue "
         "esigenze, anche per la tua beauty routine a casa.", size=15.5, line_height=1.6),
    spacer(20),
    btn("Scopri i prodotti →", "/#prodotti"),
]
prodotti_settings = sec_bg(color=BG_ALT)
prodotti_settings["_element_id"] = "centro-prodotti"
prodotti_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(60, prodotti_copy, {"content_position": "center"}),
    column(40, [image_widget("studio-centro.jpg", radius=16)]),
], prodotti_settings))

# ============ CTA BANNER ============
cta_settings = sec_bg(image_fname="cta-banner-bg.jpg")
cta_settings["_element_id"] = "centro-cta"
cta_settings.update(section_pad(100, 100))
cta_col = {"text_align": "center", "content_position": "center"}
SECTIONS.append(section([
    column(100, [
        heading("Concediti il tuo momento.", "h2", size=34, color=CREAM, align="center"),
        spacer(10),
        text("Prenota il tuo trattamento e vivi un'esperienza di benessere su misura.",
             color="rgba(251,246,238,.88)", size=16, align="center"),
        spacer(16),
        widget("button", {
            "text": "Prenota ora →",
            "link": {"url": "https://gestionale.nardianna.it/beauty-boutique/prenota", "is_external": "true"},
            "align": "center",
            "background_color": "transparent",
            "button_text_color": CREAM,
            "border_border": "solid",
            "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
            "border_color": "rgba(251,246,238,.55)",
            "border_radius": {"unit": "px", "top": "4", "right": "4", "bottom": "4", "left": "4", "isLinked": True},
            "text_padding": {"unit": "px", "top": "14", "right": "26", "bottom": "14", "left": "26", "isLinked": False},
            **typo(FONT_BODY, size=12.5, weight=500, letter_spacing=1, transform="uppercase"),
        }),
    ], cta_col),
], cta_settings))

# ============ FOOTER (same as other pages) ============
def social_icon(fname, url="#"):
    return (f'<a href="{url}" target="_blank" rel="noopener" style="width:34px;height:34px;'
            f'border:1px solid {LINE};border-radius:50%;'
            f'display:inline-flex;align-items:center;justify-content:center;">'
            f'<img src="{M[fname]["url"]}" width="15" height="15" style="width:15px;height:15px;'
            f'display:block;"></a>')

social_row = text(
    f'<div id="footer-social-row" style="display:flex;gap:12px;">'
    f'{social_icon("social-instagram.png", "https://www.instagram.com/beauty_boutique.sc/")}'
    f'</div>'
)

footer_brand = [
    image_widget("logo-footer.png", width_px=150),
    spacer(16),
    text("Bellezza, benessere e amore per sé stessi.", size=14, line_height=1.5),
    spacer(18),
    social_row,
]

hours_html = (
    '<ul style="list-style:none;margin:0;padding:0;font-size:13.5px;">' +
    "".join(
        f'<li style="display:flex;justify-content:space-between;gap:18px;padding:5px 0;">'
        f'<span style="color:{INK};flex:none;">{day}</span>'
        f'<span style="color:{INK_FAINT if closed else INK_SOFT};font-style:{"italic" if closed else "normal"};'
        f'flex:1;text-align:right;">{hrs}</span></li>'
        for day, hrs, closed in [
            ("Lunedì", "08:30 – 15:00", False),
            ("Martedì", "08:30–13:00 / 15:00–19:30", False),
            ("Mercoledì", "Chiuso", True),
            ("Giovedì", "08:30–13:00 / 15:00–19:30", False),
            ("Venerdì", "08:30–13:00 / 15:00–20:00", False),
            ("Sabato", "08:30 – 16:00", False),
        ]
    ) + "</ul>"
)
footer_hours = [
    heading("Orari di apertura", "h4", size=12, weight=600, font=FONT_BODY, letter_spacing=1.4,
            transform="uppercase", color=INK_FAINT),
    spacer(28),
    text(hours_html),
]

def contact_row(icon_fname, label):
    url = M[icon_fname]["url"]
    return (f'<li style="display:flex;align-items:center;gap:10px;">'
            f'<img src="{url}" width="16" height="16" style="width:16px;height:16px;flex:none;display:block;">'
            f'<span>{label}</span></li>')

contact_html = (
    f'<ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:20px;'
    f'font-size:14px;color:{INK_SOFT};">'
    + contact_row("contact-phone.png", "347 6524326")
    + contact_row("contact-pin.png", "Via Ruzante 10, Codevigo (PD)")
    + contact_row("contact-instagram.png", "beauty_boutique.sc")
    + '</ul>'
)
footer_contact = [
    heading("Contatti", "h4", size=12, weight=600, font=FONT_BODY, letter_spacing=1.4,
            transform="uppercase", color=INK_FAINT),
    spacer(28),
    text(contact_html),
    spacer(18),
    html_button("Prenota ora →", "https://gestionale.nardianna.it/beauty-boutique/prenota", align="left"),
]

footer_settings = sec_bg(color=BG_ALT, image_fname="footer-flower.png", position="bottom right")
footer_settings["_element_id"] = "footer-il-centro-page"
footer_settings["background_repeat"] = "no-repeat"
footer_settings["background_size"] = "custom"
footer_settings["background_bg_width"] = {"unit": "px", "size": 300, "sizes": []}
footer_settings["border_border"] = "solid"
footer_settings["border_width"] = {"unit": "px", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False}
footer_settings["border_color"] = LINE
footer_settings.update(section_pad(80, 44))
footer_settings["gap"] = "custom"
footer_settings["gap_columns_custom"] = {"unit": "px", "size": 50, "sizes": []}

SECTIONS.append(section([
    column(30, footer_brand, pad(0, 30, 0, 0)),
    column(30, footer_hours, pad(0, 20, 0, 20)),
    column(40, footer_contact, pad(0, 0, 0, 20)),
], footer_settings))

bottom_settings = sec_bg(color=BG_ALT)
bottom_settings["border_border"] = "solid"
bottom_settings["border_width"] = {"unit": "px", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False}
bottom_settings["border_color"] = LINE
bottom_settings.update(pad(18, 20, 18, 20))

SECTIONS.append(section([
    column(60, [text(f'<span style="font-size:12.5px;color:{INK_FAINT};">'
                      '© 2026 Beauty Boutique – Centro Estetico. Tutti i diritti riservati.</span>')],
           {"content_position": "center"}),
    column(40, [text(
        f'<div style="display:flex;gap:18px;align-items:center;justify-content:flex-end;font-size:12.5px;color:{INK_FAINT};">'
        '<a href="/privacy-policy/" style="color:inherit;text-decoration:none;">Privacy Policy</a>'
        '<a href="/cookie-policy/" style="color:inherit;text-decoration:none;">Cookie Policy</a>'
        '<span>Powered by <a href="https://nardianna.it" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">Nardi Creates</a></span></div>')],
           {"content_position": "center"}),
], bottom_settings))

# ============ RESPONSIVE CSS ============
IL_CENTRO_CSS = """<style>
@media (max-width: 900px) {
  #centro-galleria-grid > .elementor-container{flex-wrap:wrap;}
  #centro-galleria-grid .elementor-column{width:50%!important;margin-bottom:20px;}
}
@media (max-width: 560px) {
  #centro-galleria-grid .elementor-column{width:100%!important;}
}
@media (max-width: 767px) {
  #centro-spazi-grid > .elementor-container{flex-wrap:wrap;}
  #centro-spazi-grid .elementor-column{width:100%!important;padding-bottom:28px!important;border-bottom:1px solid #E3D3B6;margin-bottom:14px;}
  #centro-spazi-grid .elementor-column:last-child{border-bottom:none;}
  #centro-hero .elementor-column:last-child{display:none;}
}
</style>"""
SECTIONS[0]["elements"][0]["elements"].append(widget("text-editor", {"editor": IL_CENTRO_CSS}))

with open("elementor_data_il_centro.json", "w") as f:
    json.dump(SECTIONS, f)

print("Sections:", len(SECTIONS))
print("Total JSON length:", len(json.dumps(SECTIONS)))
