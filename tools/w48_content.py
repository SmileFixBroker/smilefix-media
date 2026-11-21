# -*- coding: utf-8 -*-
"""Settimana 23-29 novembre 2026. Dati verificati il 21/11/2026.
 LUN 23 Mercato auto nuove ottobre 2026: UNRAE su dati MIT (L'Automobile ACI, Motorbox, Fleetime, Carx, La Discussione)
 MAR 24 Usato ottobre 2026: ACI Auto-Trend (aci.gov.it 6/11/2026, LSDI, DealerLink)
 MER 25 Parco circolante: studio UNRAE su dati ACI 2011-2025 (L'Automobile ACI, Motorbox, Think.it)
 GIO 26 Carburanti: Osservatorio prezzi MIMIT (2/11 Geagency; 20/11 Soldionline)
 VEN 27 Gomme invernali: periodo 15/11-15/4 su strade con ordinanza (MIT, Motor1, Unipolmove, alVolante, Quattroruote)
Regole: niente prezzi di riparazione/servizio, niente luogo d'asta, niente nome/indirizzo, niente "gratis" sul Vol. 3 (promo non confermata).
"""
S_UN = "Fonte: UNRAE su dati MIT, ottobre 2026"
S_ACI = "Fonte: ACI, Auto-Trend ottobre 2026"
S_PARCO = "Fonte: UNRAE su dati ACI, parco 2011-2025"
S_MIMIT = "Fonte: Osservatorio prezzi MIMIT, novembre 2026"
S_GOM = "Fonte: MIT, periodo 15 novembre - 15 aprile"
S_SF = "SmileFix · consiglio pratico"
AMZ3 = "https://www.amazon.it/dp/B0HSFHS1JD"
LINK = "smilefixbroker.com"

DAYS = ["2026-11-23", "2026-11-24", "2026-11-25", "2026-11-26", "2026-11-27"]

# ---------- INSTAGRAM (pop sticker) ----------
# (kind, kick, title, data, source, caption, tags)
IG = [
 # LUN 23 - auto nuove
 ("num", "MERCATO OTTOBRE", "Auto nuove vendute<br>a ottobre", ("131.921", "+4,8% su ottobre 2025"), S_UN,
  "131.921 auto nuove immatricolate a ottobre in Italia: +4,8% in un anno 📈\n\nDa gennaio siamo a 1,4 milioni, +8,3%. Il mercato si muove, ma resta sotto i livelli del 2019.\n\nTu l'auto nuova la compreresti adesso o aspetti? 👇", "#mercatoauto #autonuove #unrae"),
 ("bars", "COSA SI COMPRA", "Le alimentazioni<br>più scelte a ottobre", [("Ibride", 49, "49%"), ("Plug-in", 12.7, "12,7%"), ("GPL", 9, "9%"), ("Elettriche", 6.1, "6,1%")], S_UN,
  "Ottobre: quasi un'auto nuova su due è ibrida (49%) ⚡⛽\n\nLe plug-in salgono al 12,7%, le elettriche pure restano al 6,1%.\n\n📌 Salva il post: ti serve quando scegli la prossima auto.", "#ibrido #elettrico #plugin"),
 ("quiz", "QUIZ", "L'auto nuova più venduta<br>a ottobre?", ("indovina", ["Jeep Avenger", "Fiat Panda", "Dacia Sandero"], 1), S_UN,
  "Quiz lampo ⏱️ Qual è stata l'auto nuova più venduta in Italia a ottobre?\n\nRisposta: la FIAT PANDA, sempre prima. Sul podio anche la Jeep Avenger.\n\nL'avevi indovinato?", "#quiz #fiatpanda #curiosita"),
 ("vs", "2026 VS 2019", "Il mercato è tornato<br>ai livelli di prima?", (("Stima 2026", "1,64 mln"), ("Rispetto al 2019", "−14,4%")), S_UN,
  "UNRAE stima 1.640.000 auto nuove vendute nel 2026: +7,5% sul 2025 📊\n\nMa rispetto al 2019 mancano ancora il 14,4%. Si compra di più, non ancora come prima.\n\nSecondo te perché? Prezzi, incertezza o motori?", "#mercatoauto #dati #italia"),
 ("book", "È USCITO", "Vol. 3: decidere<br>e firmare", ("3", "trattativa, pagamento, passaggio"), "Guide da tasca SmileFix · Amazon",
  "📘 È uscito su Amazon il Vol. 3 delle Guide da tasca SmileFix: «Decidere e firmare».\n\nIl semaforo per decidere, la trattativa, il pagamento sicuro e il passaggio di proprietà.\n\n🔎 Link in bio o cerca «Decidere e firmare SmileFix».", "#libri #kindle #autousata"),
 # MAR 24 - usato
 ("num", "USATO OTTOBRE", "Ogni 100 auto nuove<br>quante usate?", ("212", "usate vendute ogni 100 nuove"), S_ACI,
  "A ottobre, ogni 100 auto nuove vendute ne sono passate di mano 212 usate 🚗🚗\n\nL'usato resta il mercato principale in Italia. E chi compra usato ha bisogno di sapere cosa guardare.\n\n📌 Salva il post.", "#autousate #aci #mercatoauto"),
 ("num", "IN CALO", "Passaggi di proprietà<br>auto a ottobre", ("292.138", "−6,3% su ottobre 2025"), S_ACI,
  "292.138 passaggi di proprietà di auto a ottobre: −6,3% in un anno 📉\n\nIl mercato dell'usato rallenta un po'. Momento buono per trattare? Dimmi la tua 👇", "#passaggiodiproprieta #autousate #dati"),
 ("num", "VINTAGE?", "Auto passate di mano<br>con almeno 20 anni", ("19,3%", "quasi 1 su 5"), S_ACI,
  "Quasi un'auto usata venduta su cinque ha almeno 20 anni (19,3%) 👴🚗\n\nAuto vecchie, budget bassi. Ma su un'auto così il controllo prima dell'acquisto vale doppio.\n\nTu compreresti un'auto di 20 anni?", "#autodepoca #autousate #consigli"),
 ("num", "BOOM IBRIDE", "Ibride a benzina<br>nell'usato", ("12,7%", "dei passaggi, +15,9% in un anno"), S_ACI,
  "Anche nell'usato crescono le ibride: 12,7% dei passaggi di ottobre, +15,9% in un anno 🔋\n\nPrima di comprarne una usata, chiedi sempre lo stato della batteria ibrida e i tagliandi.\n\n📌 Salva per quando ti servirà.", "#ibrido #autousate #batteria"),
 # MER 25 - parco vecchio
 ("num", "ETÀ MEDIA", "Quanti anni ha<br>un'auto in Italia?", ("13,2", "anni di media (erano 8,5 nel 2011)"), S_PARCO,
  "13,2 anni: l'età media di un'auto in Italia 🕰️\n\nNel 2011 era 8,5. In 14 anni le auto sono aumentate (da 37,1 a 41,8 milioni) e sono invecchiate parecchio.\n\nLa tua quanti anni ha? Scrivilo 👇", "#parcoauto #etamedia #unrae"),
 ("num", "OVER 20", "Auto in giro con<br>più di 20 anni", ("10,7 mln", "il 25,6% del parco"), S_PARCO,
  "10,7 milioni di auto in Italia hanno più di 20 anni: una su quattro 😳\n\nSicurezza, emissioni, ricambi: un parco così vecchio pesa su tutti.\n\nTagga chi ha ancora l'auto dei primi anni 2000 👇", "#autovecchie #sicurezza #parcoauto"),
 ("bars", "SUD VS NORD", "Dove le auto<br>sono più vecchie", [("Sicilia, Calabria, Campania", 19, "oltre 19 anni"), ("Media Italia", 13.2, "13,2 anni")], S_PARCO,
  "In Sicilia, Calabria e Campania l'età media delle auto supera i 19 anni 🗺️\n\nLa media italiana è 13,2. Nella tua regione come va? Scrivila nei commenti.", "#regioni #parcoauto #italia"),
 ("quiz", "QUIZ", "Senza le auto a noleggio<br>l'età media è…", ("indovina", ["11 anni", "13,2 anni", "15,6 anni"], 2), S_PARCO,
  "Quiz 🤔 Se togli dal conto le auto a noleggio (nuove e cambiate spesso), quanti anni ha in media un'auto italiana?\n\nRisposta: 15,6 ANNI.\n\nL'avresti detto?", "#quiz #auto #curiosita"),
 ("num", "OCCHIO", "Auto vecchia comprata usata:<br>cosa guardare", ("3", "ruggine · tagliandi · km veri"), S_SF,
  "Stai guardando un'auto di più di 15 anni? 3 cose da non saltare 👇\n\n🔎 ruggine sotto e nei passaruota\n📒 tagliandi e libretto\n📊 km controllati sul Portale dell'Automobilista\n\n📌 Salva e manda a chi sta cercando.", "#autousata #checklist #consigli"),
 # GIO 26 - carburanti
 ("num", "BENZINA", "Prezzo medio self<br>il 20 novembre", ("1,945 €", "al litro, rete stradale"), S_MIMIT,
  "Benzina self a 1,945 €/litro di media il 20 novembre ⛽\n\nIl 2 novembre era a 2,010: in meno di tre settimane 6,5 centesimi in meno.\n\nTu dove fai benzina? Self, servito o autostrada?", "#benzina #carburanti #mimit"),
 ("vs", "DIESEL VS BENZINA", "Chi costa di più<br>alla pompa?", (("Benzina", "1,945 €"), ("Gasolio", "2,199 €")), S_MIMIT,
  "Oggi il gasolio costa più della benzina: 2,199 € contro 1,945 € al litro (self, 20/11) 😮\n\nQuasi 25 centesimi di differenza. Se fai pochi km, il diesel conviene ancora?\n\nDimmi la tua 👇", "#diesel #benzina #carburanti"),
 ("quiz", "QUIZ", "In autostrada la benzina<br>costa…", ("rispetto alla rete stradale", ["Uguale", "Di meno", "Di più"], 2), S_MIMIT,
  "Quiz ⛽ In autostrada la benzina self costa più o meno che sulla rete normale?\n\nRisposta: DI PIÙ. Il 20/11 la media in autostrada era 1,976 € contro 1,945 €.\n\nUn pieno prima di entrare = qualche euro risparmiato.", "#autostrada #quiz #benzina"),
 ("num", "IN CALO", "Gasolio: quanto è sceso<br>in novembre", ("−4,1 cent", "da 2,240 a 2,199 €/l"), S_MIMIT,
  "Gasolio self: dal 2 al 20 novembre è sceso da 2,240 a 2,199 €/litro ⬇️\n\nCala, ma resta sopra i 2 euro. E per chi compra un'auto usata, il carburante è una spesa da mettere nel conto.", "#gasolio #carburanti #risparmio"),
 ("num", "CONSIGLIO", "Comprare usato:<br>calcola il costo vero", ("4", "carburante · bollo · RC · tagliandi"), S_SF,
  "Il prezzo dell'auto è solo l'inizio 💶\n\nPrima di comprare calcola anche:\n⛽ carburante (km all'anno × consumo)\n🧾 bollo\n🛡️ RC auto\n🔧 tagliandi\n\n📌 Salva: è la lista che pochi fanno.", "#autousata #costi #consigli"),
 # VEN 27 - gomme invernali
 ("num", "SCATTATO L'OBBLIGO", "Gomme invernali<br>o catene a bordo", ("15/11 → 15/4", "sulle strade con ordinanza"), S_GOM,
  "Dal 15 novembre al 15 aprile, sulle strade con ordinanza servono gomme invernali (o 4 stagioni M+S) oppure catene a bordo ❄️\n\nVale anche se non nevica.\n\nTu le hai già montate?", "#gommeinvernali #catene #inverno"),
 ("quiz", "QUIZ", "Gomme invernali con codice<br>di velocità più basso: fino a…", ("quando puoi tenerle?", ["15 aprile", "15 maggio", "Tutto l'anno"], 1), S_GOM,
  "Quiz ❄️ Fino a quando puoi tenere le invernali con indice di velocità più basso di quello del libretto?\n\nRisposta: 15 MAGGIO (un mese di tolleranza). Dopo rischi una multa da 155 a 624 €.\n\n📌 Salva il promemoria.", "#gomme #quiz #multe"),
 ("bars", "INDICE DI VELOCITÀ", "Le lettere<br>sul fianco della gomma", [("Q", 160, "160 km/h"), ("S", 180, "180 km/h"), ("T", 190, "190 km/h"), ("H", 210, "210 km/h")], "Fonte: codici di velocità degli pneumatici",
  "Quella lettera sul fianco della gomma è l'indice di velocità 🔤\n\nQ = 160, S = 180, T = 190, H = 210 km/h. Sulle invernali non può essere inferiore a Q.\n\n📌 Salva e controlla le tue.", "#gomme #pneumatici #consigli"),
 ("num", "AUTO USATA", "Gomme di un'auto usata:<br>i 3 controlli", ("3", "battistrada · data DOT · crepe"), S_SF,
  "Vai a vedere un'auto usata? Guarda le gomme 🛞\n\n📏 battistrada consumato in modo uniforme?\n📅 data DOT: le ultime 4 cifre (settimana e anno)\n🔍 crepe sui fianchi\n\nGomme da cambiare = spesa da mettere nel prezzo.", "#autousata #gomme #checklist"),
 ("quiz", "RECAP", "Il dato della settimana<br>che ti ha colpito?", ("della settimana", ["Auto di 13,2 anni", "212 usate ogni 100 nuove", "Diesel più caro"], -1), "Fonti: UNRAE · ACI · MIMIT",
  "Recap della settimana 📊\n\n🕰️ auto italiane: 13,2 anni di media\n🚗 212 usate vendute ogni 100 nuove\n⛽ gasolio più caro della benzina di 25 cent\n\nQual è il dato che ti ha colpito di più? 1, 2 o 3 👇", "#recap #auto #dati"),
]
IG_BASE = "#auto #motori #automobili #consigliauto #smilefixbroker"

# ---------- FACEBOOK (gazzetta) ----------
# (kind, testata, title, data, source, text)   None = slot già occupato
FB = [
 # LUN
 ("num", "Mercato", "Ottobre in crescita per le auto nuove", ("131.921", "immatricolazioni, +4,8%"), S_UN,
  "A ottobre in Italia sono state immatricolate 131.921 auto nuove, il 4,8% in più di un anno fa. Da gennaio il totale è di 1.400.991, +8,3%.\n\nUn buon segnale, ma l'UNRAE ricorda che il 2026 dovrebbe chiudersi ancora sotto i livelli del 2019 di circa il 14%.\n\nVoi state pensando di cambiare auto nei prossimi mesi? Nuova o usata?"),
 ("bars", "Alimentazioni", "Ibride al 49%, elettriche al 6,1%", [("Ibride", 49, "49%"), ("Plug-in", 12.7, "12,7%"), ("GPL", 9, "9%"), ("Elettriche", 6.1, "6,1%")], S_UN,
  "Come sono alimentate le auto nuove vendute a ottobre?\n\n• Ibride: 49%\n• Plug-in: 12,7%\n• GPL: 9%\n• Elettriche pure: 6,1%\n\nLe plug-in crescono, le elettriche restano al palo. Voi cosa scegliereste oggi: ibrida, plug-in, elettrica o tradizionale?"),
 ("num", "Classifica", "La Panda resta la più venduta", ("1ª", "anche a ottobre 2026"), S_UN,
  "Anche a ottobre la Fiat Panda è l'auto nuova più venduta in Italia. Sul podio sale anche la Jeep Avenger.\n\nLa Panda è un caso unico: prima nel nuovo, prima nell'usato… e purtroppo anche tra le più rubate.\n\nChi in famiglia ha avuto almeno una Panda? 🙋"),
 ("vs", "Il confronto", "Il mercato non è tornato al 2019", (("Stima 2026", "1,64 mln"), ("Sul 2019", "−14,4%")), S_UN,
  "L'UNRAE ha rivisto al rialzo le previsioni: nel 2026 dovrebbero essere vendute circa 1.640.000 auto nuove, +7,5% sul 2025.\n\nResta però un divario del 14,4% rispetto al 2019. Prezzi più alti, incertezza sui motori, tassi: secondo voi qual è il motivo principale?"),
 ("book", "Libri", "È uscito il Vol. 3 delle Guide da tasca", ("3", "Decidere e firmare"), "Guide da tasca SmileFix",
  "È disponibile su Amazon il terzo volume delle Guide da tasca SmileFix: «Decidere e firmare».\n\nÈ la parte finale dell'acquisto di un'auto usata: il semaforo per decidere, la trattativa, il pagamento sicuro e il passaggio di proprietà.\n\nCon il Vol. 1 (le verifiche da casa) e il Vol. 2 (i controlli sul posto) il metodo è completo.\n\n📚 " + AMZ3),
 # MAR (14:00 già occupato)
 ("num", "Usato", "212 usate ogni 100 nuove", ("212", "auto usate ogni 100 nuove, ottobre"), S_ACI,
  "Secondo il bollettino ACI, a ottobre sono state vendute 212 auto usate ogni 100 nuove. Da inizio anno il rapporto è di 190 a 100.\n\nIn Italia l'usato è il vero mercato dell'auto. Voi la prossima la comprerete usata o nuova?"),
 ("num", "Mercato usato", "Passaggi di proprietà in calo", ("−6,3%", "292.138 passaggi auto a ottobre"), S_ACI,
  "A ottobre i passaggi di proprietà di auto, al netto delle minivolture, sono stati 292.138: il 6,3% in meno di un anno fa. Le moto invece crescono (+1,1%).\n\nCon meno compratori in giro, chi vende può essere più disposto a trattare. Voi avete notato prezzi più trattabili?"),
 None,
 ("num", "Curiosità", "Un'auto venduta su cinque ha 20 anni", ("19,3%", "dei passaggi a ottobre"), S_ACI,
  "Quasi un'auto usata venduta su cinque ha almeno vent'anni: il 19,3% dei passaggi di ottobre.\n\nSono auto da budget basso, spesso prime auto per i ragazzi. Proprio per questo vanno controllate bene: ruggine, freni, gomme, sospensioni, libretto dei tagliandi.\n\nVoi comprereste un'auto di vent'anni a vostro figlio?"),
 ("num", "Tendenze", "Le ibride crescono anche nell'usato", ("+15,9%", "ibride a benzina in un anno"), S_ACI,
  "Le ibride a benzina sono il 12,7% dei passaggi di proprietà di ottobre, con un aumento del 15,9% in un anno.\n\nSe ne state valutando una usata, chiedete sempre: tagliandi regolari, stato della batteria ibrida e garanzia residua del costruttore sulla parte ibrida.\n\nAvete un'ibrida? Come vi trovate?"),
 # MER
 ("num", "Parco auto", "Le auto italiane hanno 13,2 anni", ("13,2", "anni di età media"), S_PARCO,
  "Secondo uno studio UNRAE su dati ACI, l'età media delle auto in Italia è salita da 8,5 anni nel 2011 a 13,2 anni nel 2025. Nello stesso periodo le auto sono passate da 37,1 a 41,8 milioni.\n\nPiù auto e più vecchie. La vostra quanti anni ha?"),
 ("num", "Il dato", "10,7 milioni di auto con oltre 20 anni", ("25,6%", "del parco circolante"), S_PARCO,
  "Le auto con più di vent'anni sono circa 10,7 milioni: il 25,6% di tutte quelle in circolazione.\n\nVuol dire meno sistemi di sicurezza, più emissioni e ricambi sempre più difficili da trovare.\n\nSecondo voi cosa servirebbe per svecchiare il parco auto?"),
 ("bars", "Le regioni", "Al Sud auto più vecchie", [("Sicilia, Calabria, Campania", 19, "oltre 19 anni"), ("Media Italia", 13.2, "13,2 anni")], S_PARCO,
  "Le differenze tra regioni sono forti: in Sicilia, Calabria e Campania l'età media delle auto supera i 19 anni, contro i 13,2 della media italiana.\n\nE se si escludono le auto a noleggio, la media nazionale sale a 15,6 anni.\n\nDa quale regione ci leggete?"),
 ("num", "Discussione", "Tenere l'auto vecchia o cambiarla?", ("15,6", "anni di media senza il noleggio"), S_PARCO,
  "Tenere un'auto vecchia finché va o cambiarla prima che inizino le spese grosse?\n\nNon c'è una risposta valida per tutti: dipende da quanti km fate, dallo stato dell'auto e da quanto vi costa ogni anno tra bollo, assicurazione, riparazioni e carburante.\n\nVoi cosa fate? Raccontateci la vostra scelta."),
 ("num", "Consigli", "Comprare un'auto di 15 anni: cosa guardare", ("3", "ruggine · tagliandi · km"), S_SF,
  "State guardando un'auto con più di 15 anni? Tre controlli da non saltare:\n\n1️⃣ Ruggine sotto la scocca, nei passaruota e sotto i tappetini\n2️⃣ Libretto dei tagliandi e fatture\n3️⃣ Chilometri: verificateli con le revisioni sul Portale dell'Automobilista\n\nSalvate il post per quando vi servirà."),
 # GIO
 ("num", "Carburanti", "Benzina sotto i 2 euro", ("1,945 €", "self, media del 20 novembre"), S_MIMIT,
  "Secondo l'Osservatorio prezzi del MIMIT, il 20 novembre la benzina self costava in media 1,945 € al litro sulla rete stradale, il gasolio 2,199 €.\n\nIl 2 novembre eravamo a 2,010 e 2,240: un calo lento ma costante.\n\nVoi avete notato la differenza al distributore?"),
 ("vs", "Il confronto", "Il gasolio costa più della benzina", (("Benzina", "1,945 €"), ("Gasolio", "2,199 €")), S_MIMIT,
  "Oggi il gasolio costa circa 25 centesimi al litro più della benzina (self, media nazionale del 20 novembre).\n\nPer chi fa tanti km il diesel resta interessante per i consumi più bassi. Per chi ne fa pochi, il conto cambia.\n\nVoi quanti km fate all'anno e cosa guidate?"),
 ("num", "In autostrada", "Fare il pieno prima di entrare", ("1,976 €", "benzina self in autostrada, 20/11"), S_MIMIT,
  "In autostrada la benzina self costa in media 1,976 € al litro contro 1,945 € della rete stradale (dati MIMIT del 20 novembre).\n\nSu un pieno da 50 litri sono un paio di euro. Poco? Moltiplicato per i viaggi di un anno, no.\n\nVoi fate il pieno prima di partire?"),
 ("num", "Andamento", "Gasolio in calo, ma sopra i 2 euro", ("−4,1 cent", "dal 2 al 20 novembre"), S_MIMIT,
  "Il gasolio self è sceso da 2,240 € (2 novembre) a 2,199 € al litro (20 novembre): circa 4 centesimi in meno.\n\nResta comunque sopra i 2 euro. Pensate che scenderà ancora prima delle feste?"),
 ("num", "Consiglio", "Il costo vero di un'auto usata", ("4", "carburante · bollo · RC · tagliandi"), S_SF,
  "Quando confrontate due auto usate, non guardate solo il prezzo. Fate il conto di quanto vi costeranno in un anno:\n\n⛽ carburante (km all'anno × consumo)\n🧾 bollo\n🛡️ assicurazione\n🔧 tagliandi e gomme\n\nA volte l'auto che costa di più all'acquisto costa meno da tenere."),
 # VEN
 ("num", "Inverno", "Gomme invernali o catene a bordo", ("15/11-15/4", "sulle strade con ordinanza"), S_GOM,
  "Dal 15 novembre al 15 aprile, sulle strade dove c'è un'ordinanza, serve circolare con pneumatici invernali (o quattro stagioni M+S) oppure avere le catene o le calze da neve a bordo.\n\nL'obbligo vale anche se non nevica. Voi avete già fatto il cambio gomme?"),
 ("num", "Promemoria", "Fino a quando si possono tenere", ("15 maggio", "per le invernali con indice più basso"), S_GOM,
  "C'è un mese di tolleranza: le gomme invernali si possono montare dal 15 ottobre e, se hanno un indice di velocità più basso di quello del libretto, vanno tolte entro il 15 maggio.\n\nDopo, si rischia una sanzione da 155 a 624 euro.\n\nSalvate il post come promemoria per la primavera."),
 ("bars", "Da sapere", "Cosa vuol dire la lettera sulla gomma", [("Q", 160, "160 km/h"), ("S", 180, "180 km/h"), ("T", 190, "190 km/h"), ("H", 210, "210 km/h")], "Fonte: codici di velocità degli pneumatici",
  "Sul fianco di ogni gomma c'è una lettera: è l'indice di velocità, cioè la velocità massima per cui è omologata.\n\nQ = 160 km/h, S = 180, T = 190, H = 210. Sulle invernali è ammesso un indice inferiore a quello del libretto, ma non sotto Q.\n\nAndate a guardare le vostre e diteci che lettera hanno!"),
 ("num", "Auto usata", "Le gomme dicono molto", ("3", "battistrada · DOT · crepe"), S_SF,
  "Quando andate a vedere un'auto usata, guardate bene le gomme:\n\n📏 battistrada: consumato in modo uniforme? Se è consumato solo da un lato, la convergenza o le sospensioni vanno controllate\n📅 data DOT: le ultime quattro cifre dicono settimana e anno di produzione\n🔍 crepe sui fianchi: gomme vecchie anche se hanno battistrada\n\nGomme da cambiare sono una spesa da mettere nella trattativa."),
 ("quiz", "Riepilogo", "I numeri della settimana", ("quale vi ha colpito?", ["13,2 anni di media", "212 usate ogni 100 nuove", "Gasolio +25 cent"], -1), "Fonti: UNRAE · ACI · MIMIT",
  "Il riepilogo della settimana:\n\n1️⃣ Le auto italiane hanno in media 13,2 anni (UNRAE su dati ACI)\n2️⃣ A ottobre 212 auto usate vendute ogni 100 nuove (ACI)\n3️⃣ Il gasolio costa circa 25 centesimi più della benzina (MIMIT)\n\nQuale dato vi ha sorpreso di più? Rispondete 1, 2 o 3."),
]

# ---------- TELEGRAM (09:00) - mar 24 già occupato (18:00 guida asta) ----------
TG = [
 ("2026-11-23", "📈 Auto nuove: ottobre 2026", ["131.921 immatricolazioni (+4,8%)", "Gen-ott: 1.400.991 (+8,3%)", "Ibride 49%, plug-in 12,7%", "Elettriche pure 6,1%", "Stima 2026: 1,64 mln (−14,4% sul 2019)"], S_UN),
 ("2026-11-25", "🕰️ Il parco auto invecchia", ["Età media: 13,2 anni (8,5 nel 2011)", "Auto in circolazione: 41,8 milioni", "Oltre 20 anni: 10,7 milioni (25,6%)", "Sicilia, Calabria, Campania: oltre 19 anni", "Senza noleggio: 15,6 anni"], S_PARCO),
 ("2026-11-26", "⛽ Carburanti, prezzi self", ["Benzina: 1,945 €/l (20/11)", "Gasolio: 2,199 €/l (20/11)", "Il 2/11: 2,010 e 2,240", "Autostrada benzina: 1,976 €/l", "Gasolio +25 cent sulla benzina"], S_MIMIT),
 ("2026-11-27", "❄️ Gomme invernali", ["Obbligo 15/11 - 15/4 dove c'è ordinanza", "In alternativa catene o calze a bordo", "Ok anche 4 stagioni M+S", "Indice minimo per invernali: Q (160 km/h)", "Tolleranza: via entro il 15/5"], S_GOM),
 ("2026-11-28", "🚗 Usato a ottobre", ["292.138 passaggi auto (−6,3%)", "212 usate ogni 100 nuove", "19,3% con almeno 20 anni", "Ibride a benzina: 12,7% (+15,9%)", "Moto: 52.929 passaggi (+1,1%)"], S_ACI),
 ("2026-11-29", "📚 Guide da tasca SmileFix", ["Vol. 1: le verifiche da casa", "Vol. 2: 50 controlli sul posto", "Vol. 3: decidere e firmare (nuovo)", "Su Amazon, Kindle e cartaceo"], "smilefixbroker.com/link"),
]

# ---------- BLUESKY (18:00) - mer 25 già occupato ----------
BS = [
 ("2026-11-23", "UNRAE, ottobre 2026: 131.921 auto nuove (+4,8%), gen-ott +8,3%. Le BEV scendono al 6,1% dal 7,6% di settembre, le plug-in salgono al 12,7%. La crescita c'è, la transizione no. #auto"),
 ("2026-11-24", "ACI, ottobre 2026: 212 auto usate vendute ogni 100 nuove, ma i passaggi calano del 6,3%. Il 19,3% delle auto passate di mano ha almeno 20 anni: l'usato si sposta verso il basso del mercato."),
 ("2026-11-26", "MIMIT, 20/11: benzina self 1,945 €/l, gasolio 2,199 €/l. Il differenziale a favore della benzina (~25 cent) cambia il calcolo di convenienza del diesel per chi percorre pochi km. #carburanti"),
 ("2026-11-27", "Gomme invernali: l'obbligo 15/11-15/4 non è nazionale e automatico, scatta sulle strade con ordinanza dell'ente gestore. Alternativa ammessa: catene o calze omologate a bordo."),
]

# ---------- PINTEREST (09:00) - mer 25 già occupato ----------
PIN = [
 ("2026-11-23", "Auto nuova o usata? 5 domande prima di scegliere", "list", ["Quanti km fai all'anno?", "Quanto puoi spendere in tutto?", "Ti serve garanzia lunga?", "Che alimentazione ti conviene?", "Per quanti anni la terrai?"], S_UN,
  "Auto nuova o usata: 5 domande per scegliere. A ottobre 2026 in Italia 131.921 auto nuove immatricolate (+4,8%) e 212 usate vendute ogni 100 nuove. #autonuova #autousata #consigliauto"),
 ("2026-11-24", "Auto usata ibrida: cosa controllare prima di comprarla", "list", ["Tagliandi regolari in rete", "Stato della batteria ibrida", "Garanzia residua sulla parte ibrida", "Spie e diagnosi elettronica", "Prova su strada in modalità elettrica"], S_ACI,
  "Checklist per comprare un'ibrida usata: tagliandi, batteria, garanzia, diagnosi. Le ibride a benzina sono il 12,7% dei passaggi di proprietà di ottobre 2026 (+15,9%). #ibrida #autousata #checklist"),
 ("2026-11-26", "Il costo vero di un'auto: 5 voci da calcolare", "list", ["Carburante: km × consumo", "Bollo auto", "Assicurazione RC", "Tagliandi e gomme", "Svalutazione negli anni"], S_MIMIT,
  "Come calcolare il costo annuo di un'auto oltre al prezzo: carburante, bollo, RC, tagliandi, svalutazione. Benzina self 1,945 €/l e gasolio 2,199 €/l (MIMIT, 20/11/2026). #costiauto #risparmio #autousata"),
 ("2026-11-27", "Gomme invernali: le regole da sapere", "list", ["Obbligo 15/11 - 15/4 dove c'è ordinanza", "Oppure catene o calze a bordo", "Valgono le 4 stagioni M+S", "Indice minimo Q (160 km/h)", "Invernali via entro il 15 maggio"], S_GOM,
  "Regole gomme invernali: periodo 15 novembre - 15 aprile, catene a bordo, 4 stagioni M+S, indice di velocità, tolleranza fino al 15 maggio. #gommeinvernali #pneumatici #inverno"),
]

# ---------- X (Buffer, 12:00) - mer 25 già occupato ----------
XP = [
 ("2026-11-23T12:00:00+01:00", "Auto nuove, ottobre 2026:\n📈 131.921 (+4,8%)\n⚡ ibride 49%\n🔌 plug-in 12,7%\n🔋 BEV 6,1%\n📊 stima 2026: 1,64 mln, −14,4% sul 2019\n\nFonte: UNRAE su dati MIT"),
 ("2026-11-27T12:00:00+01:00", "Carburanti self, 20/11:\n⛽ benzina 1,945 €/l\n🛢️ gasolio 2,199 €/l\n🛣️ benzina in autostrada 1,976 €/l\n\nIl gasolio costa ~25 cent in più della benzina.\n\nFonte: Osservatorio prezzi MIMIT"),
]
# ---------- MASTODON (Buffer, 10:00) - mer 25 già occupato ----------
MA = [
 ("2026-11-24T10:00:00+01:00", "ACI Auto-Trend, ottobre 2026: 292.138 passaggi di proprietà di auto (−6,3%), 212 usate ogni 100 nuove. Il 19,3% delle auto vendute ha almeno 20 anni; ibride a benzina al 12,7% (+15,9%). #auto #usato #Italia"),
 ("2026-11-26T10:00:00+01:00", "UNRAE su dati ACI: età media delle auto in Italia 13,2 anni nel 2025 (8,5 nel 2011), 15,6 escludendo il noleggio. 10,7 milioni di vetture hanno più di 20 anni, il 25,6% del parco. #auto #mobilità"),
]
# ---------- LINKEDIN (08:45) - mer 25 già occupato ----------
LI = [
 ("2026-11-24T08:45:00+01:00",
  "Il mercato auto italiano cresce, ma in modo selettivo.\n\nA ottobre 2026 le immatricolazioni sono state 131.921 (+4,8%) e da inizio anno 1.400.991 (+8,3%). UNRAE stima 1,64 milioni a fine anno: +7,5% sul 2025, ma ancora −14,4% rispetto al 2019.\n\nNello stesso mese, secondo ACI, sono state vendute 212 auto usate ogni 100 nuove, con passaggi di proprietà in calo del 6,3% e quasi un'auto usata su cinque con almeno 20 anni.\n\nLa lettura che ne do: il nuovo recupera soprattutto nella fascia di chi può spendere, mentre l'usato scivola verso auto più vecchie e budget più bassi. Per chi compra usato, aumenta il peso delle verifiche prima dell'acquisto.\n\n#automotive #mercatoauto #usato #mobilità"),
 ("2026-11-26T08:45:00+01:00",
  "Parco auto italiano: 13,2 anni di età media.\n\nLo studio UNRAE su dati ACI mostra che tra il 2011 e il 2025 le auto in circolazione sono passate da 37,1 a 41,8 milioni e l'età media da 8,5 a 13,2 anni (15,6 escludendo il noleggio). Circa 10,7 milioni di vetture superano i 20 anni, il 25,6% del totale, con punte oltre i 19 anni di media in Sicilia, Calabria e Campania.\n\nTre conseguenze pratiche:\n• sicurezza: molte auto non hanno i sistemi di assistenza oggi obbligatori sul nuovo\n• costi: ricambi e manutenzione pesano di più con l'età\n• mercato: l'usato giovane e controllato diventa una risorsa scarsa\n\nPer chi compra, la domanda giusta non è solo quanto costa l'auto, ma quanto costerà tenerla nei prossimi anni.\n\n#automotive #parcoauto #sicurezzastradale #mobilità"),
]

# ---------- STORIE (12:30) ----------
ST = [
 ("2026-11-23", "Sondaggio", "Prossima auto?", ["Nuova", "Usata", "Non so ancora"], "Ottobre: 131.921 auto nuove (+4,8%)"),
 ("2026-11-24", "Quiz", "Ogni 100 nuove, quante usate?", ["A · 120", "B · 212", "Risposta: B (ACI, ottobre)"], "Fonte: ACI Auto-Trend"),
 ("2026-11-25", "Domanda", "La tua auto quanti anni ha?", ["Meno di 5", "5-13", "Più di 13"], "Media Italia: 13,2 anni"),
 ("2026-11-26", "Sondaggio", "Dove fai il pieno?", ["Self", "Servito", "Dove costa meno"], "Benzina self 1,945 €/l (MIMIT 20/11)"),
 ("2026-11-27", "Quiz", "Invernali: obbligo fino al…", ["A · 31 marzo", "B · 15 aprile", "Risposta: B"], "Dove c'è ordinanza"),
]

# ---------- VIDEO ----------
# scene: hook(kick,title) list(title,items) vs(a,ai,b,bi) big(kick,num,text) bars(title,rows,src) cta(title,text) quiz(q,opts,correct) meme(top,bottom)
# + voce: testo letto da Luca (breve, ~12-18 s)
TT_TAGS = "#auto #motori #autotok #imparacontiktok #automobili"
TT = [
 # LUN 23
 ("t01", [("hook", "Ottobre 2026", "Auto nuove: <em>si torna a comprare?</em>"), ("big", "Immatricolazioni", "131.921", "+4,8% in un anno"), ("cta", "Tu cosa compri?", "Nuova o usata, scrivilo")],
  "A ottobre in Italia sono state vendute centotrentunomila auto nuove. Il quattro virgola otto per cento in più di un anno fa. Tu la prossima la prendi nuova o usata? Scrivilo nei commenti.",
  "Ottobre: 131.921 auto nuove vendute, +4,8% 📈 Fonte UNRAE"),
 ("t02", [("meme", "Io che volevo l'elettrica", "e poi ho visto i prezzi 🥲"), ("bars", "Ottobre 2026", [("Ibride", 49, "49%"), ("Plug-in", 12.7, "12,7%"), ("Elettriche", 6.1, "6,1%")], "UNRAE"), ("cta", "E tu?", "Cosa guidi oggi?")],
  "Quasi un'auto nuova su due è ibrida. Le plug-in salgono al dodici virgola sette per cento. Le elettriche pure? Ferme al sei per cento. E tu cosa guidi?",
  "Ibride al 49%, elettriche al 6,1% ⚡ Fonte UNRAE"),
 ("t03", [("quiz", "L'auto più venduta a ottobre?", ["Jeep Avenger", "Fiat Panda", "Dacia Sandero"], 1), ("big", "Sempre lei", "Panda", "prima anche a ottobre"), ("cta", "Indovinato?", "Scrivilo nei commenti")],
  "Quiz. Qual è stata l'auto nuova più venduta in Italia a ottobre? La risposta è sempre la stessa: la Fiat Panda. L'avevi indovinato?",
  "Quiz: l'auto più venduta a ottobre? 🤔 Fonte UNRAE"),
 ("t04", [("hook", "Nuovo su Amazon", "Vol. 3: <em>decidere e firmare</em>"), ("list", "Dentro trovi", ["Il semaforo per decidere", "La trattativa", "Pagamento e passaggio"]), ("cta", "Link in bio", "Guide da tasca SmileFix")],
  "È uscito il volume tre delle Guide da tasca SmileFix. Come decidere, come trattare, come pagare in sicurezza e fare il passaggio di proprietà. Trovi il link in bio.",
  "📘 È uscito il Vol. 3 delle Guide da tasca SmileFix. Link in bio"),
 # MAR 24
 ("t05", [("hook", "Usato", "Ogni 100 auto nuove…"), ("big", "Ottobre 2026", "212", "auto usate vendute"), ("cta", "L'usato comanda", "Fonte: ACI")],
  "Lo sapevi? A ottobre, per ogni cento auto nuove, in Italia ne sono state vendute duecentododici usate. L'usato è il vero mercato dell'auto.",
  "212 auto usate ogni 100 nuove 🚗 Fonte ACI"),
 ("t06", [("meme", "Mio cugino che compra", "un'auto di 20 anni a 500 € 🤡"), ("big", "Passaggi di ottobre", "19,3%", "auto con almeno 20 anni"), ("cta", "Controllala prima", "sempre")],
  "Quasi un'auto usata su cinque venduta a ottobre ha almeno vent'anni. Costano poco, ma vanno controllate il doppio: ruggine, freni, gomme e tagliandi.",
  "1 auto usata su 5 ha almeno 20 anni 👴 Fonte ACI"),
 ("t07", [("quiz", "Passaggi di proprietà a ottobre?", ["In crescita", "Stabili", "In calo"], 2), ("big", "Auto, ottobre 2026", "−6,3%", "292.138 passaggi"), ("cta", "Momento per trattare?", "Dimmi la tua")],
  "Quiz. I passaggi di proprietà delle auto a ottobre sono saliti o scesi? Sono scesi del sei virgola tre per cento. Momento buono per trattare?",
  "Passaggi di proprietà in calo del 6,3% 📉 Fonte ACI"),
 ("t08", [("hook", "Ibrida usata?", "Chiedi <em>queste 3 cose</em>"), ("list", "Prima di comprare", ["Tagliandi regolari", "Stato batteria ibrida", "Garanzia residua"]), ("cta", "Salva il video", "ti servirà")],
  "Vuoi comprare un'ibrida usata? Chiedi tre cose: i tagliandi regolari, lo stato della batteria ibrida e quanta garanzia resta sulla parte ibrida. Salva il video.",
  "Ibrida usata: le 3 domande da fare 🔋"),
 # MER 25
 ("t09", [("hook", "Auto italiane", "Quanti anni <em>hanno?</em>"), ("big", "Età media", "13,2", "anni, erano 8,5 nel 2011"), ("cta", "La tua?", "Scrivi l'anno nei commenti")],
  "Quanti anni ha in media un'auto in Italia? Tredici virgola due. Nel duemilaundici erano otto e mezzo. La tua di che anno è? Scrivilo nei commenti.",
  "Età media delle auto in Italia: 13,2 anni 🕰️ Fonte UNRAE su dati ACI"),
 ("t10", [("meme", "La mia auto del 2003", "che non molla mai 💪"), ("big", "Over 20 anni", "10,7 mln", "una su quattro"), ("cta", "Tagga chi", "ce l'ha ancora")],
  "In Italia ci sono dieci virgola sette milioni di auto con più di vent'anni. Una su quattro. Tagga chi ha ancora l'auto dei primi anni duemila.",
  "10,7 milioni di auto con più di 20 anni 😳 Fonte UNRAE"),
 ("t11", [("quiz", "Dove le auto sono più vecchie?", ["Lombardia", "Sicilia", "Veneto"], 1), ("big", "Sicilia, Calabria, Campania", "19+", "anni di età media"), ("cta", "La tua regione?", "Scrivila")],
  "Quiz. Dove sono le auto più vecchie d'Italia? In Sicilia, Calabria e Campania: oltre diciannove anni di media. La tua regione?",
  "Dove le auto sono più vecchie? 🗺️ Fonte UNRAE"),
 ("t12", [("hook", "Auto di 15 anni?", "I <em>3 controlli</em>"), ("list", "Non saltarli", ["Ruggine sotto", "Libretto tagliandi", "Km sulle revisioni"]), ("cta", "Salva", "e manda a chi cerca")],
  "Stai per comprare un'auto di quindici anni? Tre controlli: ruggine sotto la scocca, libretto dei tagliandi e chilometri verificati con le revisioni.",
  "Auto vecchia usata: i 3 controlli da fare ✅"),
 # VEN 27
 ("t13", [("hook", "Inverno", "Gomme invernali <em>o catene</em>"), ("big", "Obbligo", "15/11 → 15/4", "dove c'è ordinanza"), ("cta", "Già montate?", "Rispondi sì o no")],
  "Dal quindici novembre al quindici aprile, sulle strade con ordinanza, servono gomme invernali oppure catene a bordo. Anche se non nevica. Le hai già montate?",
  "Gomme invernali: l'obbligo è scattato ❄️"),
 ("t14", [("quiz", "Invernali con codice basso: fino a…", ["15 aprile", "15 maggio", "Sempre"], 1), ("big", "Dopo il 15 maggio", "155-624 €", "di multa"), ("cta", "Segna la data", "15 maggio")],
  "Quiz. Fino a quando puoi tenere le invernali con un codice di velocità più basso? Fino al quindici maggio. Dopo rischi una multa da centocinquantacinque a seicentoventiquattro euro.",
  "Gomme invernali: fino a quando tenerle? 📅"),
 ("t15", [("meme", "Io davanti alla lettera", "sul fianco della gomma 🤨"), ("bars", "Indice di velocità", [("Q", 160, "160"), ("T", 190, "190"), ("H", 210, "210")], "km/h"), ("cta", "Vai a guardare", "le tue gomme")],
  "Quella lettera sul fianco della gomma è l'indice di velocità. Q vuol dire centosessanta all'ora, T centonovanta, H duecentodieci. Vai a guardare le tue.",
  "Cosa vuol dire la lettera sulla gomma? 🔤"),
 ("t16", [("hook", "Auto usata", "Guarda <em>le gomme</em>"), ("list", "3 controlli", ["Battistrada uniforme", "Data DOT", "Crepe sui fianchi"]), ("cta", "Gomme da cambiare?", "Mettilo nella trattativa")],
  "Vai a vedere un'auto usata? Guarda le gomme: battistrada uniforme, data di produzione sul fianco e crepe. Se sono da cambiare, usalo nella trattativa.",
  "Auto usata: cosa dicono le gomme 🛞"),
 # SAB 28
 ("t17", [("hook", "Carburanti", "La benzina <em>scende</em>"), ("big", "Self, 20 novembre", "1,945 €", "al litro"), ("cta", "Tu dove fai il pieno?", "Fonte: MIMIT")],
  "La benzina self è scesa a uno virgola novecentoquarantacinque euro al litro di media. A inizio novembre era sopra i due euro. Tu dove fai il pieno?",
  "Benzina self a 1,945 € ⛽ Fonte MIMIT"),
 ("t18", [("meme", "Io col diesel", "che costa più della benzina 🫠"), ("vs", "Benzina", ["1,945 €/l"], "Gasolio", ["2,199 €/l", "+25 cent"]), ("cta", "Il diesel conviene?", "Dipende dai km")],
  "Plot twist: oggi il gasolio costa venticinque centesimi più della benzina. Il diesel conviene ancora? Dipende da quanti chilometri fai.",
  "Il gasolio costa più della benzina 🫠 Fonte MIMIT"),
 ("t19", [("hook", "Prima di comprare", "Il costo <em>vero</em> dell'auto"), ("list", "Calcola", ["Carburante", "Bollo", "RC auto", "Tagliandi e gomme"]), ("cta", "Salva il video", "e fai il conto")],
  "Il prezzo dell'auto è solo l'inizio. Prima di comprare calcola carburante, bollo, assicurazione, tagliandi e gomme. A volte l'auto più cara costa meno da tenere.",
  "Il costo vero di un'auto 💶"),
 ("t20", [("hook", "Recap", "3 dati <em>della settimana</em>"), ("list", "Dati", ["Auto: 13,2 anni di media", "212 usate ogni 100 nuove", "Gasolio +25 cent"]), ("cta", "Quale ti ha colpito?", "1, 2 o 3")],
  "Ricapitoliamo la settimana. Le auto italiane hanno tredici anni di media. Si vendono duecentododici usate ogni cento nuove. E il gasolio costa più della benzina. Quale ti ha colpito?",
  "Recap: 3 dati auto della settimana 📊"),
]

YT_TAGS = "#auto #autousate #motori"
YT = [
 # LUN 23
 ("y01", [("hook", "Mercato auto", "Ottobre 2026 <em>in numeri</em>"), ("big", "Immatricolazioni", "131.921", "+4,8% su ottobre 2025"), ("list", "In sintesi", ["Gen-ott: 1,4 milioni (+8,3%)", "Stima 2026: 1,64 milioni", "Ancora −14,4% sul 2019"])],
  "Mercato auto di ottobre: centotrentunomila novecentoventuno immatricolazioni, più quattro virgola otto per cento. Da inizio anno siamo a un milione e quattrocentomila. Ma rispetto al duemiladiciannove manca ancora il quattordici per cento.",
  "Mercato auto ottobre 2026: +4,8% #shorts", "Dati UNRAE su fonte MIT: a ottobre 2026 131.921 auto nuove immatricolate (+4,8%), 1.400.991 da inizio anno (+8,3%)."),
 ("y02", [("hook", "Alimentazioni", "Cosa comprano <em>gli italiani</em>"), ("bars", "Ottobre 2026", [("Ibride", 49, "49%"), ("Plug-in", 12.7, "12,7%"), ("GPL", 9, "9%"), ("Elettriche", 6.1, "6,1%")], "UNRAE"), ("cta", "Elettriche", "ferme al 6,1%")],
  "Come sono alimentate le auto nuove? Ibride al quarantanove per cento, plug-in al dodici virgola sette, GPL al nove. Le elettriche pure restano al sei virgola uno.",
  "Ibride, plug-in o elettriche? Le quote di ottobre #shorts", "Quote di mercato per alimentazione a ottobre 2026 secondo UNRAE: ibride 49%, plug-in 12,7%, GPL 9%, elettriche 6,1%."),
 ("y03", [("hook", "Nuova o usata?", "<em>5 domande</em> per scegliere"), ("list", "Chiediti", ["Quanti km all'anno?", "Budget totale?", "Ti serve garanzia lunga?", "Che alimentazione?", "Per quanti anni?"]), ("cta", "Poi decidi", "con i numeri")],
  "Nuova o usata? Prima chiediti cinque cose: quanti chilometri fai all'anno, quanto puoi spendere in tutto, se ti serve una garanzia lunga, che alimentazione ti conviene e per quanti anni la terrai.",
  "Auto nuova o usata? 5 domande per scegliere #shorts", "Le cinque domande da farsi prima di scegliere tra auto nuova e usata."),
 ("y04", [("hook", "Guide da tasca SmileFix", "Esce il <em>Vol. 3</em>"), ("list", "Decidere e firmare", ["Il semaforo per decidere", "La trattativa", "Pagamento sicuro", "Passaggio di proprietà"]), ("cta", "Su Amazon", "Kindle e cartaceo")],
  "È uscito il terzo volume delle Guide da tasca SmileFix: decidere e firmare. Il semaforo per decidere, la trattativa, il pagamento sicuro e il passaggio di proprietà. Lo trovi su Amazon.",
  "Comprare un'auto usata: decidere e firmare (Vol. 3) #shorts", "Il Vol. 3 delle Guide da tasca SmileFix, «Decidere e firmare», è disponibile su Amazon.\n\n📚 " + AMZ3),
 # MAR 24
 ("y05", [("hook", "Usato", "Ottobre <em>in numeri</em>"), ("list", "Dati ACI", ["292.138 passaggi auto (−6,3%)", "212 usate ogni 100 nuove", "Moto: +1,1%"]), ("cta", "Fonte", "ACI Auto-Trend")],
  "Mercato dell'usato a ottobre: duecentonovantaduemila passaggi di proprietà di auto, meno sei virgola tre per cento. Ma ogni cento auto nuove se ne vendono duecentododici usate.",
  "Auto usate: i dati di ottobre 2026 #shorts", "Bollettino ACI Auto-Trend di ottobre 2026: 292.138 passaggi di proprietà di auto (−6,3%), 212 usate ogni 100 nuove."),
 ("y06", [("hook", "Auto di 20 anni", "Si vendono <em>ancora</em>"), ("big", "Ottobre 2026", "19,3%", "dei passaggi"), ("list", "Se la compri", ["Ruggine e sottoscocca", "Freni e sospensioni", "Tagliandi e km"])],
  "Quasi un'auto usata su cinque venduta a ottobre ha almeno vent'anni. Se ne compri una, controlla ruggine e sottoscocca, freni e sospensioni, tagliandi e chilometri.",
  "Comprare un'auto di 20 anni: cosa controllare #shorts", "Il 19,3% delle auto usate vendute a ottobre 2026 ha almeno 20 anni (ACI)."),
 ("y07", [("hook", "Ibrida usata", "Cosa <em>controllare</em>"), ("list", "Checklist", ["Tagliandi in rete", "Stato batteria ibrida", "Garanzia residua", "Diagnosi elettronica", "Prova in elettrico"]), ("cta", "Ibride a benzina", "+15,9% nell'usato")],
  "Le ibride crescono anche nell'usato. Se ne compri una controlla i tagliandi, lo stato della batteria ibrida, la garanzia residua, fai una diagnosi elettronica e provala in modalità elettrica.",
  "Auto ibrida usata: la checklist #shorts", "Le ibride a benzina sono il 12,7% dei passaggi di ottobre 2026, +15,9% (ACI)."),
 ("y08", [("hook", "Mercato in calo", "È il momento di <em>trattare?</em>"), ("big", "Passaggi auto", "−6,3%", "ottobre su ottobre"), ("list", "Come trattare", ["Confronta 3 annunci simili", "Usa i difetti trovati", "Fai un'offerta motivata"])],
  "Con i passaggi di proprietà in calo, chi vende può essere più disponibile. Confronta tre annunci simili, usa i difetti che trovi e fai un'offerta motivata.",
  "Auto usata: come trattare sul prezzo #shorts", "Consigli per trattare il prezzo di un'auto usata con il mercato in calo (ACI, ottobre 2026: −6,3%)."),
 # MER 25
 ("y09", [("hook", "Parco auto", "Quanto sono <em>vecchie</em>"), ("big", "Età media", "13,2", "anni nel 2025"), ("list", "Dal 2011 al 2025", ["Da 8,5 a 13,2 anni", "Da 37,1 a 41,8 milioni", "15,6 anni senza noleggio"])],
  "Le auto in Italia hanno in media tredici virgola due anni. Nel duemilaundici erano otto e mezzo. Nel frattempo sono passate da trentasette a quasi quarantadue milioni.",
  "Età media delle auto in Italia: 13,2 anni #shorts", "Studio UNRAE su dati ACI: età media del parco auto italiano 13,2 anni nel 2025 (8,5 nel 2011)."),
 ("y10", [("hook", "Over 20", "Una auto su <em>quattro</em>"), ("big", "Auto con più di 20 anni", "10,7 mln", "il 25,6% del parco"), ("cta", "Il problema", "sicurezza ed emissioni")],
  "Dieci virgola sette milioni di auto in Italia hanno più di vent'anni: una su quattro. Meno sicurezza, più emissioni e ricambi sempre più difficili.",
  "10,7 milioni di auto con più di 20 anni #shorts", "Secondo UNRAE su dati ACI circa 10,7 milioni di auto superano i 20 anni (25,6% del parco)."),
 ("y11", [("hook", "Nord e Sud", "Due Italie <em>dell'auto</em>"), ("vs", "Media Italia", ["13,2 anni"], "Sicilia, Calabria, Campania", ["oltre 19 anni"]), ("cta", "Fonte", "UNRAE su dati ACI")],
  "La media italiana è tredici anni, ma in Sicilia, Calabria e Campania le auto superano i diciannove anni di media. Due Italie dell'auto.",
  "Dove sono le auto più vecchie d'Italia #shorts", "Età media delle auto per regione: in Sicilia, Calabria e Campania oltre 19 anni (UNRAE su dati ACI)."),
 ("y12", [("hook", "Auto vecchia o nuova?", "Come <em>decidere</em>"), ("list", "Fai il conto annuo", ["Riparazioni previste", "Consumi", "Bollo e RC", "Sicurezza"]), ("cta", "Poi confronta", "con un'auto più giovane")],
  "Tenere l'auto vecchia o cambiarla? Fai il conto di un anno: riparazioni previste, consumi, bollo e assicurazione. E metti nel conto anche la sicurezza. Poi confronta con un'auto più giovane.",
  "Tenere l'auto vecchia o cambiarla? #shorts", "Come decidere se tenere un'auto vecchia o cambiarla: il conto annuo da fare."),
 # GIO 26 (carosello TikTok già programmato: su YT 4 video)
 ("y13", [("hook", "Carburanti", "I prezzi <em>di novembre</em>"), ("vs", "2 novembre", ["Benzina 2,010", "Gasolio 2,240"], "20 novembre", ["Benzina 1,945", "Gasolio 2,199"]), ("cta", "Fonte", "Osservatorio MIMIT")],
  "I carburanti scendono. Il due novembre la benzina self era a due euro e un centesimo, il venti novembre a uno virgola novecentoquarantacinque. Il gasolio da due e ventiquattro a due e diciannove.",
  "Benzina e gasolio: i prezzi di novembre #shorts", "Prezzi medi self MIMIT: benzina da 2,010 €/l (2/11) a 1,945 €/l (20/11), gasolio da 2,240 a 2,199 €/l."),
 ("y14", [("hook", "Diesel o benzina?", "Il conto <em>è cambiato</em>"), ("big", "Differenza al litro", "+25 cent", "il gasolio costa di più"), ("list", "Il diesel conviene se", ["Fai tanti km", "Viaggi in autostrada", "Tieni l'auto a lungo"])],
  "Oggi il gasolio costa circa venticinque centesimi più della benzina. Il diesel conviene ancora se fai tanti chilometri, viaggi spesso in autostrada e tieni l'auto a lungo.",
  "Diesel o benzina: conviene ancora il diesel? #shorts", "Con il gasolio a 2,199 €/l e la benzina a 1,945 €/l (MIMIT 20/11/2026) il diesel conviene solo con percorrenze elevate."),
 ("y15", [("hook", "Pieno in autostrada?", "Costa <em>di più</em>"), ("vs", "Rete stradale", ["Benzina 1,945 €"], "Autostrada", ["Benzina 1,976 €"]), ("cta", "Consiglio", "fai il pieno prima")],
  "In autostrada la benzina costa di più: uno virgola novecentosettantasei contro uno virgola novecentoquarantacinque. Consiglio semplice: fai il pieno prima di entrare.",
  "Benzina in autostrada: quanto costa in più #shorts", "Prezzo medio self della benzina il 20/11/2026: 1,976 €/l in autostrada contro 1,945 €/l sulla rete stradale (MIMIT)."),
 ("y16", [("hook", "Auto usata", "Il <em>costo vero</em>"), ("list", "Oltre al prezzo", ["Carburante", "Bollo", "Assicurazione", "Tagliandi e gomme", "Svalutazione"]), ("cta", "Fai il conto", "prima di firmare")],
  "Il costo vero di un'auto non è solo il prezzo. Calcola carburante, bollo, assicurazione, tagliandi e gomme, e quanto perderà di valore. Fai il conto prima di firmare.",
  "Quanto costa davvero un'auto usata #shorts", "Le voci di costo da calcolare prima di comprare un'auto usata."),
 # VEN 27 (14:00 già occupato dallo short guida asta)
 ("y17", [("hook", "Gomme invernali", "Le regole <em>2026-27</em>"), ("list", "In sintesi", ["15/11 - 15/4 con ordinanza", "Oppure catene a bordo", "Ok 4 stagioni M+S"]), ("cta", "Vale anche", "senza neve")],
  "Gomme invernali: dal quindici novembre al quindici aprile, sulle strade con ordinanza, servono invernali o quattro stagioni, oppure catene a bordo. Vale anche se non nevica.",
  "Gomme invernali 2026-2027: le regole #shorts", "Periodo di riferimento 15 novembre 2026 - 15 aprile 2027 sulle strade con ordinanza (MIT)."),
 ("y18", [("hook", "Codice di velocità", "Cosa vuol dire <em>la lettera</em>"), ("bars", "Indici", [("Q", 160, "160 km/h"), ("S", 180, "180 km/h"), ("T", 190, "190 km/h"), ("H", 210, "210 km/h")], "pneumatici"), ("cta", "Sulle invernali", "minimo Q")],
  "La lettera sul fianco della gomma è l'indice di velocità. Q centosessanta, S centottanta, T centonovanta, H duecentodieci. Sulle invernali il minimo è Q.",
  "Indice di velocità delle gomme: cosa significa #shorts", "Gli indici di velocità degli pneumatici: Q 160, S 180, T 190, H 210 km/h."),
 ("y19", [("hook", "Auto usata", "Leggi <em>le gomme</em>"), ("list", "Controlla", ["Battistrada uniforme", "Data DOT", "Crepe sui fianchi", "Stessa marca sull'asse"]), ("cta", "Da cambiare?", "Usalo nella trattativa")],
  "Quando vai a vedere un'auto usata, leggi le gomme: battistrada uniforme, data di produzione, crepe sui fianchi e stessa marca sullo stesso asse. Se sono da cambiare, usalo nella trattativa.",
  "Auto usata: cosa ti dicono le gomme #shorts", "Come controllare le gomme di un'auto usata prima di comprarla."),
 # SAB 28
 ("y20", [("hook", "In 30 secondi", "La settimana <em>in numeri</em>"), ("list", "Dati", ["Auto nuove ottobre +4,8%", "212 usate ogni 100 nuove", "Età media 13,2 anni", "Benzina 1,945 €/l"]), ("cta", "Fonti", "UNRAE, ACI, MIMIT")],
  "La settimana in trenta secondi. Auto nuove in crescita del quattro virgola otto per cento. Duecentododici usate ogni cento nuove. Età media tredici anni. Benzina sotto i due euro.",
  "Auto: i numeri della settimana in 30 secondi #shorts", "Riepilogo: mercato nuovo e usato, parco circolante e carburanti con le fonti."),
 ("y21", [("hook", "Recap", "Il <em>prezzo</em> non è tutto"), ("list", "Prima di comprare", ["Verifica i km", "Controlla le gomme", "Calcola il costo annuo"]), ("cta", "Guide gratuite", "smilefixbroker.com/guide")],
  "Prima di comprare un'auto usata: verifica i chilometri, controlla le gomme e calcola quanto ti costerà ogni anno. Trovi le guide gratuite sul sito SmileFix.",
  "Auto usata: 3 cose prima di comprare #shorts", "Tre controlli prima di comprare un'auto usata. Guide gratuite: https://smilefixbroker.com/guide/"),
 ("y22", [("hook", "Gomme invernali", "Fino a <em>quando</em>"), ("big", "Tolleranza", "15 maggio", "per le invernali con indice basso"), ("cta", "Dopo", "multa da 155 a 624 €")],
  "Le invernali con indice di velocità più basso di quello del libretto vanno tolte entro il quindici maggio. Dopo si rischia una multa da centocinquantacinque a seicentoventiquattro euro.",
  "Gomme invernali: entro quando toglierle #shorts", "Tolleranza fino al 15 maggio per le gomme invernali con indice di velocità inferiore a quello del libretto."),
 ("y23", [("hook", "Mercato usato", "Si compra <em>più vecchio</em>"), ("big", "Ottobre 2026", "19,3%", "auto con almeno 20 anni"), ("cta", "Più vecchia l'auto", "più importanti i controlli")],
  "Nel mercato dell'usato si compra sempre più vecchio: a ottobre quasi un'auto su cinque passata di mano aveva almeno vent'anni. Più vecchia è l'auto, più importanti sono i controlli.",
  "Usato: si comprano auto sempre più vecchie #shorts", "ACI: a ottobre 2026 il 19,3% delle auto usate vendute ha almeno 20 anni."),
]

# date/orari video (Europe/Rome)
TT_PLAN = {"2026-11-23": ["t01", "t02", "t03", "t04"], "2026-11-24": ["t05", "t06", "t07", "t08"], "2026-11-25": ["t09", "t10", "t11", "t12"],
           "2026-11-27": ["t13", "t14", "t15", "t16"], "2026-11-28": ["t17", "t18", "t19", "t20"]}
TT_TIMES = {"wk": ["07:30", "13:00", "19:00", "21:30"], "sat": ["10:00", "13:00", "18:00", "21:30"]}
YT_PLAN = {"2026-11-23": ["y01", "y02", "y03", "y04"], "2026-11-24": ["y05", "y06", "y07", "y08"], "2026-11-25": ["y09", "y10", "y11", "y12"],
           "2026-11-26": ["y13", "y14", "y15", "y16"], "2026-11-27": ["y17", "y18", "y19"], "2026-11-28": ["y20", "y21", "y22", "y23"]}
YT_TIMES = {"wk": ["12:00", "15:00", "18:00", "20:30"], "fri": ["12:00", "17:00", "20:30"], "sat": ["11:00", "15:00", "18:00", "21:00"]}
IG_TIMES = ["06:00", "10:00", "14:00", "18:00", "22:00"]
