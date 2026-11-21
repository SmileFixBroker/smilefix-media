import json, html, re, pathlib
SITE = pathlib.Path('/tmp/site')
tpl = (SITE / 'guide/auto-asta-costi.html').read_text(encoding='utf-8')

SLUG = 'asta-auto-giudiziaria-come-funziona.html'
URL = 'https://smilefixbroker.com/guide/' + SLUG
TITLE = "Asta auto giudiziaria: come funziona, passo per passo"
SEO_TITLE = "Asta auto giudiziaria: come funziona, passo per passo | SmileFix"
DESC = ("Dove trovare le aste giudiziarie di auto, moto e furgoni, come leggere l'avviso di vendita, "
        "quanto vale la cauzione, come si fa l'offerta e cosa succede dopo l'aggiudicazione.")
LEAD = ("Dall'avviso di vendita al ritiro del veicolo: le tappe di un'asta giudiziaria spiegate in modo semplice, "
        "con gli errori da evitare e una checklist prima di offrire.")
DATE = '2026-11-17'

FAQ = [
 ("Chi può partecipare a un'asta giudiziaria di auto?",
  "In generale possono partecipare sia i privati sia le aziende. Le modalità precise (offerta online o cartacea, eventuale delega a un'altra persona) sono indicate nell'avviso di vendita di ogni lotto."),
 ("Quanto è la cauzione e viene restituita?",
  "Di solito la cauzione è pari ad almeno il 10% del prezzo offerto, ma l'importo esatto è indicato nell'avviso. Se non ti aggiudichi il veicolo viene restituita; se vinci viene scalata dal prezzo. Se poi non paghi il saldo entro il termine, rischi di perderla."),
 ("Si può provare l'auto prima dell'asta?",
  "Di norma no: si può solo vedere il veicolo nelle giornate di visione indicate nell'avviso, spesso a motore spento. Per questo conviene farsi accompagnare da chi sa valutare un'auto a colpo d'occhio."),
 ("C'è garanzia su un'auto comprata a un'asta giudiziaria?",
  "No. La vendita avviene nello stato di fatto in cui il veicolo si trova («visto e piaciuto»), senza garanzia per vizi o difetti. Va messo in conto nel prezzo massimo che decidi di offrire."),
]

BODY = """
<p>In un'asta giudiziaria il veicolo viene venduto nell'ambito di una procedura del tribunale: un'esecuzione forzata, un fallimento o una liquidazione. La vendita è seguita da un professionista o da un soggetto incaricato dalla procedura, con regole scritte e uguali per tutti. È un canale in cui si trovano <strong>auto, moto, furgoni e mezzi da lavoro</strong> anche sotto il prezzo di mercato, ma solo se si conoscono le regole e si fanno bene i conti.</p>

<h2>1. Dove si trovano le aste giudiziarie di veicoli</h2>
<p>La fonte ufficiale è il <strong>Portale delle Vendite Pubbliche</strong> del Ministero della Giustizia, dove ogni vendita è pubblicata con l'avviso, la perizia o la scheda del bene e le regole di partecipazione. Gli stessi lotti compaiono anche sui siti dei gestori delle vendite autorizzati, che spesso ospitano la gara online.</p>
<div class="box"><strong>Consiglio.</strong> Partecipa solo tramite i canali indicati nell'avviso di vendita. Diffida di chi ti chiede di pagare la cauzione o il prezzo su conti diversi da quelli indicati nella documentazione ufficiale.</div>

<h2>2. Leggere l'avviso di vendita (la parte più importante)</h2>
<p>L'avviso di vendita è il «contratto» dell'asta: tutto quello che conta è scritto lì. Prima di innamorarti di un'auto, cerca queste informazioni:</p>
<table>
<tr><th>Cosa cercare</th><th>Perché conta</th></tr>
<tr><td><strong>Prezzo base e offerta minima</strong></td><td>Spesso si può offrire meno del prezzo base (per esempio fino al 75%), ma solo entro il limite indicato.</td></tr>
<tr><td><strong>Cauzione</strong></td><td>Di solito almeno il 10% del prezzo offerto, da versare prima della gara con le modalità indicate.</td></tr>
<tr><td><strong>Rilancio minimo</strong></td><td>L'importo minimo di ogni rilancio durante la gara.</td></tr>
<tr><td><strong>IVA, diritti e spese</strong></td><td>Se il prezzo è «+ IVA» e quali commissioni e spese paga chi vince: cambiano molto il costo finale.</td></tr>
<tr><td><strong>Termine per il saldo</strong></td><td>Entro quanti giorni va pagato il resto del prezzo dopo l'aggiudicazione.</td></tr>
<tr><td><strong>Documenti e chiavi</strong></td><td>Se ci sono libretto, certificato di proprietà e chiavi: se mancano, servono pratiche e spese in più.</td></tr>
<tr><td><strong>Ritiro del veicolo</strong></td><td>Dove e entro quando ritirarlo; oltre il termine possono scattare costi di custodia.</td></tr>
</table>

<h2>3. Vedere il veicolo</h2>
<p>Quasi sempre è prevista una <strong>giornata di visione</strong>, su appuntamento. Di solito non si può fare la prova su strada e spesso l'auto non viene nemmeno accesa. Guarda carrozzeria, interni, gomme, eventuali perdite sotto il motore e i segni di urti riparati male: la <a href="/guide/controlli-auto-usata-checklist.html">checklist in 5 zone</a> ti aiuta a non dimenticare nulla. Con la targa puoi controllare a casa revisioni e chilometri (vedi la <a href="/guide/km-scalati-auto-usata.html">guida sui km scalati</a>).</p>

<h2>4. Registrarsi e fare l'offerta</h2>
<ol>
<li><strong>Registrati</strong> sul portale indicato nell'avviso (per le vendite telematiche).</li>
<li><strong>Versa la cauzione</strong> nei tempi e nei modi indicati (bonifico o altro metodo previsto).</li>
<li><strong>Presenta l'offerta</strong> entro la scadenza: online con il modulo previsto oppure, dove ammesso, in busta chiusa.</li>
<li><strong>Conserva le ricevute</strong>: cauzione, offerta e comunicazioni del portale.</li>
</ol>
<div class="box"><strong>Regola d'oro.</strong> Decidi prima il tuo <strong>prezzo massimo tutto compreso</strong> (aggiudicazione + diritti + IVA se dovuta + passaggio di proprietà + trasporto + rimessa in strada) e non superarlo durante i rilanci. Per calcolarlo usa la guida <a href="/guide/auto-asta-costi.html">quanto costa davvero un'auto all'asta</a>.</div>

<h2>5. La gara e l'aggiudicazione</h2>
<p>Se ci sono più offerte si apre la gara: online può essere <strong>sincrona</strong> (tutti collegati nello stesso momento) o <strong>asincrona</strong> (rilanci in un periodo di tempo, spesso con proroga se arrivano offerte negli ultimi minuti). Vince chi offre di più. Se non vinci, la cauzione ti viene restituita.</p>

<h2>6. Dopo l'aggiudicazione: saldo, documenti e passaggio di proprietà</h2>
<ul>
<li><strong>Saldo del prezzo</strong> entro il termine dell'avviso, insieme a diritti e spese: se non paghi in tempo rischi di perdere la cauzione.</li>
<li><strong>Documenti</strong>: ricevi quanto serve per intestare il veicolo (atto di vendita o provvedimento della procedura).</li>
<li><strong>Passaggio di proprietà</strong> al PRA a tuo nome: il costo principale è l'IPT, che dipende da kW e provincia.</li>
<li><strong>Gravami</strong> (fermi, ipoteche): verifica nell'avviso come e da chi vengono cancellati e fai una visura PRA aggiornata prima del ritiro.</li>
<li><strong>Ritiro</strong> entro la data indicata, con carrello o bisarca se il mezzo non può circolare.</li>
</ul>
<div class="box red"><strong>Gli errori più comuni.</strong> Offrire senza aver letto l'avviso; dimenticare diritti e IVA nel conto; non considerare documenti o chiavi mancanti; farsi prendere dai rilanci; non avere i soldi pronti per il saldo nei tempi richiesti.</div>

<h2>7. Prima di offrire: la checklist</h2>
<ol>
<li>Ho letto tutto l'avviso di vendita e la scheda del veicolo.</li>
<li>So se il prezzo è con IVA o «+ IVA» e quanto sono diritti e spese.</li>
<li>Ho visto il veicolo (o l'ha visto qualcuno di fiducia).</li>
<li>Ho controllato revisioni e chilometri con la targa.</li>
<li>Ho calcolato passaggio di proprietà, trasporto e rimessa in strada.</li>
<li>Ho confrontato il totale con il <strong>valore di mercato</strong> di veicoli simili.</li>
<li>Ho fissato un'offerta massima e ho i soldi pronti per cauzione e saldo.</li>
</ol>

<div class="box"><strong>Vuoi partecipare senza pensieri?</strong> Con SmileFix Broker scegli il veicolo e prima dell'asta ti diciamo <strong>quanto ti costa consegnato, tutto compreso</strong>; poi seguiamo noi offerta, pratiche e ritiro. Le occasioni le pubblichiamo ogni settimana sul nostro <a href="https://whatsapp.com/channel/0029VbDoLQFFSAszyPloQW0h" rel="noopener">canale WhatsApp</a>. <a href="/">Scopri il servizio</a> oppure <a href="https://wa.me/393468866036">scrivici su WhatsApp</a>.</div>
"""

RELATED = [
 ('/guide/auto-asta-costi.html', "Auto all'asta: quanto costa davvero (oltre al prezzo di aggiudicazione)"),
 ('/guide/km-scalati-auto-usata.html', 'Km scalati: come scoprirli da casa con la sola targa'),
 ('/guide/controlli-auto-usata-checklist.html', "Cosa controllare quando vai a vedere un'auto usata: la checklist"),
]

e = html.escape
head_end = tpl.index('<style>')
style_to_body = tpl[head_end:tpl.index('<main>')]
footer = tpl[tpl.index('<footer>'):]

ld = [
 {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
   {"@type":"ListItem","position":1,"name":"Home","item":"https://smilefixbroker.com/"},
   {"@type":"ListItem","position":2,"name":"Guide","item":"https://smilefixbroker.com/guide/"},
   {"@type":"ListItem","position":3,"name":TITLE,"item":URL}]},
 {"@context":"https://schema.org","@type":"Article","headline":TITLE,"description":DESC,"inLanguage":"it-IT",
  "datePublished":DATE,"dateModified":DATE,"mainEntityOfPage":URL,
  "image":"https://smilefixbroker.com/img/guida-auto-usata-vol1.jpg",
  "author":{"@type":"Organization","name":"SmileFix Broker","url":"https://smilefixbroker.com/"},
  "publisher":{"@type":"Organization","name":"SmileFix Broker","url":"https://smilefixbroker.com/",
    "logo":{"@type":"ImageObject","url":"https://smilefixbroker.com/img/logo-smilefix.png"}},
  "keywords":"asta auto giudiziaria, aste giudiziarie auto, come partecipare asta giudiziaria, cauzione asta, portale vendite pubbliche, comprare auto all'asta"},
 {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
   {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]},
]

head = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(SEO_TITLE)}</title>
<meta name="description" content="{e(DESC)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="article">
<meta property="og:locale" content="it_IT">
<meta property="og:site_name" content="SmileFix Broker">
<meta property="og:title" content="{e(SEO_TITLE)}">
<meta property="og:description" content="{e(DESC)}">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="https://smilefixbroker.com/img/guida-auto-usata-vol1.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="me" href="https://mastodon.social/@SmileFixBroker">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
"""
style_to_body = style_to_body.replace(
  "› Auto all&#x27;asta: quanto costa davvero (oltre al prezzo di aggiudicazione)</nav>", f"› {e(TITLE)}</nav>")
assert e(TITLE) in style_to_body
rel = '<section class="related"><h2>Leggi anche</h2><ul>' + ''.join(f'<li><a href="{h}">{e(t)}</a></li>' for h,t in RELATED) + '</ul></section>'
faq = '<section class="faq"><h2>Domande frequenti</h2>' + ''.join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q,a in FAQ) + '</section>'
main = f"""<main>
<article>
<h1>{e(TITLE)}</h1>
<p class="lead">{e(LEAD)}</p>

<p class="meta">A cura di SmileFix Broker · Aggiornato il 17 novembre 2026 · Lettura: 7 minuti</p>
{BODY}
{rel}{faq}
</article>
</main>
"""
out = head + style_to_body + main + footer
(SITE/'guide'/SLUG).write_text(out, encoding='utf-8')
print('written', len(out))

# --- link from other pages ---
link_li = f'<li><a href="/guide/{SLUG}">{e(TITLE)}</a></li>'
for f in ['auto-asta-costi.html','km-scalati-auto-usata.html','domande-venditore-auto-usata.html','controlli-auto-usata-checklist.html']:
    p = SITE/'guide'/f; t = p.read_text(encoding='utf-8')
    if SLUG not in t:
        t = t.replace('<section class="related"><h2>Leggi anche</h2><ul>', '<section class="related"><h2>Leggi anche</h2><ul>' + link_li, 1)
        p.write_text(t, encoding='utf-8'); print('related ->', f)

gi = SITE/'guide/index.html'; t = gi.read_text(encoding='utf-8')
if SLUG not in t:
    card = f'<a class="card" href="/guide/{SLUG}"><b>{e(TITLE)}</b><span>{e(DESC)}</span></a>'
    t = t.replace('<div class="cards">', '<div class="cards">' + card, 1); gi.write_text(t, encoding='utf-8'); print('guide index')

hi = SITE/'index.html'; t = hi.read_text(encoding='utf-8')
if SLUG not in t:
    card = f'        <a class="g-card" href="/guide/{SLUG}"><b>Asta auto giudiziaria: come funziona</b><span>Avviso di vendita, cauzione, offerta e passaggio di proprietà, passo per passo.</span></a>\n'
    t = t.replace('      <div class="guide-grid">\n', '      <div class="guide-grid">\n' + card, 1)
    hi.write_text(t, encoding='utf-8'); print('home')

sm = SITE/'sitemap.xml'; t = sm.read_text(encoding='utf-8')
if SLUG not in t:
    t = t.replace('</urlset>', f'  <url><loc>{URL}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>')
    t = re.sub(r'(<loc>https://smilefixbroker.com/guide/</loc><lastmod>)[^<]+', r'\g<1>'+DATE, t)
    t = re.sub(r'(<loc>https://smilefixbroker.com/</loc><lastmod>)[^<]+', r'\g<1>'+DATE, t)
    sm.write_text(t, encoding='utf-8'); print('sitemap')

ll = SITE/'llms.txt'; t = ll.read_text(encoding='utf-8')
if SLUG not in t:
    anchor = "- [Cosa controllare quando vai a vedere un'auto usata](https://smilefixbroker.com/guide/controlli-auto-usata-checklist.html)"
    add = "\n- [Auto all'asta: quanto costa davvero](https://smilefixbroker.com/guide/auto-asta-costi.html)" if 'auto-asta-costi' not in t else ''
    t = t.replace(anchor, anchor + add + f"\n- [Asta auto giudiziaria: come funziona]({URL})")
    ll.write_text(t, encoding='utf-8'); print('llms')
