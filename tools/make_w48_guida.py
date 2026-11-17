import base64, pathlib
from playwright.sync_api import sync_playwright
OUT = pathlib.Path('/home/claude/smilefix-media/w48'); OUT.mkdir(exist_ok=True)
logo = 'data:image/png;base64,' + base64.b64encode(open('/tmp/site/img/logo-smilefix.png','rb').read()).decode()

STEPS = [
 ("Trova l'asta", "Sui portali ufficiali delle vendite giudiziarie"),
 ("Leggi l'avviso", "Prezzo base, cauzione, IVA, spese e scadenze"),
 ("Vedi il veicolo", "Giornata di visione: di solito niente prova su strada"),
 ("Fai i conti", "Prezzo massimo tutto compreso, prima di offrire"),
 ("Cauzione e offerta", "Di solito almeno il 10% del prezzo offerto"),
 ("La gara", "Rilanci fino al tuo limite, non oltre"),
 ("Saldo e ritiro", "Pagamento nei termini, passaggio e ritiro"),
]
BASE = """<html><head><style>
*{box-sizing:border-box;margin:0;padding:0}
body{width:%(w)dpx;height:%(h)dpx;overflow:hidden;font-family:'Inter',sans-serif;color:#10283C;
background:#FFF6DC;background-image:radial-gradient(#e9dcb8 1.6px,transparent 1.6px);background-size:26px 26px;position:relative}
.logo{position:absolute;background:#fff;border:4px solid #10283C;border-radius:16px;padding:6px 10px;box-shadow:5px 5px 0 #10283C}
.logo img{display:block;height:%(lh)dpx}
.kick{display:inline-block;background:#FFB000;border:4px solid #10283C;border-radius:12px;padding:6px 16px;font-weight:900;letter-spacing:2px;text-transform:uppercase;box-shadow:5px 5px 0 #10283C}
h1{font-family:'Inter Display','Inter';font-weight:900;letter-spacing:-2px;line-height:1}
.step{display:flex;gap:18px;align-items:center;background:#fff;border:4px solid #10283C;border-radius:16px;box-shadow:6px 6px 0 #10283C}
.n{flex:none;background:#10283C;color:#FFB000;font-weight:900;border-radius:10px;display:flex;align-items:center;justify-content:center}
.t b{display:block;font-weight:900}
.t span{color:#33475a;font-weight:600}
.foot{position:absolute;font-weight:800;display:flex;justify-content:space-between;align-items:center}
.url{background:#10283C;color:#fff;border-radius:30px;padding:8px 20px}
</style></head><body>%(body)s</body></html>"""

def page(w,h,body,lh=64):
    return BASE % dict(w=w,h=h,body=body,lh=lh)

def steps_html(fs_b, fs_s, n, pad, gap):
    return ''.join(f'<div class="step" style="padding:{pad}px;margin-bottom:{gap}px"><div class="n" style="width:{n}px;height:{n}px;font-size:{int(n*.55)}px">{i+1}</div><div class="t"><b style="font-size:{fs_b}px">{a}</b><span style="font-size:{fs_s}px">{b}</span></div></div>' for i,(a,b) in enumerate(STEPS))

pages = {}
# IG 1080x1350
pages['ig_guida_asta.jpg'] = page(1080,1350, f"""
<div class="logo" style="top:48px;right:56px"><img src="{logo}"></div>
<div style="position:absolute;left:64px;top:64px"><span class="kick" style="font-size:26px">Guida gratuita · salvala</span></div>
<h1 style="position:absolute;left:64px;top:150px;width:950px;font-size:84px">Asta auto giudiziaria: i 7 passi</h1>
<div style="position:absolute;left:64px;right:64px;top:350px">{steps_html(32,22,58,14,14)}</div>
<div class="foot" style="left:64px;right:64px;bottom:44px;font-size:26px"><span>Guida completa sul sito</span><span class="url">smilefixbroker.com/guide</span></div>
""")
# FB 1080x1350 - editorial style
pages['fb_guida_asta.jpg'] = f"""<html><head><style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1350px;overflow:hidden;background:#F4EFE3;color:#1b1b1b;font-family:'DejaVu Serif',serif;position:relative}}
.top{{position:absolute;left:70px;right:70px;top:60px;border-bottom:4px double #1b1b1b;padding-bottom:16px;display:flex;justify-content:space-between;align-items:center}}
.top b{{font-size:50px}}
.sub{{position:absolute;left:70px;right:70px;top:150px;display:flex;justify-content:space-between;font-family:'Inter';font-weight:700;font-size:20px;letter-spacing:2px;border-bottom:2px solid #1b1b1b;padding-bottom:10px}}
h1{{position:absolute;left:70px;right:70px;top:230px;font-size:78px;line-height:1.05}}
p.l{{position:absolute;left:70px;right:70px;top:500px;font-size:34px;line-height:1.4;color:#333}}
ol{{position:absolute;left:110px;right:70px;top:700px;font-family:'Inter';font-weight:700;font-size:34px;line-height:1.75}}
.f{{position:absolute;left:70px;right:70px;bottom:50px;border-top:2px solid #1b1b1b;padding-top:14px;display:flex;justify-content:space-between;font-family:'Inter';font-weight:800;font-size:24px}}
img{{height:60px}}
</style></head><body>
<div class="top"><b>La Gazzetta del Motore</b><img src="{logo}"></div>
<div class="sub"><span>EDIZIONE SMILEFIX BROKER</span><span style="color:#b03a2e">GUIDE</span><span>NOVEMBRE 2026</span></div>
<h1>Come funziona un'asta auto giudiziaria</h1>
<p class="l">Dall'avviso di vendita al ritiro del veicolo: le tappe, gli errori da evitare e la checklist prima di offrire.</p>
<ol><li>Trova l'asta</li><li>Leggi l'avviso di vendita</li><li>Vedi il veicolo</li><li>Fai i conti tutto compreso</li><li>Cauzione e offerta</li><li>La gara</li><li>Saldo, passaggio e ritiro</li></ol>
<div class="f"><span>Guida gratuita</span><span>smilefixbroker.com/guide</span></div>
</body></html>"""
# Pinterest 1000x1500
pages['pin_guida_asta.jpg'] = page(1000,1500, f"""
<div style="position:absolute;left:56px;right:56px;top:56px;background:#6B3DF2;border:5px solid #10283C;border-radius:22px;padding:34px 36px;box-shadow:8px 8px 0 #10283C;color:#fff">
<div style="font-weight:900;letter-spacing:3px;font-size:24px;opacity:.9">GUIDA GRATUITA · SALVALA</div>
<h1 style="font-size:76px;margin-top:12px">Asta auto giudiziaria: come funziona</h1></div>
<div style="position:absolute;left:56px;right:56px;top:470px">{steps_html(31,21,56,14,13)}</div>
<div class="foot" style="left:56px;right:56px;bottom:46px;font-size:24px"><div class="logo" style="position:static"><img src="{logo}"></div><span class="url">smilefixbroker.com/guide</span></div>
""", lh=54)
# Telegram 1080x1080 dark bulletin
rows = ''.join(f'<div style="display:flex;gap:26px;border-bottom:2px dashed #3a3a3a;padding:13px 0"><span style="color:#FF6B57;font-family:DejaVu Sans Mono;font-weight:700;font-size:34px">0{i+1}</span><span style="font-size:34px;font-weight:700">{a}</span></div>' for i,(a,b) in enumerate(STEPS))
pages['tg_guida_asta.jpg'] = f"""<html><head><style>*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1080px;overflow:hidden;background:#161616;color:#f2f2f2;font-family:'Inter';position:relative}}</style></head><body>
<div style="position:absolute;left:70px;top:60px;font-family:'DejaVu Sans Mono';color:#FF6B57;font-size:26px;letter-spacing:2px">● GUIDA SMILEFIX</div>
<img src="{logo}" style="position:absolute;right:70px;top:46px;height:66px;background:#fff;border-radius:10px;padding:4px 8px">
<h1 style="position:absolute;left:70px;right:70px;top:130px;font-family:'Inter Display';font-weight:900;font-size:64px;line-height:1.05;color:#FF6B57">Asta auto giudiziaria in 7 passi</h1>
<div style="position:absolute;left:70px;right:70px;top:330px">{rows}</div>
<div style="position:absolute;left:70px;bottom:46px;font-family:'DejaVu Sans Mono';font-size:24px;color:#9a9a9a">Guida completa: smilefixbroker.com/guide</div>
</body></html>"""
# TikTok carousel 1080x1920
cover = page(1080,1920, f"""
<div class="logo" style="top:80px;left:70px"><img src="{logo}"></div>
<div style="position:absolute;left:70px;top:330px"><span class="kick" style="font-size:34px">Guida gratuita</span></div>
<h1 style="position:absolute;left:70px;right:70px;top:440px;font-size:130px">Asta auto giudiziaria: come funziona</h1>
<div style="position:absolute;left:70px;right:70px;top:1050px;font-size:48px;font-weight:700;color:#33475a">I 7 passi, dall'avviso di vendita al ritiro del veicolo 👉</div>
<div class="foot" style="left:70px;right:70px;bottom:150px;font-size:34px"><span>Salvalo per dopo</span><span class="url">smilefixbroker.com</span></div>
""", lh=80)
pages['tt_guida_00.jpg'] = cover
for i,(a,b) in enumerate(STEPS):
    pages[f'tt_guida_{i+1:02d}.jpg'] = page(1080,1920, f"""
<div class="logo" style="top:80px;left:70px"><img src="{logo}"></div>
<div style="position:absolute;right:70px;top:90px;font-weight:900;font-size:40px">{i+1}/7</div>
<div style="position:absolute;left:70px;top:420px;width:260px;height:260px;background:#10283C;color:#FFB000;border-radius:36px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:180px;box-shadow:12px 12px 0 #FFB000">{i+1}</div>
<h1 style="position:absolute;left:70px;right:70px;top:780px;font-size:120px">{a}</h1>
<div style="position:absolute;left:70px;right:70px;top:1120px;background:#fff;border:5px solid #10283C;border-radius:24px;box-shadow:8px 8px 0 #10283C;padding:34px;font-size:54px;font-weight:700;line-height:1.25">{b}</div>
<div class="foot" style="left:70px;right:70px;bottom:150px;font-size:32px"><span>Asta auto giudiziaria</span><span class="url">smilefixbroker.com</span></div>
""", lh=80)
pages['tt_guida_08.jpg'] = page(1080,1920, f"""
<div class="logo" style="top:80px;left:70px"><img src="{logo}"></div>
<h1 style="position:absolute;left:70px;right:70px;top:420px;font-size:112px">Non hai tempo di leggere avvisi e perizie?</h1>
<div style="position:absolute;left:70px;right:70px;top:1000px;font-size:56px;font-weight:700;line-height:1.3">Ti diciamo prima quanto ti costa il veicolo consegnato, tutto compreso, e pensiamo noi a offerta, pratiche e ritiro.</div>
<div class="foot" style="left:70px;right:70px;bottom:150px;font-size:34px"><span>Guida completa al link in bio</span><span class="url">smilefixbroker.com</span></div>
""", lh=80)

with sync_playwright() as p:
    b = p.chromium.launch()
    for name, htmlsrc in pages.items():
        import re
        w,h = map(int, re.search(r'width:(\d+)px;height:(\d+)px', htmlsrc).groups())
        pg = b.new_page(viewport={'width':w,'height':h})
        pg.set_content(htmlsrc); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT/name), type='jpeg', quality=90)
        pg.close()
    b.close()
print(sorted(x.name for x in OUT.iterdir()))
