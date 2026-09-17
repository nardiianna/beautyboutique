import json
from common import *
from site_header import build_header

SECTIONS = []

NAV_ITEMS = [
    ("/#home", "Home", False),
    ("/trattamenti/", "Trattamenti", False),
    ("/il-centro/", "Il Centro", False),
    ("/#prodotti", "Prodotti", False),
    ("/contatti/", "Contatti", True),
]
header_section, mobile_panel_section = build_header(NAV_ITEMS, logo_href="/")
SECTIONS.append(header_section)
SECTIONS.append(mobile_panel_section)

# ============ HERO ============
hero_settings = sec_bg(image_fname="contatti-hero-bg.png", position="right center")
hero_settings.update(section_pad(90, 90))
hero_settings["_element_id"] = "contatti-hero"
hero_card = pad(34, 34, 34, 34)
hero_card["background_background"] = "classic"
hero_card["background_color"] = "rgba(251,246,238,.9)"
hero_card["border_radius"] = {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True}
hero_card["_element_id"] = "contatti-hero-card"

SECTIONS.append(section([
    column(60, [
        eyebrow("Contatti"),
        heading("Siamo qui<br>per te.", "h1", size=44),
        spacer(14),
        text('<div style="max-width:38ch;">Per informazioni, prenotazioni o semplicemente per una '
             'consulenza, il nostro team è a tua disposizione. Prenditi cura di te, è sempre il '
             'momento giusto.</div>',
             size=15.5, line_height=1.6),
    ], hero_card),
    column(40, []),
], hero_settings))

# ============ CONTACT INFO STRIP ============
def info_item(icon_fname, label, value, note):
    return column(33, [
        text(f'<div style="width:64px;height:64px;margin:0 auto;border-radius:50%;'
             f'background:{BG_ALT};display:flex;align-items:center;justify-content:center;">'
             f'<img src="{M[icon_fname]["url"]}" width="24" height="24" style="width:24px;height:24px;"></div>',
             align="center"),
        spacer(14),
        heading(label, "h4", size=12, weight=600, font=FONT_BODY, letter_spacing=1.4,
                transform="uppercase", color=INK_FAINT, align="center"),
        spacer(8),
        heading(value, "h3", size=18, weight=500, font=FONT_BODY, align="center"),
        spacer(8),
        text(note, size=13, align="center", line_height=1.5),
    ], {"text_align": "center", **pad(0, 30, 0, 30)})

info_settings = sec_bg(color=BG)
info_settings["_element_id"] = "contatti-info"
info_settings.update(section_pad(110, 110))
SECTIONS.append(section([
    info_item("contact-phone.png", "Telefono", "347 6524326",
               "Chiamaci per informazioni e prenotazioni"),
    info_item("contact-email.png", "Email", "samantharosellina@gmail.com",
               "Ti risponderemo il prima possibile"),
    info_item("contact-pin.png", "Dove siamo", "Via Ruzante 10, Codevigo (PD)",
               "Vieni a trovarci nel nostro centro estetico"),
], info_settings))

# ============ SCRIVICI + MAPPA ============
write_copy = [
    eyebrow("Scrivici"),
    heading("Entriamo in contatto", "h2", size=32),
    spacer(14),
    text("Scrivici su WhatsApp o via email per informazioni, consulenze o per prenotare "
         "il tuo trattamento: ti risponderemo il prima possibile.",
         size=15.5, line_height=1.6),
    spacer(20),
    widget("text-editor", {"editor": (
        '<div style="display:flex;flex-wrap:wrap;gap:14px;">'
        f'<a href="https://wa.me/393476524326" target="_blank" rel="noopener" '
        f'style="display:inline-block;background:{GOLD};color:{CREAM};font-family:\'{FONT_BODY}\',sans-serif;'
        f'font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:500;'
        f'text-decoration:none;padding:14px 26px;border-radius:4px;">Scrivici su WhatsApp →</a>'
        f'<a href="mailto:samantharosellina@gmail.com" '
        f'style="display:inline-block;background:transparent;color:{GOLD_DEEP};font-family:\'{FONT_BODY}\',sans-serif;'
        f'font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:500;'
        f'text-decoration:none;padding:14px 26px;border-radius:4px;border:1px solid {GOLD_DEEP};">Scrivi una email →</a>'
        '</div>'
    )}),
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

write_settings = sec_bg(color=BG_ALT)
write_settings["_element_id"] = "contatti-write"
write_settings.update(section_pad(90, 90))
SECTIONS.append(section([
    column(60, write_copy, {"content_position": "center"}),
    column(40, []),
], write_settings))

# ============ FOOTER (same as home) ============
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
footer_settings["_element_id"] = "footer-contatti-page"
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

with open("elementor_data_contatti.json", "w") as f:
    json.dump(SECTIONS, f)

print("Sections:", len(SECTIONS))
print("Total JSON length:", len(json.dumps(SECTIONS)))
