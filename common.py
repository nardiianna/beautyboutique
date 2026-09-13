import json, uuid

with open("media_map.json") as f:
    M = json.load(f)

def img(fname):
    m = M[fname]
    return {"url": m["url"], "id": m["id"]}

def rid():
    return uuid.uuid4().hex[:7]

# ---------- palette ----------
INK = "#2A2117"
INK_SOFT = "#6E5D49"
INK_FAINT = "#9C8B72"
GOLD = "#A9793C"
GOLD_DEEP = "#7C5726"
BG = "#FBF6EE"
BG_ALT = "#F2E7D4"
LINE = "#E3D3B6"
CREAM = "#FBF6EE"

FONT_DISPLAY = "Playfair Display"
FONT_BODY = "Jost"

def px(n):
    return {"unit": "px", "size": n, "sizes": []}

def em(n):
    return {"unit": "em", "size": n, "sizes": []}

def typo(family, size=None, weight=None, line_height=None, letter_spacing=None,
         transform=None, style=None, prefix="typography"):
    d = {f"{prefix}_typography": "custom", f"{prefix}_font_family": family}
    if size is not None:
        d[f"{prefix}_font_size"] = px(size)
    if weight is not None:
        d[f"{prefix}_font_weight"] = str(weight)
    if line_height is not None:
        d[f"{prefix}_line_height"] = em(line_height)
    if letter_spacing is not None:
        d[f"{prefix}_letter_spacing"] = px(letter_spacing)
    if transform:
        d[f"{prefix}_text_transform"] = transform
    if style:
        d[f"{prefix}_font_style"] = style
    return d

# Kit-level "default spacing between widgets" (20px) is added via CSS calc() as an
# extra bottom margin on every widget wrapper, on top of any explicit margin we set.
# Cancel it out here so our own spacer widgets are the only thing controlling gaps.
NO_KIT_GAP = {"unit": "px", "top": "0", "right": "0", "bottom": "-20", "left": "0", "isLinked": False}

def widget(widget_type, settings=None):
    s = settings or {}
    if "_margin" not in s:
        s = {**s, "_margin": NO_KIT_GAP}
    return {"id": rid(), "elType": "widget", "widgetType": widget_type,
            "settings": s, "elements": []}

def column(size, elements, settings=None):
    s = {"_column_size": size}
    if settings:
        s.update(settings)
    return {"id": rid(), "elType": "column", "settings": s, "elements": elements}

def section(columns, settings=None, inner=False):
    s = dict(settings or {})
    obj = {"id": rid(), "elType": "section", "settings": s, "elements": columns}
    if inner:
        obj["isInner"] = True
    return obj

def heading(text, size_tag="h2", size=32, color=INK, weight=600, align=None,
            font=FONT_DISPLAY, line_height=1.15, letter_spacing=None, transform=None):
    s = {"title": text, "header_size": size_tag, "title_color": color}
    if align:
        s["align"] = align
    s.update(typo(font, size=size, weight=weight, line_height=line_height,
                  letter_spacing=letter_spacing, transform=transform))
    return widget("heading", s)

def eyebrow(text, align=None):
    s = {"title": text, "header_size": "span", "title_color": GOLD_DEEP}
    if align:
        s["align"] = align
    s.update(typo(FONT_BODY, size=12, weight=500, letter_spacing=1.8, transform="uppercase"))
    return widget("heading", s)

def text(html, color=INK_SOFT, size=15.5, align=None, weight=300, font=FONT_BODY, line_height=1.6):
    # wrap in a div so WP's wpautop doesn't add its own margined <p> around loose content
    s = {"editor": f'<div style="margin:0;">{html}</div>'}
    if align:
        s["align"] = align
    s["text_color"] = color
    s.update(typo(font, size=size, weight=weight, line_height=line_height))
    return widget("text-editor", s)

def link_arrow(text_, url="#", align=None):
    s = {"editor": f'<div style="margin:0;text-align:{align or "left"};"><a href="{url}" style="color:{GOLD_DEEP};font-family:\'{FONT_BODY}\',sans-serif;'
                    f'font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:500;'
                    f'text-decoration:none;border-bottom:1px solid {GOLD_DEEP};padding-bottom:2px;">{text_}</a></div>'}
    if align:
        s["align"] = align
    return widget("text-editor", s)

def btn(text_, url, style="solid", align=None):
    s = {
        "text": text_,
        "link": {"url": url, "is_external": "" if url.startswith("#") else "true", "nofollow": ""},
        "size": "md",
        "border_radius": {"unit": "px", "top": "4", "right": "4", "bottom": "4", "left": "4", "isLinked": True},
        "text_padding": {"unit": "px", "top": "14", "right": "26", "bottom": "14", "left": "26", "isLinked": False},
    }
    if align:
        s["align"] = align
    s.update(typo(FONT_BODY, size=12.5, weight=500, letter_spacing=1, transform="uppercase"))
    if style == "solid":
        s["background_color"] = GOLD
        s["button_text_color"] = CREAM
        s["button_background_hover_color"] = GOLD_DEEP
    else:  # ghost cream, for dark cta banner
        s["background_color"] = "transparent"
        s["button_text_color"] = CREAM
        s["border_border"] = "solid"
        s["border_width"] = {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True}
        s["border_color"] = "rgba(251,246,238,.55)"
    return widget("button", s)

def html_button(text_, url, align="right"):
    # raw-HTML button, pinned with a real text-align div (bypasses Elementor's
    # button "align" control, which doesn't reliably reach the column edge)
    html = (f'<div style="margin:0;text-align:{align};"><a href="{url}" target="_blank" rel="noopener" '
            f'style="display:inline-block;background:{GOLD};color:{CREAM};font-family:\'{FONT_BODY}\',sans-serif;'
            f'font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:500;'
            f'text-decoration:none;padding:14px 26px;border-radius:4px;">{text_}</a></div>')
    return text(html)

def image_widget(fname, link=None, size="full", width_px=None, align=None, radius=None):
    s = {"image": img(fname), "image_size": size}
    if link:
        s["link_to"] = "custom"
        s["link"] = {"url": link}
    if width_px:
        s["width"] = {"unit": "px", "size": width_px, "sizes": []}
    if align:
        s["align"] = align
    if radius:
        s["image_border_radius"] = {"unit": "px", "top": str(radius), "right": str(radius),
                                     "bottom": str(radius), "left": str(radius), "isLinked": True}
    return widget("image", s)

def spacer(h):
    return widget("spacer", {"space": px(h)})

def icon_box(fname, box=56):
    url = M[fname]["url"]
    html = (f'<div style="width:{box}px;height:{box}px;margin:0 auto;display:flex;'
            f'align-items:center;justify-content:center;">'
            f'<img src="{url}" style="max-width:100%;max-height:100%;width:auto;'
            f'height:auto;display:block;"></div>')
    return text(html)

def fixed_box(height, elements, align="center"):
    return section([
        column(100, elements, {"content_position": align}),
    ], {"height": "min-height", "custom_height": {"unit": "px", "size": height, "sizes": []}}, inner=True)

def icon_widget(icon_class, link=None, color=INK_SOFT, border_color=LINE, size_px=15):
    s = {
        "icon": icon_class,
        "selected_icon": {"value": icon_class, "library": "fa-brands"},
        "view": "framed",
        "shape": "circle",
        "primary_color": color,
        "secondary_color": "transparent",
        "size": {"unit": "px", "size": size_px, "sizes": []},
    }
    if link:
        s["link"] = {"url": link, "is_external": "true"}
    return widget("icon", s)

def sec_bg(color=None, image_fname=None, position=None):
    s = {"background_background": "classic"}
    if color:
        s["background_color"] = color
    if image_fname:
        s["background_image"] = img(image_fname)
        s["background_size"] = "cover"
        s["background_position"] = position or "center center"
    return s

def pad(top, right=None, bottom=None, left=None):
    if right is None:
        right = top
    if bottom is None:
        bottom = top
    if left is None:
        left = right
    return {"padding": {"unit": "px", "top": str(top), "right": str(right),
                         "bottom": str(bottom), "left": str(left), "isLinked": False}}

def pad_tablet(top, bottom=None):
    if bottom is None:
        bottom = top
    return {"padding_tablet": {"unit": "px", "top": str(top), "right": "20",
                                "bottom": str(bottom), "left": "20", "isLinked": False}}

def pad_mobile(top, bottom=None):
    if bottom is None:
        bottom = top
    return {"padding_mobile": {"unit": "px", "top": str(top), "right": "20",
                                "bottom": str(bottom), "left": "20", "isLinked": False}}

def section_pad(top=90, bottom=None):
    if bottom is None:
        bottom = top
    d = pad(top, 20, bottom, 20)
    d.update(pad_tablet(min(top, 64), min(bottom, 64)))
    d.update(pad_mobile(min(top, 48), min(bottom, 48)))
    return d
