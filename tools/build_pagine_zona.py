import json, html, re, pathlib
SITE = pathlib.Path('/tmp/site')
tpl = (SITE/'guide/auto-asta-costi.html').read_text(encoding='utf-8')
style = tpl[tpl.index('<style>'):tpl.index('</style>')+8]
header = '<header class="top"><a href="/"><img src="/img/logo-smilefix.png" alt="SmileFix Broker, broker di auto, moto e veicoli commerciali" width="148" height="74"></a></header>'
footer = tpl[tpl.index('<footer>'):]
e = html.escape
DATE = '2026-11-17'

STEPS = """<h2>Come lavoriamo{loc}</h2>
<ol>
<li><strong>Ci scrivi su WhatsApp</strong> che veicolo cerchi, come lo userai e quanto vuoi spendere.</li>
<li><strong>Cerchiamo noi</strong> tra privati, operatori e aste di veicoli, e scartiamo le occasioni che non convincono.</li>
<li><strong>Verifichiamo prima di proporti</strong>: storia, chilometri, revisioni, documenti e stato del mezzo.</li>
<li><strong>Ti diamo un prezzo chiaro</strong>, tutto compreso, e decidi tu se procedere.</li>
<li><strong>Pensiamo noi</strong> a trattativa, pratiche, passaggio di proprietà e consegna.</li>
</ol>
<p>Il primo confronto e la proposta sono gratuiti e senza impegno. Gran parte del lavoro si fa a distanza: ti muovi solo quando c'è il veicolo giusto.</p>"""

IPT = """<h2>Passaggio di proprietà {prov}: quanto costa</h2>
<p>La voce principale è l'<strong>IPT (Imposta Provinciale di Trascrizione)</strong>. {prov_cap} applica la maggiorazione del 30%, come tutte le province lombarde: per le auto fino a 53 kW sono circa <strong>196 €</strong>, oltre i 53 kW circa <strong>4,56 € per ogni kW</strong> di potenza. A questo si aggiungono emolumenti ACI e diritti della Motorizzazione, circa 85 €.</p>
<table>
<tr><th>Esempio</th><th>IPT indicativa</th></tr>
<tr><td>Utilitaria da 51 kW</td><td>circa 196 €</td></tr>
<tr><td>Auto da 85 kW</td><td>circa 388 €</td></tr>
<tr><td>SUV da 110 kW</td><td>circa 501 €</td></tr>
</table>
<p>Importi indicativi: per il calcolo esatto usa il calcolatore sul sito dell'ACI con la potenza in kW riportata sul libretto. Nelle nostre proposte il passaggio di proprietà è già compreso nel prezzo finale.</p>{extra}"""

CTA = """<div class="box"><strong>Cerchi un veicolo {zona}?</strong> Scrivici cosa ti serve: ti mandiamo una proposta chiara, con il prezzo finale tutto compreso. <a href="https://wa.me/393468866036">Scrivici su WhatsApp</a> oppure <a href="/#richiedi">richiedi una proposta dal sito</a>. Le occasioni dalle aste le pubblichiamo ogni settimana sul nostro <a href="https://whatsapp.com/channel/0029VbDoLQFFSAszyPloQW0h" rel="noopener">canale WhatsApp</a>.</div>"""

PAGES = [
dict(slug='broker-auto-bergamo.html', city='Bergamo',
 title='Broker auto a Bergamo: auto, moto e furgoni con prezzo chiaro',
 seo='Broker auto Bergamo: auto usate, moto e furgoni con prezzo chiaro | SmileFix',
 desc="Broker auto in provincia di Bergamo: cerchiamo e verifichiamo per te auto, moto e furgoni nuovi e usati, anche dalle aste, con un prezzo finale tutto compreso.",
 lead="Siamo di casa in provincia di Bergamo: cerchiamo il veicolo giusto per te, lo verifichiamo e ti seguiamo fino alla consegna.",
 intro="""<p>Comprare un'auto usata a Bergamo e provincia significa spesso passare i weekend tra annunci, telefonate e viaggi a vuoto. SmileFix Broker fa questo lavoro al posto tuo: con oltre 15 anni di esperienza nel settore automotive, tra ricambi, officina, carrozzeria e vendita, cerchiamo <strong>auto, moto, furgoni e veicoli commerciali</strong>, nuovi e usati, e ti proponiamo solo quello che abbiamo controllato.</p>""",
 loc=' a Bergamo e provincia', prov='in provincia di Bergamo', prov_cap='La Provincia di Bergamo',
 rules="""<h2>Prima di comprare un usato a Bergamo: guarda la classe Euro</h2>
<p>Bergamo rientra nella <strong>Fascia 1</strong> delle misure antismog della Regione Lombardia. Nei giorni feriali dalle 7:30 alle 19:30 non possono circolare i veicoli a benzina Euro 0 e 1 e i diesel fino a Euro 4. Per i <strong>diesel Euro 5</strong> lo stop regionale nei comuni sopra i 100.000 abitanti, tra cui Bergamo, è stato rinviato all'autunno 2027.</p>
<div class="box red"><strong>In pratica.</strong> Se usi l'auto ogni giorno in città o nei comuni della cintura, un diesel Euro 4 a buon prezzo oggi può diventare un problema domani. Prima di comprare controlla la classe Euro sul libretto e le regole aggiornate sul sito della Regione Lombardia; per chi percorre pochi km, il servizio regionale Move-In può consentire deroghe a chilometri contati.</div>""",
 extra='',
 faq=[("Lavorate solo a Bergamo città?","No: seguiamo clienti in tutta la provincia di Bergamo e in Lombardia, e cerchiamo il veicolo anche fuori regione quando conviene."),
      ("Devo venire a vedere tutte le auto?","No. Facciamo noi le prime verifiche e ti proponiamo solo i veicoli che superano i controlli: ti muovi solo per quello giusto."),
      ("Quanto costa il servizio?","La prima proposta è gratuita e senza impegno. Nel preventivo trovi un prezzo finale chiaro, tutto compreso, prima di decidere.")]),
dict(slug='broker-auto-milano.html', city='Milano',
 title='Broker auto a Milano: auto usate, moto e furgoni senza sorprese',
 seo='Broker auto Milano: auto usate, moto e furgoni senza sorprese | SmileFix',
 desc="Broker auto per Milano e provincia: cerchiamo e verifichiamo auto, moto e furgoni nuovi e usati compatibili con Area B e Area C, con un prezzo finale tutto compreso.",
 lead="Cerchiamo per te il veicolo giusto per muoverti a Milano, compatibile con Area B e Area C, e ti seguiamo fino alla consegna.",
 intro="""<p>A Milano scegliere un'auto usata non è solo questione di prezzo e chilometri: bisogna anche poterla usare in città. SmileFix Broker cerca per te <strong>auto, moto, furgoni e veicoli commerciali</strong>, nuovi e usati, verifica storia e condizioni e controlla che il veicolo sia adatto alle regole di circolazione milanesi. Oltre 15 anni di esperienza nel settore automotive, al tuo servizio.</p>""",
 loc=' a Milano e provincia', prov='a Milano', prov_cap='La Città Metropolitana di Milano',
 rules="""<h2>Comprare un usato a Milano: Area B e Area C prima di tutto</h2>
<p><strong>Area B</strong> copre gran parte del territorio comunale ed è attiva nei giorni feriali dalle 7:30 alle 19:30. Le regole a novembre 2026, in sintesi:</p>
<table>
<tr><th>Alimentazione</th><th>Situazione in Area B</th></tr>
<tr><td>Diesel</td><td>Esclusi fino a Euro 5 compreso (con deroghe a giornate o chilometri in casi specifici)</td></tr>
<tr><td>Benzina</td><td>Esclusi fino a Euro 3 compreso; gli Euro 4 sono previsti in uscita da ottobre 2028</td></tr>
<tr><td>Elettriche e ibride</td><td>Ammesse; in Area C le ibride entrano gratis solo sotto certi limiti di emissioni</td></tr>
</table>
<div class="box red"><strong>Attenzione agli affari troppo belli.</strong> Molti diesel Euro 5 e benzina Euro 3 in vendita a buon prezzo arrivano proprio da chi non può più usarli a Milano. Prima di comprare controlla classe Euro e alimentazione sul libretto e il calendario aggiornato dei divieti sul sito del Comune di Milano.</div>""",
 extra='',
 faq=[("Mi aiutate a scegliere un'auto compatibile con Area B?","Sì: la compatibilità con Area B e Area C è uno dei primi filtri che applichiamo nella ricerca, insieme a budget, uso e consumi."),
      ("Cercate anche fuori Milano?","Sì. Spesso le occasioni migliori sono in provincia o in altre regioni: le verifichiamo noi e ti muovi solo per il veicolo giusto."),
      ("Seguite anche furgoni per lavoro?","Sì, cerchiamo furgoni e veicoli commerciali per artigiani e aziende, tenendo conto anche delle regole di accesso in città.")]),
dict(slug='broker-auto-brescia.html', city='Brescia',
 title='Broker auto a Brescia: auto, moto e furgoni verificati',
 seo='Broker auto Brescia: auto, moto e furgoni verificati | SmileFix',
 desc="Broker auto per Brescia e provincia: cerchiamo e verifichiamo auto, moto, furgoni e mezzi da lavoro nuovi e usati, anche dalle aste, con un prezzo finale chiaro.",
 lead="Auto per la famiglia, moto o furgoni per il lavoro: li cerchiamo e verifichiamo noi, con un prezzo finale chiaro prima di decidere.",
 intro="""<p>La provincia di Brescia è una delle più attive d'Italia per artigiani, imprese e trasporti, e i veicoli da lavoro hanno regole e costi propri. SmileFix Broker cerca per te <strong>auto, moto, furgoni e veicoli commerciali</strong>, nuovi e usati, anche dalle aste, e verifica ogni mezzo prima di proportelo. Oltre 15 anni di esperienza nel settore automotive, dall'officina alla vendita.</p>""",
 loc=' a Brescia e provincia', prov='in provincia di Brescia', prov_cap='La Provincia di Brescia',
 rules="""<h2>Prima di comprare un usato a Brescia: classe Euro e uso</h2>
<p>Brescia rientra nella <strong>Fascia 1</strong> delle misure antismog della Regione Lombardia: nei giorni feriali dalle 7:30 alle 19:30 non possono circolare i veicoli a benzina Euro 0 e 1 e i diesel fino a Euro 4. Per i <strong>diesel Euro 5</strong> lo stop regionale nei comuni sopra i 100.000 abitanti, tra cui Brescia, è stato rinviato all'autunno 2027.</p>
<div class="box red"><strong>Per chi lavora con il furgone.</strong> Anche per i veicoli commerciali le limitazioni antismog arrivano per gradi: prima di comprare un furgone diesel usato valuta per quanti anni potrai usarlo nelle zone in cui lavori. Le regole aggiornate sono sul sito della Regione Lombardia.</div>""",
 extra="""
<p><strong>Una particolarità bresciana:</strong> la Provincia di Brescia prevede regole agevolate di IPT per alcuni veicoli usati da aziende di noleggio, di trasporto pubblico locale e di autotrasporto merci per conto terzi. Se sei un'azienda del settore, verificale prima del passaggio.</p>""",
 faq=[("Cercate anche furgoni e mezzi da lavoro?","Sì: furgoni, van e veicoli commerciali per artigiani e aziende sono una parte importante del nostro lavoro, anche da aste e flotte."),
      ("Lavorate in tutta la provincia di Brescia?","Sì, e cerchiamo il veicolo anche fuori provincia quando conviene. Le prime verifiche le facciamo noi."),
      ("Il prezzo che mi date cambia dopo?","No: nella proposta trovi il prezzo finale tutto compreso, con passaggio di proprietà e pratiche, prima di decidere.")]),
]

def build(p):
    url = 'https://smilefixbroker.com/' + p['slug']
    ld = [
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
       {"@type":"ListItem","position":1,"name":"Home","item":"https://smilefixbroker.com/"},
       {"@type":"ListItem","position":2,"name":f"Broker auto {p['city']}","item":url}]},
     {"@context":"https://schema.org","@type":"Service","name":f"Broker auto a {p['city']}","serviceType":"Broker auto / consulenza acquisto veicoli",
      "description":p['desc'],"url":url,"provider":{"@id":"https://smilefixbroker.com/#org","@type":"Organization","name":"SmileFix Broker","url":"https://smilefixbroker.com/"},
      "areaServed":[{"@type":"City","name":p['city']},{"@type":"AdministrativeArea","name":f"Provincia di {p['city']}" if p['city']!='Milano' else "Città metropolitana di Milano"}]},
     {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p['faq']]},
    ]
    others = [x for x in PAGES if x is not p]
    rel = '<section class="related"><h2>Altre zone e guide utili</h2><ul>' + ''.join(f'<li><a href="/{o["slug"]}">Broker auto a {o["city"]}</a></li>' for o in others) + \
          '<li><a href="/guide/asta-auto-giudiziaria-come-funziona.html">Asta auto giudiziaria: come funziona, passo per passo</a></li><li><a href="/guide/controlli-auto-usata-checklist.html">Cosa controllare quando vai a vedere un\'auto usata</a></li></ul></section>'
    faq = '<section class="faq"><h2>Domande frequenti</h2>' + ''.join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q,a in p['faq']) + '</section>'
    body = (p['intro'] + STEPS.format(loc=p['loc']) + p['rules'] + IPT.format(prov=p['prov'], prov_cap=p['prov_cap'], extra=p['extra'])
            + CTA.format(zona=p['loc'].replace(' a ', 'a ', 1).strip()))
    out = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['seo'])}</title>
<meta name="description" content="{e(p['desc'])}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:site_name" content="SmileFix Broker">
<meta property="og:title" content="{e(p['seo'])}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://smilefixbroker.com/img/logo-smilefix.png">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{style}
</head>
<body>
{header}
<nav class="crumb" aria-label="Percorso"><a href="/">Home</a> › Broker auto {e(p['city'])}</nav>
<main>
<article>
<h1>{e(p['title'])}</h1>
<p class="lead">{e(p['lead'])}</p>
<p class="meta">SmileFix Broker · Aggiornato il 17 novembre 2026</p>
{body}
{rel}{faq}
</article>
</main>
{footer}"""
    (SITE/p['slug']).write_text(out, encoding='utf-8'); print('written', p['slug'], len(out))

for p in PAGES: build(p)

# home footer: add zones to "Servizio" column
hi = SITE/'index.html'; t = hi.read_text(encoding='utf-8')
if 'broker-auto-bergamo' not in t:
    zones = '<div><h4>Zone</h4><ul><li><a href="/broker-auto-bergamo.html">Broker auto Bergamo</a></li><li><a href="/broker-auto-milano.html">Broker auto Milano</a></li><li><a href="/broker-auto-brescia.html">Broker auto Brescia</a></li></ul></div>\n      '
    t = t.replace('<div><h4>Risorse</h4>', zones + '<div><h4>Risorse</h4>', 1)
    hi.write_text(t, encoding='utf-8'); print('home zones')
# guide index + guide footers: add small zone links line in footer of guides
for f in list((SITE/'guide').glob('*.html')) + [SITE/'faq.html', SITE/'chi-siamo.html']:
    t = f.read_text(encoding='utf-8')
    if 'broker-auto-bergamo' in t: continue
    marker = '<p style="margin-top:10px"><a href="/chi-siamo.html">Chi siamo</a>'
    if marker in t:
        t = t.replace(marker, '<p style="margin-top:10px">Zone: <a href="/broker-auto-bergamo.html">Bergamo</a> · <a href="/broker-auto-milano.html">Milano</a> · <a href="/broker-auto-brescia.html">Brescia</a></p>\n' + marker, 1)
        f.write_text(t, encoding='utf-8'); print('footer zones', f.name)
sm = SITE/'sitemap.xml'; t = sm.read_text(encoding='utf-8')
for p in PAGES:
    u = 'https://smilefixbroker.com/' + p['slug']
    if u not in t: t = t.replace('</urlset>', f'  <url><loc>{u}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>')
sm.write_text(t, encoding='utf-8')
ll = SITE/'llms.txt'; t = ll.read_text(encoding='utf-8')
if 'broker-auto-bergamo' not in t:
    t = t.rstrip('\n') + '\n\n## Zone servite\n' + ''.join(f"- [Broker auto a {p['city']}](https://smilefixbroker.com/{p['slug']})\n" for p in PAGES)
    ll.write_text(t, encoding='utf-8')
print('done')
