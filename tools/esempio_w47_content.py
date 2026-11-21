# -*- coding: utf-8 -*-
"""Settimana 16-22 novembre 2026. Dati verificati il 14/11/2026.
 IVASS, indagine IPER 2° trimestre 2026 (FleetMagazine, Motorbox, Soldionline, Teleborsa 24/9/2026)
 LoJack Italia, Dossier furti veicoli 2025 su dati Min. Interno 2024 (Motor1, Auto.it, Quotidiano.net)
 LoJack, recuperi 1° semestre 2026 (Motorionline, Affaritaliani); furti parziali (Sky TG24 21/10/2025)
 Eurostat via Businessonline: Italia 231 furti ogni 100.000 abitanti
 ACI-Istat, incidenti stradali 2024 (comunicato 24/7/2025, L'Automobile ACI)
 Osservatorio AutoScout24, usato 2025 (Teleborsa 5/2/2026)
Linea: dati veri con fonte, consigli pratici, domande e sondaggi, tono diverso per social. Niente prezzi di riparazione.
"""
S_IV = "Fonte: IVASS, indagine IPER, 2° trim. 2026"
S_LJ = "Fonte: LoJack Italia, Dossier furti 2025 (dati Min. Interno 2024)"
S_LJ26 = "Fonte: LoJack Italia, recuperi 1° semestre 2026"
S_IS = "Fonte: ACI-Istat, incidenti stradali 2024"
S_AS = "Fonte: Osservatorio AutoScout24, usato 2025"
S_EU = "Fonte: Eurostat (denunce), via Businessonline"

AMZ2 = "https://www.amazon.it/dp/B0HQYCPW11"
AMZ1 = "https://www.amazon.it/dp/B0HQYC883Z"
V2 = "«Il giro dell'auto»"

# ---------------- INSTAGRAM: 25 card stile "pop sticker" (ironiche, salvabili) ----------------
# (kind, sticker, title, data, source, caption, tags)
# kind: num (n, testo) | bars [(lab,val,str)] | vs ((lab,val),(lab,val)) | quiz (domanda, [opzioni], indice_giusta) | book (vol, riga)
IG = [
 # LUN 16 - Assicurazione
 ("book", "GRATIS 5 GIORNI", "Il Vol. 2 è gratis<br>su Kindle", ("2", "fino a venerdì 20 novembre"), "Guide da tasca SmileFix · Amazon Kindle",
  "📚 Da oggi a venerdì 20 novembre il Vol. 2 delle Guide da tasca SmileFix è GRATIS su Kindle.\n\n«Il giro dell'auto»: 50 controlli in 5 zone e la prova su strada. È la guida da tenere sul telefono quando vai a vedere un'auto usata.\n\n🔎 Cerca «Il giro dell'auto SmileFix» su Amazon o usa il link in bio.\n\nTagga chi sta cercando un'auto 👇", "#ebookgratis #kindle #autousata"),
 ("num", "RC AUTO 2026", "Quanto paghi in media<br>di assicurazione?", ("422 €", "premio medio, aprile-giugno 2026"), S_IV,
  "422 euro: è quanto paga in media un italiano per l'RC auto (IVASS, 2° trimestre 2026) 💸\n\n+1,6% in un anno, ma −0,4% rispetto al trimestre prima. Primo piccolo calo dopo mesi di aumenti.\n\nTu stai sopra o sotto la media? Scrivilo nei commenti 👇", "#rcauto #assicurazioneauto #ivass"),
 ("vs", "NAPOLI VS AOSTA", "Stessa polizza,<br>città diversa", (("Aosta", "la più bassa"), ("Napoli", "+255 €")), S_IV,
  "Napoli contro Aosta: la stessa RC auto costa in media 255 euro in più 😳\n\nLa provincia pesa sul prezzo quanto la tua storia assicurativa. Per questo un preventivo vale solo per chi lo chiede.\n\n📌 Salva e confronta sempre più offerte.", "#rcauto #napoli #aosta"),
 ("quiz", "QUIZ", "Nel 2014 l'RC auto<br>costava…", ("di più o di meno?", ["Di meno", "Uguale", "Di più"], 2), S_IV,
  "Quiz lampo ⏱️ Nel 2014 l'RC auto costava più o meno di oggi?\n\nRisposta: DI PIÙ. Allora si superavano i 488 euro, oggi siamo a 422 (−13,6% rispetto al 2° trimestre 2014).\n\nL'avresti indovinato?", "#quiz #rcauto #curiosita"),
 ("num", "SCATOLA NERA", "Quante polizze hanno<br>la scatola nera?", ("16%", "era il 17,2% un anno fa"), S_IV,
  "Solo il 16% delle polizze RC auto ha la scatola nera, ed è in calo (era il 17,2%) 📦\n\nPuò dare uno sconto, ma registra come guidi. Tu la metteresti? Sì o no nei commenti.", "#scatolanera #rcauto #sondaggio"),
 # MAR 17 - Furti
 ("num", "RED FLAG 🚩", "Veicoli rubati in Italia<br>in un anno", ("136.201", "+3% sull'anno prima"), S_LJ,
  "136.201 veicoli rubati in un anno: più di 370 al giorno 🚨\n\nE più di metà sono automobili. Domani ti diciamo qual è la preferita dai ladri (spoiler: ce l'hanno in tanti).\n\nSegui per non perderti il resto 🔔", "#furtiauto #sicurezza #auto"),
 ("num", "LA PIÙ AMATA… DAI LADRI", "L'auto più rubata<br>d'Italia è lei", ("Panda", "13.311 furti: quasi 1 su 5"), S_LJ,
  "La Panda è la regina delle vendite… e anche dei furti 😬 13.311 rubate nel 2024, quasi un'auto rubata su cinque.\n\nSe hai una Panda, tagga un amico che ce l'ha pure lui 👇", "#fiatpanda #furtiauto #meme"),
 ("bars", "TOP 3 RUBATE", "Le auto preferite<br>dai ladri", [("Fiat Panda", 13311, "13.311"), ("Fiat 500", 5254, "5.254"), ("Lancia Ypsilon", 5048, "5.048")], S_LJ,
  "Podio dei furti 2024: Panda, 500, Ypsilon 🥇🥈🥉\n\nTutte italiane, tutte diffusissime: più un modello circola, più i suoi ricambi valgono sul mercato nero.\n\n📌 Salva per i consigli antifurto di domani.", "#furtiauto #fiat #lancia"),
 ("bars", "DOVE SI RUBA", "Il 78% dei furti avviene<br>in 5 regioni", [("Campania", 23, "23%"), ("Lazio", 18, "18%"), ("Sicilia", 14, "14%"), ("Puglia + Lombardia", 23, "23%")], S_LJ,
  "5 regioni concentrano il 78% dei furti: Campania, Lazio, Sicilia, Puglia e Lombardia 🗺️\n\nLa tua è in classifica? Scrivi la tua regione nei commenti.", "#furtiauto #regioni #italia"),
 ("num", "BUONE NOTIZIE", "Auto ritrovate entro<br>24 ore dalla denuncia", ("83%", "dei recuperi LoJack, 1° sem. 2026"), S_LJ26,
  "Una buona notizia: l'83% dei veicoli recuperati da LoJack nel primo semestre 2026 è stato ritrovato entro 24 ore dalla denuncia ⏱️\n\nMorale: se ti rubano l'auto, denuncia SUBITO. Ogni ora conta.", "#furtoauto #denuncia #consigli"),
 # MER 18 - Incidenti
 ("num", "OGNI GIORNO", "Incidenti con feriti<br>sulle strade italiane", ("475", "al giorno nel 2024"), S_IS,
  "475 incidenti con feriti ogni giorno, 8 vittime al giorno ⚠️\n\nNel 2024 gli incidenti sono saliti del 4,1%. Non è un post simpatico, ma è uno di quelli da girare a chi guida.", "#sicurezzastradale #incidenti #istat"),
 ("num", "CAUSA N.1", "La prima causa di incidente<br>tra gli errori di guida", ("15,7%", "distrazione: 35.371 casi"), S_IS,
  "La distrazione è la prima causa di incidente tra i comportamenti alla guida: 15,7% dei casi 📱\n\nCon mancata precedenza e velocità arriva al 37,8%.\n\nIl telefono può aspettare. Sempre.", "#distrazione #cellulare #guida"),
 ("quiz", "QUIZ", "Dove crescono di più<br>gli incidenti?", ("strade o autostrade?", ["Città", "Autostrade", "Strade di campagna"], 1), S_IS,
  "Indovina: dove sono aumentati di più gli incidenti nel 2024? 🤔\n\nRisposta: in AUTOSTRADA, +6,9% incidenti e +7,1% vittime.\n\nL'avresti detto?", "#autostrada #quiz #sicurezzastradale"),
 ("vs", "ITALIA VS EUROPA", "Morti sulle strade<br>ogni milione di abitanti", (("Media UE", "45"), ("Italia", "51")), S_IS,
  "L'Italia ha 51 morti per incidente ogni milione di abitanti, la media UE è 45 🇮🇹🇪🇺\n\nSiamo al 19° posto in Europa. Margine di miglioramento: tanto.", "#sicurezzastradale #europa #dati"),
 ("book", "IN ARRIVO", "Vol. 3: decidere<br>e firmare", ("3", "trattativa, pagamento, passaggio"), "Guide da tasca SmileFix · in pubblicazione su Amazon",
  "📘 In arrivo su Amazon il Vol. 3 delle Guide da tasca SmileFix: «Decidere e firmare».\n\nIl semaforo per decidere, la trattativa, il pagamento sicuro e il passaggio di proprietà.\n\nE intanto il Vol. 2 è ancora GRATIS fino a venerdì: link in bio 📲", "#libri #autousata #kindle"),
 # GIO 19 - Usato e prezzi
 ("num", "PREZZO MEDIO", "Quanto costa un'auto<br>usata online?", ("21.270 €", "prezzo medio degli annunci"), S_AS,
  "21.270 euro: il prezzo medio delle auto usate in vendita su AutoScout24 💶\n\nE il budget medio di chi cerca è 20.000 euro (+11% in un anno). Il tuo budget per la prossima auto? Scrivilo 👇", "#autousata #prezzi #budget"),
 ("bars", "USATE PIÙ VENDUTE", "Le usate più vendute<br>del 2025", [("Fiat Panda", 3, "1ª"), ("Fiat 500", 2, "2ª"), ("Lancia Ypsilon", 1, "3ª")], S_AS,
  "Le usate più vendute del 2025: Panda, 500, Ypsilon 🇮🇹\n\nSì, sono le stesse della classifica dei furti di martedì. Coincidenza? No: più circolano, più valgono anche i loro pezzi.", "#autousata #fiat #classifica"),
 ("quiz", "QUIZ", "Base d'asta 6.000 €.<br>Quanto paghi davvero?", ("costo finale", ["6.000 €", "Meno di 6.000 €", "Di più, sempre"], 2), "SmileFix · come si calcola il costo di un'auto all'asta",
  "Base d'asta 6.000 €: quanto paghi davvero? 🔨\n\nRisposta: DI PIÙ, sempre. Rilanci, commissioni d'asta, IVA dove prevista, trasporto, passaggio, rimessa in strada.\n\nPrima di offrire si calcola il costo chiavi in mano. Vuoi un esempio vero? Commenta ASTA.", "#asteauto #aste #autousata"),
 ("vs", "PRIVATO VS ASTA", "Dove si rischia<br>di più?", (("Privato", "lo provi"), ("Asta", "spesso no")), "SmileFix · consigli per l'acquisto",
  "Privato o asta? 🤔\n\nDal privato di solito puoi provare l'auto. All'asta spesso vedi solo foto e scheda, ma il prezzo può essere molto interessante.\n\nTu dove compreresti? PRIVATO o ASTA nei commenti.", "#asteauto #autousata #sondaggio"),
 ("num", "SECOND HAND", "Quanto vale l'usato<br>dei veicoli in Italia", ("11,1 mld", "il primo settore della second hand"), "Fonte: Osservatorio Second Hand Economy 2025, IPSOS Doxa per Subito",
  "I veicoli sono il settore più grande della second hand economy italiana: 11,1 miliardi di euro 🔁\n\nL'usato non è più il piano B. È il mercato.", "#secondhand #autousata #economia"),
 # VEN 20 - Aste, furti parziali, recap
 ("num", "FURTI PARZIALI", "Rubano i pezzi,<br>non l'auto", ("5.000 €+", "di danni possibili per vettura"), "Fonte: LoJack Italia, report furti parziali 2025",
  "Non rubano l'auto: rubano i pezzi 🔧 Fari LED, gruppi ottici, paraurti, telecamere. Danni che possono superare i 5.000 euro.\n\nTi è mai successo? Racconta nei commenti.", "#furtiparziali #furti #auto"),
 ("num", "EUROPA", "Furti di veicoli ogni<br>100.000 abitanti", ("231", "Italia, 4ª in Europa"), S_EU,
  "Italia quarta in Europa per furti di veicoli rispetto alla popolazione: 231 ogni 100.000 abitanti 🇪🇺\n\nNon è un primato di cui vantarsi.", "#furti #europa #eurostat"),
 ("book", "ULTIMO GIORNO", "Vol. 2 gratis<br>solo oggi", ("2", "50 controlli in 5 zone"), "Guide da tasca SmileFix · Amazon Kindle",
  "⏳ ULTIMO GIORNO: il Vol. 2 «Il giro dell'auto» è gratis su Kindle solo fino a stasera.\n\n50 controlli in 5 zone e la prova su strada, da tenere sul telefono quando vai a vedere un'usata.\n\nLink in bio 📲", "#ebookgratis #ultimogiorno #kindle"),
 ("quiz", "RECAP", "Qual è il dato<br>che ti ha colpito?", ("della settimana", ["RC a 422 €", "Panda la più rubata", "475 incidenti al giorno"], -1), "Fonti: IVASS · LoJack · ACI-Istat",
  "Recap della settimana 📊\n\n💸 RC auto media 422 €\n🚗 Panda: quasi 1 auto rubata su 5\n⚠️ 475 incidenti con feriti al giorno\n\nQual è il dato che ti ha colpito di più? 1, 2 o 3 nei commenti 👇", "#recap #auto #dati"),
 ("num", "WEEKEND", "Prima di partire:<br>il controllo da 2 minuti", ("4", "luci · gomme · freni · tergicristalli"), "SmileFix · consiglio pratico",
  "Prima del weekend, 2 minuti di controllo 🚗\n\n💡 luci tutte accese\n🛞 gomme gonfie e senza crepe\n🛑 freni senza rumori strani\n🌧️ tergicristalli che puliscono bene\n\nPiccole cose che ti evitano grandi problemi. Salva e manda a chi parte.", "#weekend #manutenzione #consigli"),
]

# ---------------- FACEBOOK: 25 post "bacheca/giornale" (adulti, discussione, sondaggi) ----------------
# (kind, testata, title, data, source, text)
FB = [
 # LUN
 ("book", "Libri", "Gratis su Kindle fino a venerdì", ("2", "Il giro dell'auto"), "Guide da tasca SmileFix",
  "Da oggi a venerdì 20 novembre il secondo volume delle Guide da tasca SmileFix è gratis su Amazon Kindle.\n\n«Il giro dell'auto» è la guida per quando vai a vedere un'auto usata: 50 controlli divisi in 5 zone, la prova su strada e le tabelle a semaforo per capire cosa è un dettaglio e cosa è un campanello d'allarme.\n\n📚 Scaricala qui: " + AMZ2 + "\n\nSe conoscete qualcuno che sta cercando un'auto, giratelo: è gratis per pochi giorni."),
 ("num", "Sondaggio", "Quanto pagate di RC auto?", ("422 €", "media italiana, 2° trim. 2026"), S_IV,
  "Sondaggio della settimana 📊\n\nSecondo l'IVASS nel periodo aprile-giugno 2026 la RC auto è costata in media 422 euro: +1,6% in un anno, ma in leggero calo rispetto al trimestre precedente.\n\nVoi quanto pagate? Rispondete con:\nA) meno di 300 €\nB) tra 300 e 500 €\nC) più di 500 €\n\nE se avete trovato un trucco per pagare meno, condividetelo con gli altri."),
 ("vs", "Il confronto", "Stessa auto, due province", (("Aosta", "min"), ("Napoli", "+255 €")), S_IV,
  "Tra Napoli e Aosta la stessa copertura RC auto costa in media 255 euro di differenza.\n\nIl prezzo della polizza dipende da tanti fattori: provincia, età, classe di merito, auto, eventuali sinistri. Ecco perché il preventivo di un amico non vale per voi.\n\nIl consiglio pratico: prima di rinnovare, chiedete almeno tre preventivi con le stesse garanzie. Confrontate massimali, franchigie e garanzie accessorie, non solo il prezzo."),
 ("num", "Un po' di storia", "RC auto: oggi costa meno del 2014", ("−13,6%", "rispetto al 2° trimestre 2014"), S_IV,
  "Lo sapevate? Nonostante gli aumenti degli ultimi anni, la RC auto oggi costa meno di dieci anni fa.\n\nNel 2014 il premio medio superava i 488 euro, oggi siamo a 422: il 13,6% in meno. Ma rispetto al 2022, quando si pagavano circa 353 euro, la crescita si è fatta sentire.\n\nVoi vi ricordate quanto pagavate dieci anni fa?"),
 ("num", "Discussione", "Scatola nera: sì o no?", ("16%", "delle polizze RC auto"), S_IV,
  "Solo il 16% delle polizze RC auto ha la scatola nera, in calo rispetto al 17,2% di un anno fa.\n\nPro: spesso dà uno sconto e aiuta a ricostruire un incidente.\nContro: registra percorsi e stile di guida.\n\nVoi la montereste? Scrivete SÌ o NO e il perché."),
 # MAR
 ("num", "Cronaca in numeri", "136.201 veicoli rubati in un anno", ("+3%", "rispetto all'anno prima"), S_LJ,
  "Secondo il Dossier LoJack su dati del Ministero dell'Interno, nel 2024 in Italia sono stati rubati 136.201 veicoli, il 3% in più del 2023.\n\nPiù della metà sono automobili (56%), poi moto (23%), SUV e crossover (15%), furgoni (5%).\n\nA voi o a qualcuno che conoscete è mai successo?"),
 ("bars", "La classifica", "Le auto più rubate", [("Fiat Panda", 13311, "13.311"), ("Fiat 500", 5254, "5.254"), ("Lancia Ypsilon", 5048, "5.048")], S_LJ,
  "La Fiat Panda è l'auto più rubata d'Italia: 13.311 furti nel 2024, quasi una su cinque. Seguono Fiat 500 e Lancia Ypsilon.\n\nNon è un caso: sono tra le auto più diffuse e i loro ricambi hanno un mercato enorme.\n\nChi ha una Panda in famiglia? 🙋"),
 ("bars", "Mappa dei furti", "Cinque regioni, 78% dei furti", [("Campania", 23, "23%"), ("Lazio", 18, "18%"), ("Sicilia", 14, "14%"), ("Puglia e Lombardia", 23, "23%")], S_LJ,
  "Il 78% dei furti di veicoli avviene in cinque regioni: Campania, Lazio, Sicilia, Puglia e Lombardia.\n\nAnche la Lombardia è nella lista. Nella vostra zona come va? Scrivete la vostra città."),
 ("num", "Consigli utili", "Cosa fare se vi rubano l'auto", ("24 ore", "l'83% dei recuperi avviene entro"), S_LJ26,
  "Se vi rubano l'auto, la velocità conta. Secondo LoJack, nel primo semestre 2026 l'83% dei veicoli recuperati è stato ritrovato entro 24 ore dalla denuncia.\n\nCosa fare subito:\n1️⃣ Denuncia immediata alle Forze dell'Ordine\n2️⃣ Avvisate l'assicurazione (se avete la garanzia furto)\n3️⃣ Tenete a portata targa, telaio e documenti\n\nSalvate il post: speriamo non serva mai."),
 ("num", "Il dato che pesa", "Quanti ne tornano indietro?", ("45%", "media dei veicoli ritrovati"), S_LJ,
  "Solo il 45% dei veicoli rubati viene ritrovato, e per SUV e crossover la percentuale scende al 41%.\n\nMolti finiscono smontati per i ricambi o portati all'estero.\n\nVoi usate un antifurto oltre a quello di serie? Quale?"),
 # MER
 ("num", "Sicurezza", "475 incidenti al giorno", ("173.364", "incidenti con feriti nel 2024"), S_IS,
  "Nel 2024 in Italia ci sono stati 173.364 incidenti stradali con lesioni (+4,1%), 3.030 vittime e 233.853 feriti. In media 475 incidenti al giorno.\n\nNumeri che fanno riflettere. Condividete se pensate che servano più controlli o più educazione stradale."),
 ("bars", "Le cause", "Perché succedono gli incidenti", [("Distrazione", 15.7, "15,7%"), ("Precedenza", 13.5, "13,5%"), ("Velocità", 8.6, "8,6%")], S_IS,
  "Distrazione, mancata precedenza e velocità: insieme fanno il 37,8% delle cause di incidente individuate.\n\nLa prima resta la distrazione. Il telefono in mano mentre si guida è ancora troppo diffuso.\n\nVoi lo usate in vivavoce o lo tenete proprio lontano?"),
 ("num", "Autostrade", "Dove crescono di più", ("+6,9%", "incidenti in autostrada"), S_IS,
  "Nel 2024 gli incidenti in autostrada sono aumentati del 6,9% e le vittime del 7,1%: la crescita più forte tra tutti i tipi di strada.\n\nVelocità, stanchezza, distanze di sicurezza. Qual è secondo voi il problema principale in autostrada?"),
 ("vs", "Confronto europeo", "Italia sopra la media UE", (("Media UE", "45"), ("Italia", "51")), S_IS,
  "L'Italia ha 51 morti per incidente stradale ogni milione di abitanti, contro una media UE di 45. Siamo al 19° posto in Europa.\n\nIl costo sociale degli incidenti con feriti è stimato in circa 18 miliardi di euro, quasi l'1% del PIL.\n\nCosa cambiereste per primo?"),
 ("book", "In uscita", "Vol. 3: Decidere e firmare", ("3", "in pubblicazione su Amazon"), "Guide da tasca SmileFix",
  "Sta arrivando su Amazon il terzo volume delle Guide da tasca SmileFix: «Decidere e firmare».\n\nÈ la parte finale dell'acquisto: il semaforo per decidere, la trattativa, il pagamento sicuro, cosa scrivere e il passaggio di proprietà.\n\nCon il Vol. 1 (da casa) e il Vol. 2 (sul posto) il metodo è completo. E il Vol. 2 è gratis fino a venerdì: " + AMZ2),
 # GIO
 ("num", "Mercato", "Il prezzo medio dell'usato", ("21.270 €", "prezzo medio annunci AutoScout24"), S_AS,
  "Il prezzo medio delle auto usate in vendita su AutoScout24 è di 21.270 euro, mentre il budget medio di chi cerca un'usata è salito a 20.000 euro (+11% in un anno).\n\nVoi quanto pensate di spendere per la prossima auto? Scrivetelo, anche a grandi linee."),
 ("bars", "Classifica", "Le usate più vendute del 2025", [("Fiat Panda", 3, "1ª"), ("Fiat 500", 2, "2ª"), ("Lancia Ypsilon", 1, "3ª")], S_AS,
  "Le auto usate più vendute in Italia nel 2025 sono Fiat Panda, Fiat 500 e Lancia Ypsilon.\n\nCuriosamente sono anche le tre più rubate. Tra le tre, voi quale scegliereste?"),
 ("quiz", "Aste", "Base d'asta 6.000 euro: quanto si paga?", ("il costo vero", ["6.000 €", "Meno", "Di più"], 2), "SmileFix · come si calcola il costo all'asta",
  "Vedete un'auto all'asta con base 6.000 euro. Quanto pagherete davvero?\n\nSempre di più. Al prezzo di aggiudicazione si aggiungono, a seconda dell'asta, commissioni o diritti d'asta, IVA dove prevista, trasporto, passaggio di proprietà ed eventuale rimessa in strada (batteria, gomme, tagliando).\n\nPer questo prima di fare un'offerta si calcola il costo chiavi in mano e lo si confronta con il mercato. Vi interessa un esempio con un'auto vera? Scrivete ASTA nei commenti."),
 ("vs", "Sondaggio", "Privato o asta?", (("Privato", "la provi"), ("Asta", "spesso no")), "SmileFix · consigli per l'acquisto",
  "Sondaggio: per la vostra prossima auto usata, comprereste da\nA) un privato\nB) un concessionario\nC) un'asta\n\nOgnuno ha pro e contro: il privato costa meno ma senza garanzia del rivenditore, il concessionario offre la garanzia legale, l'asta può far risparmiare ma richiede esperienza.\n\nVotate nei commenti!"),
 ("num", "Economia", "L'usato vale 11,1 miliardi", ("11,1 mld", "veicoli nella second hand economy"), "Fonte: Osservatorio Second Hand Economy 2025, IPSOS Doxa per Subito",
  "I veicoli sono il primo settore della second hand economy italiana, con un valore di 11,1 miliardi di euro.\n\nL'usato non è più una scelta di ripiego: è il modo in cui la maggior parte degli italiani compra l'auto."),
 # VEN
 ("num", "Attenzione", "I furti parziali", ("5.000 €+", "di danni possibili per auto"), "Fonte: LoJack Italia, report furti parziali 2025",
  "Cresce il fenomeno dei furti parziali: non rubano l'auto, ma i pezzi. Fari LED, gruppi ottici, paraurti, telecamere e monitor, con danni che possono superare i 5.000 euro.\n\nVi è mai capitato di trovare l'auto senza fari o senza paraurti?"),
 ("num", "Europa", "Italia quarta per furti", ("231", "furti ogni 100.000 abitanti"), S_EU,
  "Secondo i dati Eurostat sulle denunce, l'Italia è quarta in Europa per furti di veicoli rispetto alla popolazione: 231 ogni 100.000 abitanti.\n\nCosa usate per proteggere l'auto? Bloccasterzo, antifurto satellitare, garage?"),
 ("book", "Ultimo giorno", "Vol. 2 gratis solo oggi", ("2", "Il giro dell'auto"), "Guide da tasca SmileFix",
  "Ultimo giorno per scaricare gratis su Kindle il Vol. 2 delle Guide da tasca SmileFix, «Il giro dell'auto».\n\n50 controlli in 5 zone e la prova su strada: tutto quello che serve guardare quando andate a vedere un'auto usata.\n\n📚 " + AMZ2),
 ("quiz", "Riepilogo", "I numeri della settimana", ("quale vi ha colpito?", ["RC media 422 €", "Panda più rubata", "475 incidenti al giorno"], -1), "Fonti: IVASS · LoJack · ACI-Istat",
  "Il riepilogo della settimana:\n\n1️⃣ RC auto media: 422 euro (IVASS)\n2️⃣ Fiat Panda: quasi un'auto rubata su cinque (LoJack)\n3️⃣ 475 incidenti con feriti al giorno (ACI-Istat)\n\nQuale dato vi ha sorpreso di più? Rispondete 1, 2 o 3."),
 ("num", "Weekend", "Il controllo prima di partire", ("4", "luci · gomme · freni · tergicristalli"), "SmileFix · consiglio pratico",
  "Prima di partire per il weekend, due minuti di controllo:\n\n💡 Luci: accendetele tutte, anche stop e frecce\n🛞 Gomme: pressione e crepe sui fianchi\n🛑 Freni: nessun rumore o vibrazione\n🌧️ Tergicristalli: devono pulire senza lasciare strisce\n\nBuon weekend e guidate con prudenza!"),
]

# ---------------- TELEGRAM: 7 bollettini (09:00) ----------------
TG = [
 ("2026-11-16", "💸 RC auto: i numeri IVASS", ["Premio medio: 422 € (2° trim. 2026)", "+1,6% in un anno, −0,4% sul trimestre", "Napoli-Aosta: 255 € di differenza", "Scatola nera nel 16% delle polizze", "📚 Vol. 2 gratis su Kindle fino al 20/11"], S_IV),
 ("2026-11-17", "🚨 Furti di veicoli in Italia", ["136.201 veicoli rubati (+3%)", "Fiat Panda: 13.311, quasi 1 su 5", "78% dei furti in 5 regioni", "Ritrovati in media il 45%", "Commerciali: +112% in un anno"], S_LJ),
 ("2026-11-18", "⚠️ Incidenti stradali 2024", ["173.364 incidenti con feriti (+4,1%)", "3.030 vittime, 233.853 feriti", "Distrazione: 15,7% delle cause", "Autostrade: +6,9% incidenti", "Italia 51 morti per milione, UE 45"], S_IS),
 ("2026-11-19", "💶 L'usato in numeri", ["Prezzo medio annunci: 21.270 €", "Budget medio di chi cerca: 20.000 € (+11%)", "Più vendute: Panda, 500, Ypsilon", "Veicoli: 11,1 mld nella second hand"], "Fonti: Osservatorio AutoScout24 · IPSOS Doxa per Subito"),
 ("2026-11-20", "🔨 Auto all'asta: il costo vero", ["Il prezzo finale supera sempre la base", "+ commissioni o diritti d'asta", "+ IVA dove prevista e trasporto", "+ passaggio e rimessa in strada", "Confronta il totale con il mercato"], "SmileFix · guida pratica alle aste"),
 ("2026-11-21", "🔧 Furti parziali: cosa rubano", ["Fari LED e gruppi ottici", "Paraurti", "Telecamere e monitor", "Danni oltre 5.000 € per auto"], "Fonte: LoJack Italia, report furti parziali 2025"),
 ("2026-11-22", "📚 Guide da tasca SmileFix", ["Vol. 1: le verifiche da casa", "Vol. 2: 50 controlli sul posto", "Vol. 3: decidere e firmare", "Su Amazon, Kindle e cartaceo"], "smilefixbroker.com/link"),
]

# ---------------- BLUESKY: 5 (18:00) ----------------
BS = [
 ("2026-11-16", "IVASS, 2° trimestre 2026: RC auto media 422 €, +1,6% annuo e −0,4% sul trimestre. Tra Napoli e Aosta 255 € di differenza. #auto #assicurazioni"),
 ("2026-11-17", "Furti di veicoli in Italia nel 2024: 136.201 (+3%). Fiat Panda la più rubata con 13.311 casi, quasi 1 su 5.\n\nFonte: LoJack su dati Ministero dell'Interno"),
 ("2026-11-18", "ACI-Istat 2024: 173.364 incidenti con feriti (+4,1%), 3.030 vittime. Distrazione prima causa tra i comportamenti alla guida (15,7%). #sicurezzastradale"),
 ("2026-11-19", "Prezzo medio delle auto usate in vendita su AutoScout24: 21.270 €. Budget medio di chi cerca: 20.000 €, +11% in un anno. #auto"),
 ("2026-11-20", "LoJack, 1° semestre 2026: 1.230 veicoli recuperati (+20%), l'83% entro 24 ore dalla denuncia. Denunciare subito fa la differenza."),
]

# ---------------- PINTEREST: 5 poster "checklist" (09:00) ----------------
PIN = [
 ("2026-11-16", "RC auto: come pagare meno, 5 cose da confrontare", "list", ["Stesse garanzie in ogni preventivo", "Massimali e franchigie", "Classe di merito e attestato", "Garanzie accessorie davvero utili", "Scatola nera: sconto e privacy"], S_IV,
  "Come confrontare i preventivi RC auto: garanzie, massimali, franchigie, classe di merito, scatola nera. Premio medio IVASS 2° trimestre 2026: 422 euro. #rcauto #assicurazioneauto #risparmio"),
 ("2026-11-17", "Auto rubata: cosa fare subito, passo dopo passo", "list", ["Denuncia immediata", "Avvisa l'assicurazione", "Prepara targa, telaio, documenti", "Segnala eventuali localizzatori", "Conserva copia della denuncia"], S_LJ26,
  "Cosa fare se ti rubano l'auto: denuncia immediata, assicurazione, documenti. L'83% dei recuperi LoJack avviene entro 24 ore dalla denuncia. #furtoauto #autorubata #consigli"),
 ("2026-11-18", "Sicurezza stradale: le 3 cause principali di incidente", "bars", [("Distrazione", 15.7, "15,7%"), ("Precedenza", 13.5, "13,5%"), ("Velocità", 8.6, "8,6%")], S_IS,
  "Le principali cause di incidente in Italia secondo ACI-Istat 2024: distrazione 15,7%, mancata precedenza, velocità. Insieme il 37,8% delle cause. #sicurezzastradale #guidasicura #incidenti"),
 ("2026-11-19", "Auto all'asta: come calcolare il costo finale", "list", ["Prezzo di aggiudicazione", "Commissioni o diritti d'asta", "IVA dove prevista", "Trasporto e passaggio", "Rimessa in strada"], "SmileFix · guida pratica",
  "Come calcolare il costo reale di un'auto comprata all'asta: aggiudicazione, commissioni, IVA, trasporto, passaggio di proprietà, rimessa in strada. #asteauto #autousata #risparmio"),
 ("2026-11-20", "Furti d'auto: i 5 consigli per proteggerla", "list", ["Bloccasterzo visibile", "Antifurto satellitare", "Parcheggio illuminato o garage", "Chiavi keyless in custodia schermata", "Mai documenti in auto"], S_LJ,
  "Come proteggere l'auto dai furti: bloccasterzo, antifurto satellitare, parcheggio, chiavi keyless schermate. In Italia 136.201 veicoli rubati nel 2024. #antifurto #furtiauto #sicurezza"),
]

# ---------------- THREADS: 5 (Metricool, 13:00) ----------------
TH = [
 ("2026-11-16", "RC auto media in Italia: 422 € (IVASS).\n\nConfessione: quanto pagate voi? Prometto che non giudico 😅"),
 ("2026-11-17", "La Panda è l'auto più venduta d'Italia.\nE anche la più rubata: quasi 1 furto su 5.\n\nEssere popolari ha un prezzo 🫠"),
 ("2026-11-18", "La prima causa di incidente tra gli errori di guida? La distrazione (ACI-Istat).\n\nOnestamente: quante volte avete guardato il telefono al semaforo oggi? 👀"),
 ("2026-11-19", "Base d'asta 6.000 €.\nPrezzo finale? Sempre di più.\n\nVolete che vi mostri il conto vero di un'auto all'asta? Scrivete 'sì' 👇"),
 ("2026-11-20", "Furti parziali: rubano fari e paraurti e lasciano l'auto.\n\nIl colmo è ritrovarla… senza faccia 😶 È mai successo a qualcuno?"),
]

# ---------------- X: 3 (Buffer, 12:00) ----------------
XP = [
 ("2026-11-17T12:00:00+01:00", "Furti di veicoli in Italia (2024):\n🚗 136.201 (+3%)\n🥇 Fiat Panda: 13.311\n🗺️ 78% in 5 regioni\n\nFonte: LoJack su dati Min. Interno"),
 ("2026-11-19T12:00:00+01:00", "Usato in Italia:\n💶 prezzo medio annunci 21.270 €\n🎯 budget medio 20.000 € (+11%)\n🏆 più vendute: Panda, 500, Ypsilon\n\nFonte: AutoScout24"),
 ("2026-11-21T12:00:00+01:00", "Incidenti 2024:\n⚠️ 173.364 (+4,1%)\n📱 distrazione 15,7%\n🛣️ autostrade +6,9%\n🇮🇹 51 morti/mln vs UE 45\n\nFonte: ACI-Istat"),
]

# ---------------- MASTODON: 3 (Buffer, 10:00) ----------------
MA = [
 ("2026-11-16T10:00:00+01:00", "IVASS, indagine IPER 2° trimestre 2026: premio medio RC auto 422 €, +1,6% su base annua, −0,4% sul trimestre. In termini reali il prezzo cala dell'1,3%. #auto #assicurazioni #Italia"),
 ("2026-11-18T10:00:00+01:00", "ACI-Istat, incidenti 2024: 173.364 con lesioni (+4,1%), 3.030 morti (−0,3%), 233.853 feriti. Distrazione, precedenza e velocità = 37,8% delle cause. #sicurezzastradale"),
 ("2026-11-20T10:00:00+01:00", "LoJack: nel 1° semestre 2026 recuperati 1.230 veicoli rubati (+20%), l'83% entro 24 ore dalla denuncia. Nel 2024 i furti in Italia sono stati 136.201. #furti #auto"),
]

# ---------------- LINKEDIN: 3 analisi (09:00) ----------------
LI = [
 ("2026-11-17T09:00:00+01:00", "Flotte e furti", "Furti di veicoli:<br>cosa cambia per le aziende", ["136.201 veicoli rubati nel 2024 (+3%)", "Commerciali: +112% in un anno", "Recupero medio: 45% (SUV 41%)"],
  "Per chi gestisce mezzi aziendali, i furti sono un costo sottovalutato.\n\nSecondo il Dossier LoJack su dati del Ministero dell'Interno, nel 2024 in Italia sono stati rubati 136.201 veicoli, il 3% in più del 2023. Il dato che più interessa le aziende: i furti di veicoli commerciali sono più che raddoppiati (+112%).\n\nSolo il 45% dei veicoli rubati viene ritrovato (41% per SUV e crossover). E nel primo semestre 2026 l'83% dei recuperi LoJack è avvenuto entro 24 ore dalla denuncia: tempi di reazione e procedure interne contano.\n\nTre domande per chi gestisce una flotta:\n• i mezzi hanno un sistema di localizzazione attivo?\n• esiste una procedura chiara in caso di furto?\n• la polizza copre il fermo del mezzo?\n\n#flotte #fleetmanagement #automotive #sicurezza"),
 ("2026-11-19T09:00:00+01:00", "Assicurazioni", "RC auto 2026:<br>prezzi e differenze", ["Premio medio 422 € (2° trim. 2026)", "Napoli-Aosta: 255 € di differenza", "Scatola nera: 16% dei contratti"],
  "Il prezzo dell'RC auto sta rallentando.\n\nL'indagine IPER dell'IVASS sul 2° trimestre 2026 indica un premio medio di 422 euro: +1,6% su base annua, −0,4% sul trimestre precedente, −1,3% in termini reali.\n\nRestano forti le differenze territoriali (255 euro tra Napoli e Aosta) e cala la diffusione della scatola nera, presente nel 16% dei contratti contro il 17,2% di un anno fa.\n\nPer chi compra un'auto, il costo dell'assicurazione andrebbe messo nel conto prima della firma, non dopo: modello, alimentazione e provincia lo cambiano molto.\n\n#assicurazioni #rcauto #automotive #mobilità"),
 ("2026-11-20T09:00:00+01:00", "Aste di veicoli", "Comprare all'asta:<br>il costo che non si vede", ["Aggiudicazione sopra la base", "Commissioni, IVA, trasporto", "Passaggio e rimessa in strada"],
  "Le aste di veicoli attirano sempre più attenzione, privati compresi. Il prezzo di partenza però racconta solo una parte della storia.\n\nIl costo reale di un veicolo all'asta si costruisce così:\n• prezzo di aggiudicazione, quasi sempre sopra la base\n• commissioni o diritti d'asta, IVA dove prevista\n• trasporto dal luogo in cui si trova il veicolo\n• passaggio di proprietà e pratiche\n• rimessa in strada: batteria, pneumatici, tagliando, a volte revisione\n\nA questo si aggiunge un rischio: spesso il veicolo non si può provare.\n\nIl metodo che uso: calcolare il costo chiavi in mano e confrontarlo con lo stesso modello sul mercato, con un margine di sicurezza. Se il margine non c'è, si passa al lotto successivo.\n\n#aste #automotive #usato #acquisti"),
]

# ---------------- STORIE IG/FB (le pubblica Enea, 12:30) ----------------
ST = [
 ("2026-11-16", "Sondaggio", "Quanto paghi di RC?", ["Meno di 300 €", "300–500 €", "Più di 500 €"], "Media Italia: 422 € (IVASS)"),
 ("2026-11-17", "Quiz", "L'auto più rubata?", ["A · Fiat 500", "B · Fiat Panda", "Risposta: B, 13.311 furti"], "Fonte: LoJack, dati 2024"),
 ("2026-11-18", "Domanda", "Telefono alla guida?", ["Mai", "Solo vivavoce", "Ogni tanto 🙈"], "Distrazione: 15,7% delle cause"),
 ("2026-11-19", "Sondaggio", "Compreresti all'asta?", ["Sì, se conviene", "No, troppo rischio"], "Scrivi ASTA per un esempio"),
 ("2026-11-20", "Ultimo giorno", "Vol. 2 gratis", ["50 controlli in 5 zone", "La prova su strada"], "Link in bio 📲"),
]

# ---------------- VIDEO (nuovo design "tabloid pop") ----------------
# scene: hook(kick,title) list(title,items) vs(a,ai,b,bi) big(kick,num,text) bars(title,rows,src) cta(title,text) quiz(question,[opts],correct) meme(top,bottom)
TT_TAGS = "#auto #motori #autotok #imparacontiktok #automobili"
TT = [
 # LUN 16
 ("t01", [("meme", "Io che rinnovo l'RC auto", "convinto di risparmiare 🥲"), ("big", "Media Italia 2026", "422 €", "premio RC auto, fonte IVASS"), ("cta", "Tu quanto paghi?", "Scrivilo nei commenti")], "Quanto paghi di RC auto? La media è 422 € 💸 Fonte IVASS"),
 ("t02", [("hook", "Stessa polizza", "Due città, <em>255 €</em> di differenza"), ("vs", "Aosta", ["+ La provincia più economica"], "Napoli", ["- 255 € in più in media"]), ("cta", "Il preventivo", "è solo tuo")], "Napoli vs Aosta: 255 € di differenza sull'RC auto 😳 Fonte IVASS"),
 ("t03", [("quiz", "Nel 2014 l'RC auto costava…", ["Meno di oggi", "Uguale", "Più di oggi"], 2), ("big", "2014 vs 2026", "−13,6%", "oggi si paga meno del 2014"), ("cta", "L'avresti detto?", "Fonte: IVASS")], "Quiz: l'RC auto costava di più nel 2014? 🤔 Fonte IVASS"),
 ("t04", [("hook", "Gratis su Kindle", "Il Vol. 2 è <em>gratis</em> fino a venerdì"), ("list", "Dentro trovi", ["50 controlli in 5 zone", "La prova su strada", "Tabelle a semaforo"]), ("cta", "Cerca su Amazon", "Il giro dell'auto SmileFix")], "📚 Il Vol. 2 «Il giro dell'auto» è GRATIS su Kindle fino al 20/11. Link in bio"),
 # MAR 17
 ("t05", [("meme", "I ladri quando vedono", "una Panda parcheggiata 👀"), ("big", "Auto più rubata", "Panda", "13.311 furti: quasi 1 su 5"), ("cta", "Ce l'hai anche tu?", "Fonte: LoJack 2024")], "La Panda è anche l'auto più rubata d'Italia 😬 Fonte LoJack"),
 ("t06", [("hook", "In un anno", "Quanti veicoli <em>spariscono?</em>"), ("big", "Furti 2024", "136.201", "più di 370 al giorno"), ("cta", "Segui per i consigli", "antifurto di domani")], "136.201 veicoli rubati in un anno in Italia 🚨 Fonte LoJack"),
 ("t07", [("quiz", "La regione con più furti?", ["Lombardia", "Campania", "Lazio"], 1), ("bars", "Quota dei furti", [("Campania", 23, "23%"), ("Lazio", 18, "18%"), ("Sicilia", 14, "14%")], "LoJack 2024"), ("cta", "La tua regione?", "Scrivila nei commenti")], "Indovina la regione con più furti d'auto 🗺️ Fonte LoJack"),
 ("t08", [("hook", "Ti rubano l'auto?", "Fai <em>subito</em> questo"), ("list", "Entro un'ora", ["Denuncia immediata", "Avvisa l'assicurazione", "Prepara targa e telaio"]), ("big", "Recuperi LoJack 2026", "83%", "entro 24 ore dalla denuncia")], "Ti rubano l'auto? Ecco cosa fare subito ⏱️ Fonte LoJack"),
 # MER 18
 ("t09", [("meme", "Io: 'guardo solo un attimo'", "il telefono al volante 📱"), ("big", "Prima causa", "15,7%", "degli incidenti: distrazione"), ("cta", "Il telefono aspetta", "Tu no")], "La distrazione è la prima causa di incidente 📱 Fonte ACI-Istat"),
 ("t10", [("hook", "Ogni giorno in Italia", "Quanti incidenti <em>con feriti?</em>"), ("big", "Media 2024", "475", "al giorno, 8 vittime al giorno"), ("cta", "Gira il video", "a chi guida")], "475 incidenti con feriti al giorno in Italia ⚠️ Fonte ACI-Istat"),
 ("t11", [("quiz", "Dove crescono di più gli incidenti?", ["In città", "In autostrada", "In montagna"], 1), ("big", "Autostrade 2024", "+6,9%", "incidenti, +7,1% vittime"), ("cta", "Occhio alla distanza", "di sicurezza")], "Quiz: dove crescono gli incidenti? In autostrada 🛣️ Fonte ACI-Istat"),
 ("t12", [("hook", "Vol. 3 in arrivo", "Decidere e <em>firmare</em>"), ("list", "Cosa c'è dentro", ["Il semaforo per decidere", "La trattativa", "Pagamento e passaggio"]), ("cta", "Intanto il Vol. 2", "è gratis fino a venerdì")], "📘 In arrivo il Vol. 3 delle Guide da tasca SmileFix. Il Vol. 2 è gratis fino al 20/11"),
 # VEN 20
 ("t13", [("meme", "Base d'asta: 6.000 €", "Io: affare fatto! 🤑"), ("list", "Poi arrivano", ["Commissioni d'asta", "Trasporto", "Passaggio e gomme"]), ("cta", "Il prezzo vero", "è sempre più alto")], "Base d'asta 6.000 €: quanto paghi davvero? 🔨"),
 ("t14", [("hook", "Furti parziali", "Ti lasciano l'auto, <em>senza fari</em>"), ("list", "Cosa rubano", ["Fari LED", "Paraurti", "Telecamere"]), ("big", "Danni possibili", "5.000 €+", "per una sola auto")], "Furti parziali: rubano fari e paraurti 🔧 Fonte LoJack"),
 ("t15", [("hook", "Ultimo giorno", "Il Vol. 2 è gratis <em>solo oggi</em>"), ("list", "Il giro dell'auto", ["50 controlli", "5 zone", "Prova su strada"]), ("cta", "Link in bio", "Gratis fino a stasera")], "⏳ Ultimo giorno: Vol. 2 gratis su Kindle. Link in bio"),
 ("t16", [("quiz", "L'Italia in Europa per furti?", ["1ª", "4ª", "10ª"], 1), ("big", "Ogni 100.000 abitanti", "231", "furti di veicoli"), ("cta", "Non è un primato", "da vantare")], "Italia 4ª in Europa per furti di veicoli 🇪🇺 Fonte Eurostat"),
 # SAB 21
 ("t17", [("hook", "Usato", "Quanto costa <em>in media?</em>"), ("big", "Annunci AutoScout24", "21.270 €", "prezzo medio auto usate"), ("cta", "Il tuo budget?", "Scrivilo nei commenti")], "Prezzo medio di un'auto usata: 21.270 € 💶 Fonte AutoScout24"),
 ("t18", [("meme", "Le usate più vendute", "e le più rubate… sono le stesse 🤡"), ("list", "Top 3 di entrambe", ["Fiat Panda", "Fiat 500", "Lancia Ypsilon"]), ("cta", "Coincidenza?", "No: più circolano, più valgono i pezzi")], "Le usate più vendute sono anche le più rubate 🤡 Fonti AutoScout24 e LoJack"),
 ("t19", [("hook", "Prima del weekend", "Il controllo da <em>2 minuti</em>"), ("list", "Controlla", ["Luci", "Gomme", "Freni", "Tergicristalli"]), ("cta", "Salva il video", "e buon viaggio")], "Il controllo da 2 minuti prima di partire 🚗"),
 ("t20", [("hook", "Recap della settimana", "3 dati <em>da ricordare</em>"), ("list", "Dati", ["RC media: 422 €", "Panda: 1 rubata su 5", "475 incidenti al giorno"]), ("cta", "Quale ti ha colpito?", "Scrivi 1, 2 o 3")], "Recap: 3 dati auto della settimana 📊"),
]

YT_TAGS = "#auto #autousate #motori"
YT = [
 # LUN 16
 ("y01", [("hook", "RC auto 2026", "Quanto si paga <em>davvero</em>"), ("big", "IVASS, 2° trim. 2026", "422 €", "premio medio RC auto"), ("list", "In sintesi", ["+1,6% in un anno", "−0,4% sul trimestre", "−1,3% in termini reali"])], "RC auto 2026: il premio medio è 422 euro #shorts", "Dati IVASS (indagine IPER) sul 2° trimestre 2026: premio medio RC auto 422 euro, +1,6% annuo, −0,4% sul trimestre precedente."),
 ("y02", [("hook", "Preventivi RC", "Come <em>confrontarli</em>"), ("list", "Controlla sempre", ["Stesse garanzie", "Massimali e franchigie", "Classe di merito", "Garanzie accessorie"]), ("cta", "Il prezzo da solo", "non basta")], "Come confrontare i preventivi RC auto #shorts", "Cosa controllare nei preventivi RC auto oltre al prezzo: garanzie, massimali, franchigie e classe di merito."),
 ("y03", [("hook", "Scatola nera", "Conviene <em>davvero?</em>"), ("big", "Polizze con scatola nera", "16%", "era il 17,2% un anno fa"), ("vs", "Pro", ["+ Spesso uno sconto", "+ Aiuta a ricostruire un incidente"], "Contro", ["- Registra percorsi", "- Registra lo stile di guida"])], "Scatola nera RC auto: pro e contro #shorts", "Secondo IVASS la scatola nera è presente nel 16% dei contratti RC auto (2° trimestre 2026)."),
 ("y04", [("hook", "Ebook gratis", "Il giro dell'auto: <em>Vol. 2</em>"), ("list", "Cosa contiene", ["50 controlli in 5 zone", "La prova su strada", "Tabelle a semaforo"]), ("cta", "Gratis su Kindle", "fino al 20 novembre")], "Ebook gratis: cosa controllare quando vai a vedere un'auto usata #shorts", "Il Vol. 2 delle Guide da tasca SmileFix, «Il giro dell'auto», è gratis su Amazon Kindle dal 16 al 20 novembre 2026.\n\n📚 " + AMZ2),
 # MAR 17
 ("y05", [("hook", "Furti 2024", "I numeri <em>in Italia</em>"), ("big", "Veicoli rubati", "136.201", "+3% rispetto al 2023"), ("bars", "Cosa viene rubato", [("Auto", 56, "56%"), ("Moto", 23, "23%"), ("SUV e crossover", 15, "15%"), ("Furgoni", 5, "5%")], "LoJack 2024")], "Furti di veicoli in Italia: 136.201 nel 2024 #shorts", "Dossier LoJack 2025 su dati del Ministero dell'Interno: nel 2024 rubati 136.201 veicoli in Italia."),
 ("y06", [("hook", "Le più rubate", "La classifica <em>2024</em>"), ("bars", "Furti per modello", [("Fiat Panda", 13311, "13.311"), ("Fiat 500", 5254, "5.254"), ("Lancia Ypsilon", 5048, "5.048")], "LoJack 2024"), ("cta", "Più diffuse", "più ricercate")], "Le auto più rubate in Italia #shorts", "Fiat Panda, Fiat 500 e Lancia Ypsilon le auto più rubate nel 2024 secondo il Dossier LoJack."),
 ("y07", [("hook", "Antifurto", "5 modi per <em>proteggere</em> l'auto"), ("list", "Consigli", ["Bloccasterzo visibile", "Localizzatore satellitare", "Parcheggio illuminato", "Chiave keyless schermata", "Niente documenti in auto"]), ("cta", "Recupero medio", "solo il 45% dei veicoli")], "Come proteggere l'auto dai furti #shorts", "Consigli pratici antifurto. Solo il 45% dei veicoli rubati viene ritrovato (LoJack)."),
 ("y08", [("hook", "Auto rubata", "Cosa fare nelle <em>prime ore</em>"), ("list", "Subito", ["Denuncia alle Forze dell'Ordine", "Avvisa l'assicurazione", "Tieni pronti targa e telaio"]), ("big", "LoJack, 1° sem. 2026", "83%", "dei recuperi entro 24 ore")], "Ti hanno rubato l'auto? Cosa fare subito #shorts", "Nel primo semestre 2026 l'83% dei veicoli recuperati da LoJack è stato ritrovato entro 24 ore dalla denuncia."),
 # MER 18
 ("y09", [("hook", "Incidenti 2024", "I dati <em>ACI-Istat</em>"), ("list", "Numeri", ["173.364 incidenti con feriti", "3.030 vittime", "233.853 feriti", "475 incidenti al giorno"]), ("cta", "Fonte", "ACI-Istat 2024")], "Incidenti stradali 2024 in Italia: i numeri #shorts", "Report ACI-Istat: 173.364 incidenti con lesioni nel 2024 (+4,1%), 3.030 vittime, 233.853 feriti."),
 ("y10", [("hook", "Le cause", "Perché si fanno <em>incidenti</em>"), ("bars", "Comportamenti errati", [("Distrazione", 15.7, "15,7%"), ("Precedenza", 13.5, "13,5%"), ("Velocità", 8.6, "8,6%")], "ACI-Istat 2024"), ("cta", "Insieme", "il 37,8% delle cause")], "Le 3 cause principali degli incidenti #shorts", "Distrazione, mancata precedenza e velocità: il 37,8% delle cause di incidente secondo ACI-Istat 2024."),
 ("y11", [("hook", "Italia vs Europa", "Morti <em>sulle strade</em>"), ("vs", "Media UE", ["45 morti per milione"], "Italia", ["51 morti per milione", "19° posto in UE"]), ("cta", "Costo sociale", "circa l'1% del PIL")], "Sicurezza stradale: Italia sopra la media UE #shorts", "L'Italia registra 51 morti per incidente ogni milione di abitanti, contro 45 della media UE (ACI-Istat 2024)."),
 ("y12", [("hook", "Guide da tasca SmileFix", "Il metodo in <em>3 volumi</em>"), ("list", "La collana", ["Vol. 1: da casa", "Vol. 2: sul posto", "Vol. 3: alla firma"]), ("cta", "Vol. 2 gratis", "fino al 20 novembre")], "Comprare un'auto usata in 3 passi: la collana SmileFix #shorts", "Guide da tasca SmileFix: Vol. 1 le verifiche da casa, Vol. 2 i controlli sul posto (gratis su Kindle fino al 20/11), Vol. 3 decidere e firmare.\n\n📚 " + AMZ2),
 # VEN 20
 ("y13", [("hook", "Auto all'asta", "Il costo <em>vero</em>"), ("list", "Oltre alla base d'asta", ["Rilanci", "Commissioni o diritti", "IVA dove prevista", "Trasporto", "Passaggio e rimessa in strada"]), ("cta", "Calcola il totale", "e confrontalo col mercato")], "Auto all'asta: come calcolare il costo finale #shorts", "Cosa si aggiunge al prezzo di un'auto all'asta: commissioni, IVA, trasporto, passaggio di proprietà e rimessa in strada."),
 ("y14", [("hook", "Privato, concessionario, asta", "Dove <em>conviene?</em>"), ("list", "In breve", ["Privato: prezzo, niente garanzia rivenditore", "Concessionario: garanzia legale", "Asta: risparmio possibile, più rischio"]), ("cta", "Scegli in base", "al tuo tempo e alla tua esperienza")], "Auto usata: privato, concessionario o asta? #shorts", "Pro e contro dei tre canali per comprare un'auto usata."),
 ("y15", [("hook", "Furti parziali", "Il nuovo <em>fenomeno</em>"), ("list", "Pezzi più rubati", ["Fari e gruppi ottici", "Paraurti", "Telecamere e monitor"]), ("big", "Danni possibili", "5.000 €+", "per singola auto")], "Furti parziali d'auto: cosa rubano #shorts", "Secondo LoJack crescono i furti parziali: fari, paraurti, telecamere, con danni oltre 5.000 euro."),
 ("y16", [("hook", "Ultimo giorno", "Ebook gratis <em>Vol. 2</em>"), ("list", "Il giro dell'auto", ["Carrozzeria e vetri", "Interni e motore", "Prova su strada"]), ("cta", "Gratis su Kindle", "solo fino a stasera")], "Ultimo giorno: ebook gratis sull'auto usata #shorts", "Ultimo giorno per scaricare gratis il Vol. 2 delle Guide da tasca SmileFix.\n\n📚 " + AMZ2),
 # SAB 21
 ("y17", [("hook", "Mercato usato", "Prezzi e <em>budget</em>"), ("vs", "Prezzo medio annunci", ["21.270 €"], "Budget medio", ["20.000 €", "+11% in un anno"]), ("cta", "Fonte", "Osservatorio AutoScout24")], "Quanto costa un'auto usata oggi #shorts", "Prezzo medio delle auto usate su AutoScout24: 21.270 euro; budget medio di chi cerca 20.000 euro (+11%)."),
 ("y18", [("hook", "Usate più vendute", "La top 3 <em>2025</em>"), ("list", "Classifica", ["1. Fiat Panda", "2. Fiat 500", "3. Lancia Ypsilon"]), ("cta", "Curiosità", "sono anche le più rubate")], "Le auto usate più vendute nel 2025 #shorts", "Secondo l'Osservatorio AutoScout24 le usate più vendute nel 2025 sono Panda, 500 e Ypsilon."),
 ("y19", [("hook", "Prima di partire", "Il controllo da <em>2 minuti</em>"), ("list", "Controlla", ["Luci e stop", "Pressione e crepe gomme", "Rumori dei freni", "Tergicristalli"]), ("cta", "Buon viaggio", "e guida con prudenza")], "Controllo dell'auto prima di partire #shorts", "Quattro controlli rapidi prima di un viaggio: luci, gomme, freni, tergicristalli."),
 ("y20", [("hook", "In 30 secondi", "La settimana <em>in numeri</em>"), ("list", "Dati", ["RC media 422 € (IVASS)", "136.201 furti (LoJack)", "173.364 incidenti (ACI-Istat)", "Usato: 21.270 € medi"]), ("cta", "Fonti", "IVASS, LoJack, ACI-Istat, AutoScout24")], "Auto: i numeri della settimana in 30 secondi #shorts", "Riepilogo: RC auto, furti, incidenti e prezzi dell'usato con le fonti."),
]
DAYS_V = ["2026-11-16", "2026-11-17", "2026-11-18", "2026-11-20", "2026-11-21"]
TT_TIMES = {"wk": ["07:30", "13:00", "19:00", "21:30"], "sat": ["10:00", "13:00", "18:00", "21:30"]}
YT_TIMES = {"wk": ["12:00", "15:00", "18:00", "20:30"], "sat": ["11:00", "15:00", "18:00", "21:00"]}
IG_DAYS = ["2026-11-16", "2026-11-17", "2026-11-18", "2026-11-19", "2026-11-20"]
IG_TIMES = ["06:00", "10:00", "14:00", "18:00", "22:00"]
