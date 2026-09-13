import json
from common import *
from site_header import build_header, MOBILE_CSS


SECTIONS = []

# ============ HEADER ============
NAV_ITEMS = [
    ("#home", "Home", True),
    ("#trattamenti", "Trattamenti", False),
    ("#il-centro", "Il Centro", False),
    ("#prodotti", "Prodotti", False),
    ("/contatti/", "Contatti", False),
]
header_section, mobile_panel_section = build_header(NAV_ITEMS, logo_href="#home")
SECTIONS.append(header_section)
SECTIONS.append(mobile_panel_section)

# ============ HERO ============
hero_settings = sec_bg(image_fname="hero-bg.jpg", position="right top")
hero_settings.update(section_pad(90, 90))
hero_settings["_element_id"] = "home"
hero_settings["height"] = "min-height"
hero_settings["custom_height"] = {"unit": "px", "size": 440, "sizes": []}
hero_card = pad(34, 34, 34, 34)
hero_card["background_background"] = "classic"
hero_card["background_color"] = "rgba(251,246,238,.9)"
hero_card["border_radius"] = {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True}
hero_card["_element_id"] = "hero-card"

hero_inner_card = section([
    column(100, [
        eyebrow("Il tuo momento"),
        text('<h1 style="font-family:\'Playfair Display\',serif;font-weight:600;font-size:clamp(32px,5vw,52px);'
             f'line-height:1.1;color:{INK};margin:0 0 18px;">La bellezza<br>di sentirsi bene.</h1>'),
        text("Trattamenti estetici personalizzati, per una pelle sana, luminosa e in equilibrio.",
             size=16, line_height=1.6),
        spacer(14),
        btn("Scopri i trattamenti →", "#trattamenti"),
    ], hero_card),
], {}, inner=True)

SECTIONS.append(section([
    column(50, [hero_inner_card]),
    column(50, []),
], hero_settings))

# ============ SERVICES STRIP ============
services = [
    ("icon-viso.png", "Viso", "Pulizia, trattamenti specifici e anti-età"),
    ("icon-corpo.png", "Corpo", "Rimodellamento, drenaggio, benessere"),
    ("icon-epilazione.png", "Epilazione", "Pelle liscia e luminosa a lungo"),
    ("icon-ciglia.png", "Ciglia & Sguardo", "Laminazione, tintura e cura naturale"),
    ("icon-benessere.png", "Benessere", "Massaggi e trattamenti rilassanti"),
]
svc_cols = []
for i, (icon, title, desc) in enumerate(services):
    col_settings = {"text_align": "center"}
    col_settings.update(pad(20, 16, 30, 16))
    svc_cols.append(column(20, [
        icon_box(icon, box=56),
        spacer(8),
        fixed_box(40, [heading(title, "h3", size=13, weight=600, font=FONT_BODY,
                                letter_spacing=1.2, align="center", transform="uppercase")]),
        spacer(6),
        text(desc, size=13, align="center", line_height=1.4),
    ], col_settings))
svc_settings = sec_bg(color=BG_ALT)
svc_settings.update(section_pad(60, 60))
svc_settings["_element_id"] = "services-strip"
SECTIONS.append(section(svc_cols, svc_settings))

# ============ TREATMENTS ============
trattamenti_all_link = link_arrow("Tutti i trattamenti →", align="right")
trattamenti_all_link["settings"]["_element_id"] = "trattamenti-all-link"
trattamenti_head = section([
    column(70, [eyebrow("Scegli ciò di cui hai bisogno"),
                heading("Ogni esigenza,<br>il trattamento giusto.", "h2", size=34)]),
    column(30, [trattamenti_all_link], {"content_position": "center"}),
], sec_bg(color=BG), inner=True)

treatments = [
    ("treatment-viso.jpg", "Vuoi una pelle più luminosa?", "Scopri i trattamenti viso →"),
    ("treatment-corpo.jpg", "Vuoi sentirti più leggera?", "Scopri i trattamenti corpo →"),
    ("treatment-ciglia.jpg", "Vuoi valorizzare lo sguardo?", "Ciglia e sopracciglia →"),
    ("treatment-benessere.jpg", "Vuoi rilassarti davvero?", "Scopri i trattamenti benessere →"),
]
t_cols = []
for photo, title, link_label in treatments:
    t_cols.append(column(25, [
        image_widget(photo, radius=16),
        spacer(14),
        heading(title, "h3", size=17, weight=500, font=FONT_BODY, line_height=1.4),
        spacer(6),
        link_arrow(link_label),
    ]))
trattamenti_grid = section(t_cols, {"_element_id": "trattamenti-grid"}, inner=True)

trattamenti_settings = sec_bg(color=BG)
trattamenti_settings["_element_id"] = "trattamenti"
trattamenti_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(100, [trattamenti_head, spacer(36), trattamenti_grid])
], trattamenti_settings))

# ============ IL CENTRO ============
studio_copy = [
    eyebrow("Il nostro centro"),
    heading("Un ambiente<br>pensato per te.", "h2", size=34),
    spacer(16),
    text("Ti accogliamo in un'atmosfera rilassante e curata, dove ogni dettaglio è pensato per farti "
         "sentire a tuo agio. Professionalità, ascolto e attenzione sono al centro di tutto ciò che facciamo.",
         size=15.5, line_height=1.6),
    spacer(14),
    link_arrow("Scopri il centro →"),
    spacer(22),
    text(f'<p style="font-family:\'Playfair Display\',serif;font-style:italic;font-size:18px;color:{INK};margin:0;">'
         '"Bellezza è prendersi cura di sé."</p>'
         f'<cite style="display:block;font-style:normal;font-size:11.5px;letter-spacing:.14em;'
         f'text-transform:uppercase;color:{INK_FAINT};margin-top:6px;">Samantha Crepaldi</cite>'),
]
studio_settings = sec_bg(color=BG_ALT)
studio_settings["_element_id"] = "il-centro"
studio_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(50, [image_widget("studio-centro.jpg", radius=16)]),
    column(50, studio_copy),
], studio_settings))

# ============ PRODOTTI ============
prodotti_copy = [
    eyebrow("La qualità continua a casa"),
    heading("Physio Natura<br>Cosmetici", "h2", size=34),
    spacer(16),
    text("Una linea professionale italiana che unisce natura, innovazione ed efficacia. Prodotti "
         "selezionati per prolungare i benefici dei trattamenti e prenderti cura della tua pelle ogni giorno.",
         size=15.5, line_height=1.6),
    spacer(14),
    link_arrow("Scopri i prodotti →"),
]
prodotti_settings = sec_bg(color=BG)
prodotti_settings["_element_id"] = "prodotti"
prodotti_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(40, prodotti_copy, {"content_position": "center"}),
    column(60, [image_widget("prodotti-physio.jpg", radius=16)]),
], prodotti_settings))

# ============ RISULTATI ============
results_head = section([
    column(100, [eyebrow("Risultati reali"), heading("La differenza si vede.", "h2", size=32)])
], {}, inner=True)

def result_card(photo, title, desc):
    return section([
        column(40, [image_widget(photo, radius=14)]),
        column(60, [heading(title, "h3", size=19, weight=500, font=FONT_BODY, line_height=1.3),
                    spacer(6),
                    text(desc, size=14.5, line_height=1.5)], {"content_position": "center"}),
    ], {}, inner=True)

results_cards = section([
    column(50, [result_card("result-ciglia.jpg", "Laminazione Ciglia",
                            "Uno sguardo più aperto e naturale, senza mascara.")]),
    column(50, [result_card("result-viso.jpg", "Trattamenti Viso",
                            "Pelle più luminosa, compatta e uniforme.")]),
], {"_element_id": "risultati-cards"}, inner=True)

results_settings = sec_bg(color=BG_ALT)
results_settings["_element_id"] = "risultati"
results_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(100, [results_head, spacer(36), results_cards])
], results_settings))

# ============ CTA BANNER ============
cta_settings = sec_bg(image_fname="cta-banner-bg.jpg")
cta_settings.update(section_pad(100, 100))
cta_col = {"text_align": "center", "content_position": "center"}
SECTIONS.append(section([
    column(100, [
        heading("Concediti il tuo momento.", "h2", size=34, color=CREAM, align="center"),
        spacer(10),
        text("Scrivici e scegliamo insieme il trattamento più adatto a te.",
             color="rgba(251,246,238,.88)", size=16, align="center"),
        spacer(16),
        widget("button", {
            "text": "Prenota su WhatsApp →",
            "link": {"url": "https://wa.me/393476324326", "is_external": "true"},
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

# ============ FOOTER ============
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
    + contact_row("contact-phone.png", "347 6324326")
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
    btn("Prenota ora →", "https://gestionale.nardianna.it/beauty-boutique/prenota"),
]

footer_settings = sec_bg(color=BG_ALT, image_fname="footer-flower.png", position="bottom right")
footer_settings["_element_id"] = "contatti"
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

# footer bottom bar
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
        '<a href="#" style="color:inherit;text-decoration:none;">Privacy Policy</a>'
        '<a href="#" style="color:inherit;text-decoration:none;">Cookie Policy</a>'
        '<span>Powered by <a href="https://nardianna.it" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">Nardi Creates</a></span></div>')],
           {"content_position": "center"}),
], bottom_settings))

with open("elementor_data.json", "w") as f:
    json.dump(SECTIONS, f)

print("Sections:", len(SECTIONS))
print("Total JSON length:", len(json.dumps(SECTIONS)))
