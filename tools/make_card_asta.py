"""Genera le schede asta per il canale WhatsApp nello stile SmileFix (1080x1350).
Uso:
  python3 make_card_asta.py card.json out.jpg
card.json:
 {"tipo":"occasione"|"esito", "categoria":"AUTO", "titolo":"Renault Arkana<br>E-Tech full hybrid",
  "sottotitolo":"2022 · 123.000 km", "prezzo":"13.500 €", "label_prezzo":"Te la portiamo a casa con",
  "mercato":"15.500 €", "esito":"Aggiudicata a 12.000 € (4 offerte)",
  "verdetto":"✅ OCCASIONE VERA · Il cliente avrebbe risparmiato 2.000 €, servizio incluso.",
  "bg":"#C9F04F", "cta_bg":"#FF6B57", "dark": false}
"""
import base64, json, sys
from playwright.sync_api import sync_playwright

LOGO = 'data:image/png;base64,' + base64.b64encode(open('/tmp/site/img/logo-smilefix.png', 'rb').read()).decode()

def html(c):
    dark = c.get('dark', False)
    fg = '#ffffff' if dark else '#111111'
    dot = 'rgba(255,255,255,.18)' if dark else 'rgba(0,0,0,.14)'
    esito = c.get('tipo') == 'esito'
    badge = '🔨 ASTA CONCLUSA' if esito else "🔨 OCCASIONE DALL'ASTA"
    label = c.get('label_prezzo') or ('Con noi chiavi in mano' if esito else 'Te la portiamo a casa con')
    esito_pill = f'<div class="pill">{c["esito"]}</div>' if esito and c.get('esito') else ''
    bottom = c.get('verdetto') if esito else 'Scrivici "ASTA" · smilefixbroker.com'
    foot = c.get('nota') or ("Esempio su un'asta giudiziaria conclusa. Prezzi chiavi in mano stimati con il metodo SmileFix (diritti, passaggio, rimessa in strada, servizio incluso)." if esito else
            "Prezzo stimato chiavi in mano, servizio SmileFix incluso, se aggiudicata alla base d'asta. L'esito dell'asta non è garantito.")
    top_title = 230 if esito else 245
    price_top = 640 if esito else 600
    return f"""<html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif;color:{fg};
background:{c.get('bg','#FFE04D')};background-image:radial-gradient({dot} 1.6px,transparent 1.6px);background-size:26px 26px;position:relative}}
.logo{{position:absolute;left:72px;top:66px;background:#FFF6DC;border:5px solid #111;border-radius:18px;padding:8px 12px;box-shadow:6px 6px 0 #111}}
.logo img{{height:64px;display:block}}
.badge{{position:absolute;right:72px;top:62px;background:#111;color:#FFD84D;font-weight:900;font-size:32px;padding:14px 28px;border-radius:14px;transform:rotate(2deg)}}
.cat{{position:absolute;left:72px;top:{top_title-50}px;font-weight:900;font-size:34px;letter-spacing:4px}}
h1{{position:absolute;left:72px;right:72px;top:{top_title}px;font-weight:900;font-size:94px;line-height:1;letter-spacing:-3px}}
.sub{{position:absolute;left:72px;top:{top_title+215}px;font-weight:800;font-size:36px}}
.pill{{position:absolute;left:72px;top:{top_title+265}px;background:#111;color:#fff;font-weight:900;font-size:34px;padding:10px 22px;border-radius:12px}}
.price{{position:absolute;left:72px;right:60px;top:{price_top}px;height:300px;background:#fff;border:7px solid #111;border-radius:30px;box-shadow:14px 14px 0 #111;transform:rotate(-1deg);padding:34px 46px;color:#111}}
.price .l{{font-weight:900;font-size:40px}}
.price .v{{font-weight:900;font-size:150px;letter-spacing:-6px;line-height:1.05}}
.mkt{{position:absolute;left:72px;top:{price_top+335}px;font-weight:900;font-size:44px;display:flex;align-items:center;gap:26px}}
.mkt span{{background:#fff;color:#111;border:5px solid #111;border-radius:14px;padding:4px 20px}}
.cta{{position:absolute;left:72px;right:72px;top:1095px;min-height:95px;background:{c.get('cta_bg','#5B2BFF')};color:{c.get('cta_fg','#fff')};border:6px solid #111;border-radius:18px;
display:flex;align-items:center;justify-content:center;text-align:center;font-weight:900;font-size:{36 if esito else 40}px;padding:12px 24px;line-height:1.2}}
.foot{{position:absolute;left:72px;right:72px;top:1235px;font-weight:600;font-size:21px;line-height:1.3}}
</style></head><body>
<div class="logo"><img src="{LOGO}"></div><div class="badge">{badge}</div>
<div class="cat">{c.get('categoria','AUTO')}</div><h1>{c['titolo']}</h1><div class="sub">{c.get('sottotitolo','')}</div>{esito_pill}
<div class="price"><div class="l">{label}</div><div class="v">{c['prezzo']}</div></div>
<div class="mkt">Valore di mercato <span>{c['mercato']}</span></div>
<div class="cta">{bottom}</div><div class="foot">{foot}</div>
</body></html>"""

if __name__ == '__main__':
    card = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        pg.set_content(html(card)); pg.wait_for_timeout(300)
        pg.screenshot(path=out, type='jpeg', quality=90); b.close()
    print(out)
