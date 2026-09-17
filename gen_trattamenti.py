import json
from common import *
from site_header import build_header

SECTIONS = []

NAV_ITEMS = [
    ("/#home", "Home", False),
    ("/trattamenti/", "Trattamenti", True),
    ("/il-centro/", "Il Centro", False),
    ("/#prodotti", "Prodotti", False),
    ("/contatti/", "Contatti", False),
]
header_section, mobile_panel_section = build_header(NAV_ITEMS, logo_href="/")
SECTIONS.append(header_section)
SECTIONS.append(mobile_panel_section)

BOOK_URL = "https://gestionale.nardianna.it/beauty-boutique/prenota"

# ============ HERO ============
hero_settings = sec_bg(image_fname="treatment2-hero-shoulder.jpg", position="right center")
hero_settings.update(section_pad(90, 90))
hero_settings["_element_id"] = "trattamenti-hero"
hero_card = pad(34, 34, 34, 34)
hero_card["background_background"] = "classic"
hero_card["background_color"] = "rgba(251,246,238,.9)"
hero_card["border_radius"] = {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True}
hero_card["_element_id"] = "trattamenti-hero-card"

SECTIONS.append(section([
    column(50, [
        eyebrow("Trattamenti"),
        heading("La tua bellezza,<br>il nostro impegno.", "h1", size=44),
        spacer(14),
        text('<div style="max-width:40ch;">Trattamenti estetici professionali, tecnologie innovative e un '
             'approccio personalizzato per farti sentire bene, ogni giorno.</div>', size=15.5, line_height=1.6),
        spacer(20),
        text(f'<span style="font-family:\'{FONT_BODY}\',sans-serif;font-size:11.5px;letter-spacing:.16em;'
             f'text-transform:uppercase;color:{INK_FAINT};border-top:1px solid {LINE};padding-top:14px;'
             f'display:inline-block;">Bellezza &middot; Benessere &middot; Armonia</span>'),
    ], hero_card),
    column(50, []),
], hero_settings))

# ============ helpers ============
def section_head(eyebrow_text, title, subtitle, right_caption=None):
    title_block = [
        eyebrow(eyebrow_text),
        text(f'<div style="display:flex;align-items:baseline;gap:18px;">'
             f'<h2 style="font-family:\'{FONT_DISPLAY}\',serif;font-weight:600;font-size:34px;color:{INK};'
             f'margin:0;">{title}</h2><span style="flex:1;height:1px;background:{LINE};'
             f'display:inline-block;margin-bottom:.5em;"></span></div>'),
        spacer(12),
        text(subtitle, size=15, line_height=1.6),
    ]
    if right_caption is None:
        return section([column(100, title_block)], {}, inner=True)
    return section([
        column(60, title_block),
        column(40, [text(f'<div style="text-align:right;font-family:\'{FONT_BODY}\',sans-serif;font-size:11.5px;'
                          f'letter-spacing:.14em;text-transform:uppercase;color:{INK_FAINT};">{right_caption}</div>',
                          align="right")], {"content_position": "center"}),
    ], {}, inner=True)

def photo_box(fname, ratio_pct=125, radius=14):
    url = M[fname]["url"]
    return text(f'<div style="width:100%;padding-top:{ratio_pct}%;position:relative;border-radius:{radius}px;'
                f'overflow:hidden;background-image:url(\'{url}\');background-size:cover;'
                f'background-position:center;"></div>')

ARROW_SVG = (f'<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="{GOLD_DEEP}" '
             f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:block;">'
             f'<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg>')

def arrow_button(url=None):
    return text(f'<a href="{url or BOOK_URL}" target="_blank" rel="noopener" style="width:30px;height:30px;'
                f'border:1px solid {GOLD_DEEP};border-radius:50%;display:inline-flex;align-items:center;'
                f'justify-content:center;">{ARROW_SVG}</a>')

def treatment_card(fname, title, subtitle, col_size=25, show_arrow=True):
    elements = [
        photo_box(fname, ratio_pct=100, radius=14),
        spacer(14),
        heading(title, "h4", size=15, weight=600, font=FONT_BODY, line_height=1.3),
        spacer(4),
        text(subtitle, size=13, line_height=1.4),
    ]
    if show_arrow:
        elements += [spacer(6), arrow_button()]
    return column(col_size, elements)

# ============ CORPO ============
corpo_head = section_head("Trattamenti", "Corpo",
                           "Ritrova la leggerezza e l'armonia del tuo corpo con trattamenti mirati ed efficaci.")
corpo_grid = section([
    treatment_card("treatment2-drenante.jpg", "Trattamento drenante", "Drenare e detossinare", show_arrow=False),
    treatment_card("treatment2-riducente.jpg", "Trattamento riducente anti gonfiore", "Riducente antigonfiore", show_arrow=False),
    treatment_card("treatment2-detox.jpg", "Advanced Body Treatment", "Riequilibrante e detossinante", show_arrow=False),
    treatment_card("treatment2-liporiducente.jpg", "Trattamento liporiducente e rimodellante", "Snellire e rimodellare", show_arrow=False),
], {"_element_id": "corpo-grid"}, inner=True)

corpo_settings = sec_bg(color=BG)
corpo_settings["_element_id"] = "trattamenti-corpo"
corpo_settings.update(section_pad(90, 50))
SECTIONS.append(section([
    column(100, [corpo_head, spacer(36), corpo_grid]),
], corpo_settings))

# ============ PRESSOTERAPIA ============
pressoterapia_head = section([
    column(100, [
        text(f'<div style="display:flex;align-items:baseline;gap:18px;">'
             f'<h2 style="font-family:\'{FONT_DISPLAY}\',serif;font-weight:600;font-size:34px;color:{INK};'
             f'margin:0;">Pressoterapia</h2><span style="flex:1;height:1px;background:{LINE};'
             f'display:inline-block;margin-bottom:.5em;"></span></div>'),
        spacer(12),
        text("Drenaggio e leggerezza che si sente.", size=15, line_height=1.6),
    ]),
], {}, inner=True)

pressoterapia_settings = sec_bg(color=BG)
pressoterapia_settings["_element_id"] = "trattamenti-pressoterapia"
pressoterapia_settings.update(section_pad(50, 90))
SECTIONS.append(section([
    column(100, [
        pressoterapia_head, spacer(32),
        section([
            column(50, [image_widget("treatment2-pressoterapia.jpg", radius=14)]),
            column(50, [
                heading("Un trattamento drenante e rilassante", "h3", size=22, weight=600, font=FONT_BODY, line_height=1.3),
                spacer(12),
                text("Una tecnologia professionale che stimola la microcircolazione e favorisce il "
                     "drenaggio linfatico, per gambe più leggere fin dalla prima seduta.",
                     size=15, line_height=1.6),
            ], {"content_position": "center"}),
        ], {}, inner=True),
    ]),
], pressoterapia_settings))

# ============ CIGLIA ============
ciglia_head = section([
    column(100, [
        text(f'<div style="display:flex;align-items:baseline;gap:18px;">'
             f'<h2 style="font-family:\'{FONT_DISPLAY}\',serif;font-weight:600;font-size:34px;color:{INK};'
             f'margin:0;">Ciglia</h2><span style="flex:1;height:1px;background:{LINE};'
             f'display:inline-block;margin-bottom:.5em;"></span></div>'),
        spacer(12),
        text("Uno sguardo più intenso, naturalmente.", size=15, line_height=1.6),
    ]),
], {}, inner=True)

ciglia_settings = sec_bg(color=BG_ALT)
ciglia_settings["_element_id"] = "trattamenti-ciglia"
ciglia_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(100, [
        ciglia_head, spacer(32),
        section([
            column(60, [image_widget("treatment2-laminazione-ciglia.jpg", radius=14)]),
            column(40, [
                heading("Laminazione ciglia", "h3", size=24, weight=600, font=FONT_BODY),
                spacer(12),
                text("Ciglia più lunghe, curve e definite, per uno sguardo naturale e luminoso.",
                     size=15, line_height=1.6),
            ], {"content_position": "center"}),
        ], {}, inner=True),
    ]),
], ciglia_settings))

# ============ TRUCCO PERMANENTE ============
trucco_head = section([
    column(60, [
        text(f'<div style="display:flex;align-items:baseline;gap:18px;">'
             f'<h2 style="font-family:\'{FONT_DISPLAY}\',serif;font-weight:600;font-size:34px;color:{INK};'
             f'margin:0;">Trucco Permanente</h2><span style="flex:1;height:1px;background:{LINE};'
             f'display:inline-block;margin-bottom:.5em;"></span></div>'),
    ]),
    column(40, [text(f'<div style="text-align:right;font-family:\'{FONT_BODY}\',sans-serif;font-size:11.5px;'
                      f'letter-spacing:.14em;text-transform:uppercase;color:{INK_FAINT};">'
                      'Bellezza che resta,<br>ogni giorno</div>', align="right")],
           {"content_position": "center"}),
], {}, inner=True)

trucco_settings = sec_bg(color=BG)
trucco_settings["_element_id"] = "trattamenti-trucco"
trucco_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(100, [
        trucco_head, spacer(32),
        section([
            column(50, [
                photo_box("treatment2-tatuaggio-labbra-dopo.jpg", ratio_pct=52, radius=14),
                spacer(14),
                heading("Tatuaggio labbra", "h4", size=17, weight=600, font=FONT_BODY),
                spacer(4),
                text("Colore, definizione e armonia per labbra sempre perfette.", size=14, line_height=1.5),
            ]),
            column(50, [
                photo_box("treatment2-tatuaggio-sopracciglia.jpg", ratio_pct=52, radius=14),
                spacer(14),
                heading("Tatuaggio sopracciglia", "h4", size=17, weight=600, font=FONT_BODY),
                spacer(4),
                text("Forma e intensità per uno sguardo più definito.", size=14, line_height=1.5),
            ]),
        ], {"_element_id": "trucco-grid"}, inner=True),
    ]),
], trucco_settings))

# ============ TRATTAMENTI VISO ============
viso_head = section_head("Trattamenti", "Trattamenti Viso",
                          "Soluzioni mirate per ogni esigenza della tua pelle.",
                          "Una pelle più sana,<br>luminosa, autentica")

viso_treatments = [
    ("treatment2-illuminante.jpg", "Trattamento illuminante viso", "Illuminante e uniformante"),
    ("treatment2-liftante.jpg", "Trattamento liftante viso", "Liftante"),
    ("treatment2-antimacchia.jpg", "Trattamento anti-macchia viso", "Schiarente"),
    ("treatment2-idratazione.jpg", "Armonia idratazione profonda", "Idratante"),
    ("treatment2-esfoliante.jpg", "Esfoliante viso", "Esfoliazione e rinnovamento cutaneo"),
    ("treatment2-antieta.jpg", "Trattamento anti-età", "Anti-età"),
    ("treatment2-pellisensibili.jpg", "Pelli sensibili", "Lenitivo"),
    ("treatment2-contornoocchi.jpg", "Trattamento contorno occhi", "Idratante, drenante, distensivo"),
]
viso_row1 = section([treatment_card(f, t, s, show_arrow=False) for f, t, s in viso_treatments[:4]],
                     {"_element_id": "viso-grid-row1"}, inner=True)
viso_row2 = section([treatment_card(f, t, s, show_arrow=False) for f, t, s in viso_treatments[4:]],
                     {"_element_id": "viso-grid-row2"}, inner=True)

viso_settings = sec_bg(color=BG_ALT)
viso_settings["_element_id"] = "trattamenti-viso"
viso_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(100, [viso_head, spacer(36), viso_row1, spacer(36), viso_row2]),
], viso_settings))

# ============ CTA BANNER ============
cta_settings = sec_bg(image_fname="cta-banner-bg.jpg")
cta_settings["_element_id"] = "trattamenti-cta"
cta_settings.update(section_pad(100, 100))
cta_col = {"text_align": "center", "content_position": "center"}
SECTIONS.append(section([
    column(100, [
        heading("Prenditi cura di te.", "h2", size=34, color=CREAM, align="center"),
        spacer(10),
        text("Prenota il tuo trattamento e lasciati guidare dal nostro team.",
             color="rgba(251,246,238,.88)", size=16, align="center"),
        spacer(16),
        widget("button", {
            "text": "Prenota ora →",
            "link": {"url": BOOK_URL, "is_external": "true"},
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
    html_button("Prenota ora →", BOOK_URL, align="left"),
]

footer_settings = sec_bg(color=BG_ALT, image_fname="footer-flower.png", position="bottom right")
footer_settings["_element_id"] = "footer-trattamenti-page"
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
TRATTAMENTI_CSS = """<style>
@media (max-width: 900px) {
  #corpo-grid > .elementor-container, #viso-grid-row1 > .elementor-container, #viso-grid-row2 > .elementor-container{flex-wrap:wrap;}
  #corpo-grid .elementor-column, #viso-grid-row1 .elementor-column, #viso-grid-row2 .elementor-column{width:50%!important;margin-bottom:28px;}
  #trucco-grid > .elementor-container{flex-wrap:wrap;}
  #trucco-grid .elementor-column{width:100%!important;margin-bottom:28px;}
}
@media (max-width: 767px) {
  #corpo-grid .elementor-column, #viso-grid-row1 .elementor-column, #viso-grid-row2 .elementor-column{width:100%!important;}
  #trattamenti-hero .elementor-column:last-child{display:none;}
}
</style>"""
SECTIONS[0]["elements"][0]["elements"].append(widget("text-editor", {"editor": TRATTAMENTI_CSS}))

with open("elementor_data_trattamenti.json", "w") as f:
    json.dump(SECTIONS, f)

print("Sections:", len(SECTIONS))
print("Total JSON length:", len(json.dumps(SECTIONS)))
