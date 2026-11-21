# Render settimanale: immagini IG/FB/PIN/TG/storie + slide video. Uso: python3 render_week.py w48
import base64, pathlib, re, sys, importlib.util
from playwright.sync_api import sync_playwright
WK = sys.argv[1]
spec = importlib.util.spec_from_file_location("c", f"/home/claude/smilefix-media/tools/{WK}_content.py"); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
OUT = pathlib.Path(f'/home/claude/smilefix-media/{WK}'); OUT.mkdir(exist_ok=True)
SL = pathlib.Path(f'/home/claude/smilefix-media/{WK}v/slides'); SL.mkdir(parents=True, exist_ok=True)
logo = 'data:image/png;base64,' + base64.b64encode(open('/tmp/site/img/logo-smilefix.png', 'rb').read()).decode()
NAVY, AMB = '#10283C', '#FFB000'
POP = ['#FF5C8A', '#6B3DF2', '#00B894', '#FF7A00', '#1E90FF']

def pop_page(w, h, body):
    return f"""<html><head><style>*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:{w}px;height:{h}px;overflow:hidden;font-family:'Inter',sans-serif;color:{NAVY};background:#FFF6DC;
background-image:radial-gradient(#e9dcb8 1.6px,transparent 1.6px);background-size:26px 26px;position:relative}}
.logo{{position:absolute;background:#fff;border:4px solid {NAVY};border-radius:16px;padding:6px 10px;box-shadow:5px 5px 0 {NAVY}}}
.logo img{{display:block;height:56px}}
.kick{{display:inline-block;background:{AMB};border:4px solid {NAVY};border-radius:12px;padding:6px 16px;font-weight:900;letter-spacing:2px;text-transform:uppercase;box-shadow:5px 5px 0 {NAVY}}}
h1{{font-weight:900;letter-spacing:-2px;line-height:1.02}}
.card{{background:#fff;border:5px solid {NAVY};border-radius:24px;box-shadow:9px 9px 0 {NAVY}}}
.src{{position:absolute;font-weight:700;color:#33475a}}
.url{{background:{NAVY};color:#fff;border-radius:30px;padding:8px 20px;font-weight:800}}
em{{font-style:normal;background:{AMB};padding:0 10px;border-radius:8px}}
</style></head><body>{body}</body></html>"""

def data_block(kind, data, accent, scale=1.0):
    s = scale
    if kind in ('num', 'book'):
        n, t = data
        if kind == 'book':
            return f'<div class="card" style="padding:{40*s}px;display:flex;gap:{36*s}px;align-items:center"><div style="flex:none;width:{220*s}px;height:{300*s}px;background:{NAVY};border-radius:16px;color:{AMB};display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:900"><span style="font-size:{34*s}px">VOL.</span><span style="font-size:{150*s}px;line-height:1">{n}</span></div><div style="font-size:{44*s}px;font-weight:800;line-height:1.2">{t}</div></div>'
        fs = 190 if len(n) <= 6 else (150 if len(n) <= 8 else 118)
        return f'<div class="card" style="padding:{40*s}px {44*s}px;background:{accent};color:#fff"><div style="font-size:{fs*s}px;font-weight:900;letter-spacing:-4px;line-height:1">{n}</div><div style="font-size:{40*s}px;font-weight:800;margin-top:{14*s}px">{t}</div></div>'
    if kind == 'bars':
        mx = max(v for _, v, _ in data)
        rows = ''.join(f'<div style="margin-bottom:{22*s}px"><div style="display:flex;justify-content:space-between;font-size:{34*s}px;font-weight:800"><span>{l}</span><span>{st}</span></div><div style="height:{34*s}px;background:#eee;border:3px solid {NAVY};border-radius:12px;margin-top:6px"><div style="height:100%;width:{max(6,v/mx*100):.0f}%;background:{accent};border-radius:8px"></div></div></div>' for l, v, st in data)
        return f'<div class="card" style="padding:{40*s}px">{rows}</div>'
    if kind == 'vs':
        (a, av), (b, bv) = data
        box = lambda l, v, bg, fg: f'<div class="card" style="flex:1;padding:{34*s}px;background:{bg};color:{fg};text-align:center"><div style="font-size:{34*s}px;font-weight:800">{l}</div><div style="font-size:{86*s}px;font-weight:900;letter-spacing:-2px;margin-top:8px">{v}</div></div>'
        return f'<div style="display:flex;gap:{28*s}px;align-items:center">{box(a,av,"#fff",NAVY)}<div style="font-weight:900;font-size:{56*s}px">VS</div>{box(b,bv,accent,"#fff")}</div>'
    if kind == 'quiz':
        q, opts, ok = data
        r = ''.join(f'<div class="card" style="padding:{22*s}px {30*s}px;margin-bottom:{20*s}px;font-size:{40*s}px;font-weight:800;display:flex;gap:20px;{"background:"+accent+";color:#fff" if i==ok else ""}"><span>{"ABC"[i]}</span><span>{o}</span></div>' for i, o in enumerate(opts))
        return f'<div style="font-size:{34*s}px;font-weight:800;margin-bottom:{20*s}px;color:#33475a">{q}</div>{r}'
    if kind == 'list':
        return '<div class="card" style="padding:%dpx">' % (36*s) + ''.join(f'<div style="display:flex;gap:18px;align-items:center;font-size:{38*s}px;font-weight:800;margin-bottom:{16*s}px"><span style="flex:none;width:{48*s}px;height:{48*s}px;border-radius:10px;background:{accent};color:#fff;display:flex;align-items:center;justify-content:center">{i+1}</span>{x}</div>' for i, x in enumerate(data)) + '</div>'

def ig_html(i, it):
    kind, kick, title, data, src = it[:5]; ac = POP[i % 5]
    return pop_page(1080, 1350, f"""<div class="logo" style="top:46px;right:56px"><img src="{logo}"></div>
<div style="position:absolute;left:64px;top:58px"><span class="kick" style="font-size:28px">{kick}</span></div>
<h1 style="position:absolute;left:64px;right:64px;top:160px;font-size:86px">{title}</h1>
<div style="position:absolute;left:64px;right:64px;top:{560 if kind!='quiz' else 520}px">{data_block(kind, data, ac)}</div>
<div class="src" style="left:64px;bottom:120px;font-size:24px">{src}</div>
<div style="position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;align-items:center;font-weight:800;font-size:26px"><span>📌 Salva il post</span><span class="url">{C.LINK}</span></div>""")

def fb_html(i, it):
    kind, head, title, data, src = it[:5]
    blk = data_block(kind, data, '#b03a2e', 0.85).replace(f'border:5px solid {NAVY}', '2px solid #1b1b1b').replace(f'box-shadow:9px 9px 0 {NAVY}', 'box-shadow:none')
    return f"""<html><head><style>*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1350px;overflow:hidden;background:#F4EFE3;color:#1b1b1b;font-family:'DejaVu Serif',serif;position:relative}}
.card{{background:#fff;border:2px solid #1b1b1b;border-radius:6px;font-family:'Inter'}} .url{{font-family:Inter}} em{{font-style:normal}}</style></head><body>
<div style="position:absolute;left:70px;right:70px;top:56px;border-bottom:4px double #1b1b1b;padding-bottom:14px;display:flex;justify-content:space-between;align-items:center"><b style="font-size:48px">La Gazzetta del Motore</b><img src="{logo}" style="height:58px"></div>
<div style="position:absolute;left:70px;right:70px;top:146px;display:flex;justify-content:space-between;font-family:Inter;font-weight:700;font-size:20px;letter-spacing:2px;border-bottom:2px solid #1b1b1b;padding-bottom:10px"><span>EDIZIONE SMILEFIX BROKER</span><span style="color:#b03a2e">{head.upper()}</span><span>NOVEMBRE 2026</span></div>
<h1 style="position:absolute;left:70px;right:70px;top:220px;font-size:76px;line-height:1.06">{title}</h1>
<div style="position:absolute;left:70px;right:70px;top:560px">{blk}</div>
<div style="position:absolute;left:70px;right:70px;bottom:46px;border-top:2px solid #1b1b1b;padding-top:14px;display:flex;justify-content:space-between;font-family:Inter;font-weight:700;font-size:22px"><span>{src}</span><span>{C.LINK}</span></div>
</body></html>"""

def pin_html(i, it):
    d, title, kind, data, src = it[:5]; ac = POP[(i+1) % 5]
    return pop_page(1000, 1500, f"""<div class="card" style="position:absolute;left:56px;right:56px;top:56px;background:{ac};color:#fff;padding:34px 36px">
<div style="font-weight:900;letter-spacing:3px;font-size:24px;opacity:.9">GUIDA SALVABILE</div><h1 style="font-size:70px;margin-top:12px">{title}</h1></div>
<div style="position:absolute;left:56px;right:56px;top:560px">{data_block(kind, data, ac, 0.95)}</div>
<div class="src" style="left:56px;bottom:120px;font-size:22px">{src}</div>
<div style="position:absolute;left:56px;right:56px;bottom:40px;display:flex;justify-content:space-between;align-items:center"><div class="logo" style="position:static"><img src="{logo}"></div><span class="url" style="font-size:24px">{C.LINK}/guide</span></div>""")

def tg_html(it):
    d, title, rows, src = it
    r = ''.join(f'<div style="display:flex;gap:26px;border-bottom:2px dashed #3a3a3a;padding:16px 0"><span style="color:#FF6B57;font-family:DejaVu Sans Mono;font-weight:700;font-size:34px">0{i+1}</span><span style="font-size:36px;font-weight:700">{x}</span></div>' for i, x in enumerate(rows))
    return f"""<html><head><style>*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1080px;overflow:hidden;background:#161616;color:#f2f2f2;font-family:'Inter';position:relative}}</style></head><body>
<div style="position:absolute;left:70px;top:60px;font-family:'DejaVu Sans Mono';color:#FF6B57;font-size:26px;letter-spacing:2px">● BOLLETTINO SMILEFIX</div>
<img src="{logo}" style="position:absolute;right:70px;top:46px;height:66px;background:#fff;border-radius:10px;padding:4px 8px">
<h1 style="position:absolute;left:70px;right:70px;top:130px;font-weight:900;font-size:64px;line-height:1.05;color:#FF6B57">{title}</h1>
<div style="position:absolute;left:70px;right:70px;top:300px">{r}</div>
<div style="position:absolute;left:70px;bottom:46px;font-family:'DejaVu Sans Mono';font-size:24px;color:#9a9a9a">{src}</div></body></html>"""

def story_html(i, it):
    d, kick, q, opts, foot = it; ac = POP[i % 5]
    o = ''.join(f'<div class="card" style="padding:34px 40px;margin-bottom:30px;font-size:58px;font-weight:900">{x}</div>' for x in opts)
    return pop_page(1080, 1920, f"""<div class="logo" style="top:120px;left:70px"><img src="{logo}"></div>
<div style="position:absolute;left:70px;top:330px"><span class="kick" style="font-size:40px;background:{ac};color:#fff">{kick}</span></div>
<h1 style="position:absolute;left:70px;right:70px;top:450px;font-size:120px">{q}</h1>
<div style="position:absolute;left:70px;right:70px;top:900px">{o}</div>
<div style="position:absolute;left:70px;right:70px;bottom:260px;font-size:44px;font-weight:800;color:#33475a">{foot}</div>""")

def scene_html(sc, idx, tot, ac):
    k = sc[0]; head = f'<div class="logo" style="top:90px;left:70px"><img src="{logo}"></div><div style="position:absolute;right:70px;top:100px;font-weight:900;font-size:40px">{idx}/{tot}</div>'
    if k == 'hook':
        body = f'<div style="position:absolute;left:70px;top:520px"><span class="kick" style="font-size:44px">{sc[1]}</span></div><h1 style="position:absolute;left:70px;right:70px;top:660px;font-size:128px">{sc[2]}</h1>'
    elif k == 'meme':
        body = f'<div class="card" style="position:absolute;left:70px;right:70px;top:480px;padding:60px;background:{ac};color:#fff"><div style="font-size:84px;font-weight:900;line-height:1.1">{sc[1]}</div></div><div style="position:absolute;left:70px;right:70px;top:1000px;font-size:92px;font-weight:900;line-height:1.1">{sc[2]}</div>'
    elif k == 'big':
        body = f'<div style="position:absolute;left:70px;top:470px"><span class="kick" style="font-size:40px">{sc[1]}</span></div><div style="position:absolute;left:70px;right:70px;top:600px">{data_block("num", (sc[2], sc[3]), ac, 1.25)}</div>'
    elif k == 'list':
        body = f'<h1 style="position:absolute;left:70px;right:70px;top:430px;font-size:100px">{sc[1]}</h1><div style="position:absolute;left:70px;right:70px;top:700px">{data_block("list", sc[2], ac, 1.45)}</div>'
    elif k == 'bars':
        body = f'<h1 style="position:absolute;left:70px;right:70px;top:430px;font-size:100px">{sc[1]}</h1><div style="position:absolute;left:70px;right:70px;top:700px">{data_block("bars", sc[2], ac, 1.4)}</div><div class="src" style="left:70px;bottom:330px;font-size:34px">Fonte: {sc[3]}</div>'
    elif k == 'vs':
        col = lambda t, items, bg, fg: f'<div class="card" style="padding:44px;margin-bottom:40px;background:{bg};color:{fg}"><div style="font-size:60px;font-weight:900">{t}</div>' + ''.join(f'<div style="font-size:52px;font-weight:700;margin-top:14px">{x}</div>' for x in items) + '</div>'
        body = f'<div style="position:absolute;left:70px;right:70px;top:430px">{col(sc[1], sc[2], "#fff", NAVY)}<div style="text-align:center;font-size:80px;font-weight:900;margin:-10px 0 30px">VS</div>{col(sc[3], sc[4], ac, "#fff")}</div>'
    elif k == 'quiz':
        body = f'<div style="position:absolute;left:70px;top:400px"><span class="kick" style="font-size:44px">Quiz</span></div><h1 style="position:absolute;left:70px;right:70px;top:520px;font-size:96px">{sc[1]}</h1><div style="position:absolute;left:70px;right:70px;top:1020px">{data_block("quiz", ("", sc[2], sc[3]), ac, 1.5)}</div>'
    else:  # cta
        body = f'<h1 style="position:absolute;left:70px;right:70px;top:640px;font-size:128px">{sc[1]}</h1><div class="card" style="position:absolute;left:70px;right:70px;top:1060px;padding:44px;font-size:64px;font-weight:800">{sc[2]}</div>'
    return pop_page(1080, 1920, head + body + f'<div style="position:absolute;left:70px;right:70px;bottom:200px;display:flex;justify-content:flex-end"><span class="url" style="font-size:38px">{C.LINK}</span></div>')

pages = {}
for i, it in enumerate(C.IG): pages[OUT / f'ig_{i+1:02d}.jpg'] = ig_html(i, it)
for i, it in enumerate(C.FB):
    if it: pages[OUT / f'fb_{i+1:02d}.jpg'] = fb_html(i, it)
for i, it in enumerate(C.PIN): pages[OUT / f'pin_{i+1:02d}.jpg'] = pin_html(i, it)
for i, it in enumerate(C.TG): pages[OUT / f'tg_{i+1:02d}.jpg'] = tg_html(it)
for i, it in enumerate(C.ST): pages[OUT / f'story_{i+1:02d}.jpg'] = story_html(i, it)
for vi, v in enumerate(C.TT + C.YT):
    vid, scenes = v[0], v[1]
    for si, sc in enumerate(scenes): pages[SL / f'{vid}_{si}.jpg'] = scene_html(sc, si+1, len(scenes), POP[vi % 5])

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for path, h in pages.items():
        w, hh = map(int, re.search(r'width:(\d+)px;height:(\d+)px', h).groups())
        pg.set_viewport_size({'width': w, 'height': hh}); pg.set_content(h); pg.wait_for_timeout(120)
        pg.screenshot(path=str(path), type='jpeg', quality=88)
    b.close()
print(len(pages), 'immagini')
