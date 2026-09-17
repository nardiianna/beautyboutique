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
hero_settings["_element_id"] = "cookie-hero"

SECTIONS.append(section([
    column(100, [
        eyebrow("Informazioni legali"),
        heading("Cookie Policy", "h1", size=40),
        spacer(10),
        text('<div style="max-width:60ch;">Informativa sull\'utilizzo dei cookie su questo sito web, '
             'ai sensi del Regolamento (UE) 2016/679 (GDPR) e del Provvedimento del Garante Privacy '
             'sui cookie.</div>', size=15, line_height=1.6),
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

def policy_table(rows):
    head = ('<tr>'
            '<th style="text-align:left;padding:10px 12px;border-bottom:2px solid ' + LINE + ';">Nome</th>'
            '<th style="text-align:left;padding:10px 12px;border-bottom:2px solid ' + LINE + ';">Finalità</th>'
            '<th style="text-align:left;padding:10px 12px;border-bottom:2px solid ' + LINE + ';">Durata</th>'
            '</tr>')
    body_rows = "".join(
        '<tr>'
        f'<td style="padding:10px 12px;border-bottom:1px solid {LINE};font-family:monospace;font-size:13px;">{name}</td>'
        f'<td style="padding:10px 12px;border-bottom:1px solid {LINE};">{purpose}</td>'
        f'<td style="padding:10px 12px;border-bottom:1px solid {LINE};">{duration}</td>'
        '</tr>'
        for name, purpose, duration in rows
    )
    html = f'<div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;font-size:14px;">{head}{body_rows}</table></div>'
    return text(html, size=14, line_height=1.6)

body = [
    policy_heading("Cosa sono i cookie"),
    spacer(10),
    policy_text(
        "I cookie sono piccoli file di testo che i siti visitati inviano al browser dell'utente, dove "
        "vengono memorizzati per essere poi ritrasmessi agli stessi siti alla visita successiva. I cookie "
        "possono avere finalità tecniche, necessarie al corretto funzionamento del sito, oppure finalità "
        "di profilazione, per tracciare le abitudini di navigazione dell'utente."
    ),
    spacer(36),

    policy_heading("Cookie utilizzati su questo sito"),
    spacer(10),
    policy_text(
        "Questo sito utilizza esclusivamente <strong>cookie tecnici</strong>, necessari al funzionamento "
        "della piattaforma WordPress e dell'editor Elementor e al miglioramento delle prestazioni di "
        "caricamento delle pagine. Questi cookie non richiedono il consenso preventivo dell'utente ai "
        "sensi della normativa vigente (art. 122 Codice Privacy e Linee guida del Garante Privacy sui "
        "cookie), in quanto strettamente necessari all'erogazione del servizio richiesto."
    ),
    spacer(16),
    policy_table([
        ("wordpress_test_cookie", "Verifica che il browser dell'utente supporti i cookie.", "Sessione"),
        ("wp-settings-*, wp-settings-time-*", "Personalizzano l'interfaccia di amministrazione (solo per utenti autenticati).", "1 anno"),
        ("wordpress_logged_in_*", "Mantiene la sessione di accesso per gli utenti autenticati (solo per l'amministratore del sito).", "Sessione"),
        ("Cookie di cache (Aruba Hispeed Cache)", "Ottimizzano i tempi di caricamento delle pagine memorizzando una versione statica dei contenuti.", "Variabile"),
    ]),
    spacer(36),

    policy_heading("Cookie di profilazione e di terze parti"),
    spacer(10),
    policy_text(
        "Questo sito <strong>non utilizza cookie di profilazione</strong> né cookie di terze parti a fini "
        "statistici, pubblicitari o di marketing (es. Google Analytics, Meta Pixel). Qualora in futuro "
        "venissero introdotti strumenti di questo tipo, la presente informativa sarà aggiornata e verrà "
        "richiesto il consenso preventivo dell'utente tramite apposito banner."
    ),
    spacer(36),

    policy_heading("Contenuti e servizi esterni"),
    spacer(10),
    policy_text(
        "Il sito carica caratteri tipografici da <strong>Google Fonts</strong> (Google Ireland Limited) e "
        "include collegamenti diretti a <strong>WhatsApp</strong> e <strong>Instagram</strong> (Meta "
        "Platforms Ireland Limited). Questi servizi possono impostare propri cookie solo se l'utente "
        "interagisce direttamente con essi (ad esempio cliccando su un link che porta a Instagram o "
        "WhatsApp): in tal caso si applicano le rispettive cookie policy, esterne a questo sito."
    ),
    spacer(36),

    policy_heading("Come gestire i cookie dal browser"),
    spacer(10),
    policy_text(
        "È possibile gestire le preferenze relative ai cookie direttamente dalle impostazioni del proprio "
        "browser, che permettono di rifiutare o eliminare i cookie già installati. Di seguito i link alle "
        "istruzioni per i principali browser:"
    ),
    spacer(8),
    policy_list([
        "<a href=\"https://support.google.com/chrome/answer/95647\" target=\"_blank\" rel=\"noopener\">Google Chrome</a>",
        "<a href=\"https://support.mozilla.org/it/kb/Attivare%20e%20disattivare%20i%20cookie\" target=\"_blank\" rel=\"noopener\">Mozilla Firefox</a>",
        "<a href=\"https://support.apple.com/it-it/guide/safari/sfri11471/mac\" target=\"_blank\" rel=\"noopener\">Safari</a>",
        "<a href=\"https://support.microsoft.com/it-it/microsoft-edge\" target=\"_blank\" rel=\"noopener\">Microsoft Edge</a>",
    ]),
    spacer(8),
    policy_text(
        "Si segnala che la disabilitazione dei cookie tecnici potrebbe compromettere il corretto "
        "funzionamento di alcune parti del sito."
    ),
    spacer(36),

    policy_heading("Titolare del trattamento"),
    spacer(10),
    policy_text(
        "Il Titolare del trattamento è <strong>Samantha Crepaldi</strong>, con sede in Via Ruzante 10, "
        "Codevigo (PD), Codice Fiscale CRPSNT89R51G693E. Per maggiori informazioni sul trattamento dei "
        "dati personali consulta la <a href=\"/privacy-policy/\">Privacy Policy</a>."
    ),
    spacer(36),

    policy_heading("Modifiche alla presente cookie policy"),
    spacer(10),
    policy_text(
        "Il Titolare si riserva di modificare o aggiornare, in tutto o in parte, la presente informativa, "
        "dandone comunicazione tramite pubblicazione sul sito. Si consiglia di consultare periodicamente "
        "questa pagina."
    ),
    spacer(24),
    text('<span style="font-size:13px;">Ultimo aggiornamento: settembre 2026.</span>', color=INK_FAINT),
]

body_settings = sec_bg(color=BG)
body_settings["_element_id"] = "cookie-body"
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
footer_settings["_element_id"] = "footer-cookie-page"
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

with open("elementor_data_cookie.json", "w") as f:
    json.dump(SECTIONS, f)

print("Sections:", len(SECTIONS))
print("Total JSON length:", len(json.dumps(SECTIONS)))
