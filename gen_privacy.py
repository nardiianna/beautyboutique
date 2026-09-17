import json
from common import *
from site_header import build_header

SECTIONS = []

NAV_ITEMS = [
    ("/#home", "Home", False),
    ("/trattamenti/", "Trattamenti", False),
    ("/il-centro/", "Il Centro", False),
    ("/#prodotti", "Prodotti", False),
    ("/contatti/", "Contatti", False),
]
header_section, mobile_panel_section = build_header(NAV_ITEMS, logo_href="/")
SECTIONS.append(header_section)
SECTIONS.append(mobile_panel_section)

# ============ HERO ============
hero_settings = sec_bg(color=BG_ALT)
hero_settings.update(section_pad(70, 50))
hero_settings["_element_id"] = "privacy-hero"

SECTIONS.append(section([
    column(100, [
        eyebrow("Informazioni legali"),
        heading("Privacy Policy", "h1", size=40),
        spacer(10),
        text('<div style="max-width:60ch;">Informativa sul trattamento dei dati personali ai sensi '
             'del Regolamento (UE) 2016/679 (GDPR).</div>', size=15, line_height=1.6),
    ], {"content_position": "center"}),
], hero_settings))

# ============ POLICY BODY ============
def policy_heading(txt):
    return heading(txt, "h3", size=20, weight=600, font=FONT_BODY)

def policy_text(html):
    return text(html, size=15, line_height=1.75)

def policy_list(items):
    html = '<ul style="margin:0;padding-left:20px;">' + "".join(f'<li style="margin-bottom:6px;">{i}</li>' for i in items) + '</ul>'
    return text(html, size=15, line_height=1.75)

body = [
    policy_heading("Titolare del trattamento"),
    spacer(10),
    policy_text(
        "Il Titolare del trattamento dei dati personali raccolti tramite questo sito web è "
        "<strong>Samantha Crepaldi</strong>, con sede in Via Ruzante 10, Codevigo (PD), "
        "Codice Fiscale CRPSNT89R51G693E. Per qualsiasi informazione relativa al trattamento dei "
        "dati personali è possibile contattare il Titolare all'indirizzo email "
        "<a href=\"mailto:samantharosellina@gmail.com\">samantharosellina@gmail.com</a> o al numero "
        "di telefono +39 347 6524326."
    ),
    spacer(36),

    policy_heading("Dati di navigazione"),
    spacer(10),
    policy_text(
        "I sistemi informatici e le procedure software preposte al funzionamento di questo sito web "
        "acquisiscono, nel corso del loro normale esercizio, alcuni dati personali la cui trasmissione "
        "è implicita nell'uso dei protocolli di comunicazione di Internet (ad esempio indirizzi IP, tipo "
        "di browser, sistema operativo, nomi di dominio dei siti utilizzati). Questi dati vengono "
        "utilizzati al solo fine di ricavare informazioni statistiche anonime sull'uso del sito e per "
        "controllarne il corretto funzionamento."
    ),
    spacer(36),

    policy_heading("Dati forniti volontariamente"),
    spacer(10),
    policy_text(
        "L'invio facoltativo, esplicito e volontario di messaggi tramite WhatsApp, email o telefono agli "
        "indirizzi di contatto indicati sul sito comporta la successiva acquisizione dell'indirizzo del "
        "mittente, necessario per rispondere alle richieste, nonché degli eventuali altri dati personali "
        "inseriti nel messaggio (ad esempio nome e recapiti)."
    ),
    spacer(36),

    policy_heading("Finalità e base giuridica del trattamento"),
    spacer(10),
    policy_text("I dati personali forniti volontariamente vengono trattati per le seguenti finalità:"),
    spacer(8),
    policy_list([
        "rispondere a richieste di informazioni, consulenze o prenotazioni;",
        "gestire il rapporto precontrattuale e contrattuale con la clientela.",
    ]),
    spacer(8),
    policy_text(
        "La base giuridica del trattamento è l'esecuzione di misure precontrattuali adottate su richiesta "
        "dell'interessato (art. 6.1.b GDPR) e, ove applicabile, il consenso dell'interessato (art. 6.1.a GDPR)."
    ),
    spacer(36),

    policy_heading("Prenotazioni tramite piattaforma esterna"),
    spacer(10),
    policy_text(
        "Le prenotazioni dei trattamenti avvengono tramite una piattaforma gestionale esterna "
        "(gestionale.nardianna.it), che opera come autonomo titolare del trattamento per i dati inseriti "
        "in fase di prenotazione. Si invita a consultare l'informativa privacy specifica della piattaforma "
        "di prenotazione."
    ),
    spacer(36),

    policy_heading("Servizi di terze parti"),
    spacer(10),
    policy_text("Questo sito utilizza i seguenti servizi forniti da soggetti terzi:"),
    spacer(8),
    policy_list([
        "<strong>Google Fonts</strong> (Google Ireland Limited): per la visualizzazione dei caratteri "
        "tipografici del sito vengono caricati font dai server di Google;",
        "<strong>WhatsApp</strong> e <strong>Instagram</strong> (Meta Platforms Ireland Limited): il sito "
        "include collegamenti diretti a questi servizi esterni, il cui utilizzo è soggetto alle rispettive "
        "informative privacy.",
    ]),
    spacer(8),
    policy_text(
        "Questo sito non utilizza attualmente cookie di profilazione né strumenti di analisi statistica di "
        "terze parti (es. Google Analytics)."
    ),
    spacer(36),

    policy_heading("Cookie"),
    spacer(10),
    policy_text(
        "Il sito utilizza esclusivamente cookie tecnici necessari al funzionamento della piattaforma "
        "WordPress e dell'editor Elementor, che non richiedono consenso preventivo ai sensi della normativa "
        "vigente. Non vengono utilizzati cookie di profilazione."
    ),
    spacer(36),

    policy_heading("Conservazione dei dati"),
    spacer(10),
    policy_text(
        "I dati personali forniti volontariamente per rispondere a richieste vengono conservati per il "
        "tempo necessario a soddisfare la richiesta stessa e comunque non oltre 24 mesi, salvo obblighi di "
        "legge che richiedano una conservazione più lunga."
    ),
    spacer(36),

    policy_heading("Diritti dell'interessato"),
    spacer(10),
    policy_text(
        "In qualità di interessato, hai diritto di ottenere in qualsiasi momento, ai sensi degli articoli "
        "15-22 del Regolamento (UE) 2016/679 (GDPR):"
    ),
    spacer(8),
    policy_list([
        "l'accesso ai tuoi dati personali;",
        "la rettifica o la cancellazione degli stessi;",
        "la limitazione del trattamento;",
        "l'opposizione al trattamento;",
        "la portabilità dei dati.",
    ]),
    spacer(8),
    policy_text(
        "Hai inoltre diritto di proporre reclamo all'Autorità Garante per la protezione dei dati personali "
        "(<a href=\"https://www.garanteprivacy.it\" target=\"_blank\" rel=\"noopener\">www.garanteprivacy.it</a>) "
        "qualora ritenga che il trattamento dei tuoi dati violi la normativa vigente."
    ),
    spacer(36),

    policy_heading("Modifiche alla presente informativa"),
    spacer(10),
    policy_text(
        "Il Titolare si riserva di modificare o aggiornare, in tutto o in parte, la presente informativa, "
        "dandone comunicazione tramite pubblicazione sul sito. Si consiglia di consultare periodicamente "
        "questa pagina."
    ),
    spacer(36),

    policy_heading("Contatti"),
    spacer(10),
    policy_text(
        "Per qualsiasi richiesta relativa al trattamento dei tuoi dati personali puoi contattare il "
        "Titolare all'indirizzo <a href=\"mailto:samantharosellina@gmail.com\">samantharosellina@gmail.com</a>."
    ),
    spacer(24),
    text('<span style="font-size:13px;">Ultimo aggiornamento: settembre 2026.</span>', color=INK_FAINT),
]

body_settings = sec_bg(color=BG)
body_settings["_element_id"] = "privacy-body"
body_settings.update(section_pad(60, 100))

SECTIONS.append(section([
    column(70, body, {}),
    column(30, []),
], body_settings))

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
footer_settings["_element_id"] = "footer-privacy-page"
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

with open("elementor_data_privacy.json", "w") as f:
    json.dump(SECTIONS, f)

print("Sections:", len(SECTIONS))
print("Total JSON length:", len(json.dumps(SECTIONS)))
