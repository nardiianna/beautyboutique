from common import *

MOBILE_CSS = """<style>
#services-strip .elementor-column:not(:first-child){border-left:1px solid #E3D3B6;}
@media (min-width: 768px) and (max-width: 1024px) {
  #services-strip .elementor-container{flex-wrap:wrap;}
  #services-strip .elementor-column{width:50%!important;}
  #services-strip .elementor-column:nth-child(odd){border-left:none!important;}
  #services-strip .elementor-column:nth-child(-n+2){border-top:none!important;}
  #services-strip .elementor-column{border-top:1px solid #E3D3B6;}
}
@media (max-width: 767px) {
  #home > .elementor-container{min-height:0!important;}
  #home{background-image:url('""" + M["hero-mobile-bg.png"]["url"] + """')!important;background-size:cover!important;background-position:right center!important;background-color:#FBF6EE!important;}
  #hero-card{background-color:rgba(251,246,238,.15)!important;}
  #services-strip .elementor-column{width:100%!important;border-left:none!important;border-top:1px solid #E3D3B6!important;}
  #services-strip .elementor-column:first-child{border-top:none!important;}
  #trattamenti h2,#il-centro h2,#prodotti h2{font-size:26px!important;}
  #trattamenti-all-link{margin-top:16px!important;}
  #trattamenti-all-link div{text-align:left!important;}
  #trattamenti-grid .elementor-widget-image{margin-bottom:20px!important;}
  #trattamenti-grid .elementor-column{padding-bottom:56px!important;border-bottom:1px solid #E3D3B6;}
  #trattamenti-grid .elementor-column:last-child{border-bottom:none;}
  #il-centro .elementor-widget-image,#prodotti .elementor-widget-image{margin-bottom:24px!important;margin-top:24px!important;}
  #risultati .elementor-widget-image{margin-bottom:20px!important;}
  #footer-social-row{justify-content:center!important;}
  #risultati-cards > .elementor-container > .elementor-column{padding-bottom:28px!important;}
  #contatti-info .elementor-column{padding-top:36px!important;padding-bottom:36px!important;border-bottom:1px solid #E3D3B6;margin-bottom:0;}
  #contatti-info .elementor-column:first-child{padding-top:0!important;}
  #contatti-info .elementor-column:last-child{border-bottom:none;}
  #contatti-write .elementor-widget-image{margin-bottom:20px!important;}
  #primary-nav-col{display:none!important;}
  #mobile-menu-toggle{display:inline-flex!important;}
  #header-cta-row{justify-content:space-between!important;width:100%;}
}
#mobile-menu-toggle{display:none;background:none;border:none;cursor:pointer;padding:6px;flex-direction:column;gap:5px;align-items:center;justify-content:center;}
#mobile-menu-toggle span{display:block;width:22px;height:2px;background:#2A2117;}
#mobile-nav-panel{display:none;background:#FBF6EE;border-top:1px solid #E3D3B6;}
#mobile-nav-panel.open{display:block!important;}
#mobile-nav-panel a{display:block;padding:14px 24px;font-family:'Jost',sans-serif;font-size:13px;letter-spacing:.08em;text-transform:uppercase;font-weight:500;color:#6E5D49;text-decoration:none;border-bottom:1px solid #E3D3B6;}
</style>
<script>
(function(){
  function ready(fn){ if(document.readyState!='loading'){fn();} else {document.addEventListener('DOMContentLoaded',fn);} }
  ready(function(){
    var toggle = document.getElementById('mobile-menu-toggle');
    var panel = document.getElementById('mobile-nav-panel');
    if(!toggle || !panel) return;
    toggle.addEventListener('click', function(){
      var open = panel.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
    panel.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        panel.classList.remove('open');
        toggle.setAttribute('aria-expanded','false');
      });
    });
  });
})();
</script>"""


def build_header(nav_items, logo_href="/"):
    """nav_items: list of (href, label, active_bool)"""
    header_settings = sec_bg(color=BG)
    header_settings.update(pad(20, 20, 20, 20))
    header_settings["_element_id"] = "site-header"

    nav_html = '<nav style="display:flex;gap:26px;flex-wrap:wrap;justify-content:center;">'
    for href, label, active in nav_items:
        if active:
            nav_html += (f'<a href="{href}" style="color:{INK};font-family:\'{FONT_BODY}\',sans-serif;font-size:12.5px;'
                         f'letter-spacing:.09em;text-transform:uppercase;font-weight:500;text-decoration:none;'
                         f'border-bottom:1px solid {GOLD};padding-bottom:4px;">{label}</a>')
        else:
            nav_html += (f'<a href="{href}" style="color:{INK_SOFT};font-family:\'{FONT_BODY}\',sans-serif;'
                         f'font-size:12.5px;letter-spacing:.09em;text-transform:uppercase;font-weight:500;'
                         f'text-decoration:none;">{label}</a>')
    nav_html += '</nav>'

    header_section = section([
        column(20, [image_widget("logo-header.png", link=logo_href, width_px=130),
                    widget("text-editor", {"editor": MOBILE_CSS})], {"content_position": "center"}),
        column(50, [text(nav_html)], {"content_position": "center", "_element_id": "primary-nav-col"}),
        column(30, [text(
            '<div id="header-cta-row" style="display:flex;align-items:center;justify-content:flex-end;gap:14px;">'
            '<button id="mobile-menu-toggle" aria-label="Apri il menu" aria-expanded="false">'
            '<span></span><span></span><span></span></button>'
            f'<a href="https://gestionale.nardianna.it/beauty-boutique/prenota" target="_blank" rel="noopener" '
            f'style="display:inline-block;background:{GOLD};color:{CREAM};font-family:\'{FONT_BODY}\',sans-serif;'
            f'font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:500;'
            f'text-decoration:none;padding:14px 26px;border-radius:4px;white-space:nowrap;">Prenota ora →</a>'
            '</div>'
        )], {"content_position": "center"}),
    ], header_settings)

    mobile_panel_settings = sec_bg(color=BG)
    mobile_panel_settings["_element_id"] = "mobile-nav-panel"
    mobile_panel_settings.update(pad(0, 0, 0, 0))
    panel_html = "".join(f'<a href="{href}">{label}</a>' for href, label, active in nav_items)
    mobile_panel_section = section([
        column(100, [text(panel_html)]),
    ], mobile_panel_settings)

    return header_section, mobile_panel_section
