# Genera la versione inglese del sito (en/index.html) a partire da index.html.
# Uso, dalla cartella del repository:  python strumenti/genera_en.py
# Se un testo italiano viene modificato in index.html, lo script si ferma e
# indica la frase da aggiornare qui sotto.
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
s = (ROOT / 'index.html').read_text(encoding='utf-8')

def sub(it, en, count=None):
    global s
    n = s.count(it)
    if n == 0:
        sys.exit('Testo non trovato in index.html, aggiorna genera_en.py:\n' + it[:200])
    if count is not None and n != count:
        sys.exit(f'Atteso {count} occorrenze, trovate {n}:\n' + it[:200])
    s = s.replace(it, en)

# ---------- percorsi (la pagina inglese sta in en/) ----------
for a, b in [('href="img/', 'href="../img/'), ('src="img/', 'src="../img/'), ('url(img/', 'url(../img/'),
             ('content="img/', 'content="../img/'), ('href="dati/', 'href="../dati/'), ("fetch('dati/", "fetch('../dati/"),
             ('href="favicon.ico"', 'href="../favicon.ico"')]:
    sub(a, b)

# ---------- testa, menu, apertura ----------
T = [
('<html lang="it">', '<html lang="en">'),
('<title>La produzione discografica in Italia come pratica sociale (1965–1999) · Francesco Brusco</title>',
 '<title>Record production in Italy as social practice (1965–1999) · Francesco Brusco</title>'),
('content="Mappatura, etnografia, modelli sistemici di creatività: la rete sociale di 3410 nodi e 7926 collegamenti dietro 700 album italiani, 1965–1999. Grafi, mappe, dataset."',
 'content="Mapping, ethnography, systemic models of creativity: the social network of 3410 nodes and 7926 edges behind 700 Italian albums, 1965–1999. Graphs, maps, dataset."'),
('<meta property="og:title" content="La produzione discografica in Italia come pratica sociale (1965–1999)">',
 '<meta property="og:title" content="Record production in Italy as social practice (1965–1999)">'),
('content="La rete di studi, musicisti, produttori, tecnici ed etichette dietro 700 album italiani: grafi, mappa animata degli studi di registrazione, dataset aperto."',
 'content="The network of studios, musicians, producers, engineers and labels behind 700 Italian albums: graphs, an animated map of recording studios, open data."'),
('<a class="brand" href="#">La produzione discografica in Italia come pratica sociale</a>',
 '<a class="brand" href="#">Record production in Italy as social practice</a>'),
('<li><a href="#rete">La rete</a></li>', '<li><a href="#rete">Network</a></li>'),
('<li><a href="#protagonisti">Protagonisti</a></li>', '<li><a href="#protagonisti">Key figures</a></li>'),
('<li><a href="#genere">Genere</a></li>', '<li><a href="#genere">Gender</a></li>'),
('<li><a href="#studi">Studi</a></li>', '<li><a href="#studi">Studios</a></li>'),
('<li><a href="#mappa">Mappa</a></li>', '<li><a href="#mappa">Map</a></li>'),
('<li><a href="#citta">Tre città</a></li>', '<li><a href="#citta">Three cities</a></li>'),
('<li><a href="#interviste">Interviste</a></li>', '<li><a href="#interviste">Interviews</a></li>'),
('<li><a href="#esplora">Esplora</a></li>', '<li><a href="#esplora">Explore</a></li>'),
('<li><a href="#dati">Dati</a></li>', '<li><a href="#dati">Data</a></li>'),
('<li><a href="#citare">Citare</a></li>', '<li><a href="#citare">Cite</a></li>'),
('<li><a href="#autore">Autore</a></li>', '<li><a href="#autore">Author</a></li>'),
('<div class="lang"><span aria-current="true" title="Italiano">ITA</span><a href="en/" hreflang="en" lang="en" title="English">ENG</a></div>',
 '<div class="lang"><a href="../" hreflang="it" lang="it" title="Italiano">ITA</a><span aria-current="true" title="English">ENG</span></div>'),
('<h1>La produzione discografica in Italia come pratica sociale <span class="yr">(1965–1999)</span></h1>',
 '<h1>Record production in Italy as social practice <span class="yr">(1965–1999)</span></h1>'),
('<p class="sub">Mappatura, etnografia, modelli sistemici di creatività</p>',
 '<p class="sub">Mapping, ethnography, systemic models of creativity</p>'),
('<br>Università di Salerno, Dipartimento di Scienze del Patrimonio Culturale (Dispac)<br>Dipartimento di Musicologia e Beni Culturali, Università di Pavia</p>',
 '<br>University of Salerno, Department of Cultural Heritage Sciences (Dispac)<br>Department of Musicology and Cultural Heritage, University of Pavia</p>'),
('<span>album analizzati</span>', '<span>albums analysed</span>'),
('<span>elementi (nodi)</span>', '<span>elements (nodes)</span>'),
('<span>collegamenti (edges)</span>', '<span>connections (edges)</span>'),
('<span>anni, dal 1965 al 1999</span>', '<span>years, from 1965 to 1999</span>'),
]

# ---------- la rete ----------
T += [
('<h2>La rete sociale della discografia italiana</h2>', '<h2>The social network of the Italian record industry</h2>'),
('<p class="lede">I venti album più venduti di ogni anno, dal 1965 al 1999, e i loro paratesti sono le fonti primarie per ricostruire la rete sociale della produzione in studio. Ogni credito di copertina diventa un collegamento.</p>',
 '<p class="lede">The twenty best-selling albums of each year, from 1965 to 1999, and their paratexts are the primary sources for reconstructing the social network of studio production. Every sleeve credit becomes a connection.</p>'),
('<p>La rete è multimodale: comprende soggetti individuali (interpreti, musicisti, produttori, arrangiatori, tecnici), soggetti collettivi (gruppi, orchestre, cori), nodi istituzionali (le case discografiche), gli album come progetti che catalizzano le relazioni e gli studi di registrazione, ciascuno dei quali agisce come un <i>focus</i>: un aggregatore di interazioni tra agenti umani e materiali.</p>',
 '<p>The network is multimodal: it includes individuals (performers, musicians, producers, arrangers, engineers), collective subjects (bands, orchestras, choirs), institutional nodes (record companies), albums as projects that catalyse relationships, and recording studios, each of which acts as a <i>focus</i>: an aggregator of interactions between human and material agents.</p>'),
('<p>Elaborate in Gephi, le matrici ricavate dal corpus producono un grafo di 3410 nodi e 7926 collegamenti: denso all’apparenza, ma con una densità bassissima, segno di un alto grado di omofilia. I nodi si condensano per affinità geografica, stilistica e professionale in cluster locali relativamente stretti.</p>',
 '<p>Processed in Gephi, the matrices drawn from the corpus produce a graph of 3410 nodes and 7926 edges: dense in appearance, but with very low density, a sign of a high degree of homophily. Nodes condense by geographical, stylistic and professional affinity into relatively tight local clusters.</p>'),
('aria-label="Statistiche whole-network"', 'aria-label="Whole-network statistics"'),
('<th>Proprietà della rete (Gephi)</th><th class="n">Valore</th>', '<th>Network property (Gephi)</th><th class="n">Value</th>'),
('<tr><td>Ordine (nodi)</td>', '<tr><td>Order (nodes)</td>'),
('<tr><td>Densità</td>', '<tr><td>Density</td>'),
('<tr><td>Diametro</td>', '<tr><td>Diameter</td>'),
('<tr><td>Grado medio</td>', '<tr><td>Average degree</td>'),
('<tr><td>Componenti</td>', '<tr><td>Components</td>'),
('<tr class="hl"><td>Componenti</td>', '<tr class="hl"><td>Components</td>'),
('<tr><td>Modularità</td>', '<tr><td>Modularity</td>'),
('<tr><td>Ordine</td>', '<tr><td>Order</td>'),
('<p class="note">Tabella 1. La componente principale raccoglie 3385 nodi (99,2%) e 7908 archi (99,7%).</p>',
 '<p class="note">Table 1. The giant component contains 3385 nodes (99.2%) and 7908 edges (99.7%).</p>'),
('alt="Grafo della rete sociale della discografia italiana, 1965-1999"', 'alt="Graph of the social network of the Italian record industry, 1965-1999"'),
('<figcaption><b>Figura 1.</b> Grafo della rete sociale della discografia italiana dal 1965 al 1999. Nodi dimensionati per numero di connessioni, layout Yifan Hu.</figcaption>',
 '<figcaption><b>Figure 1.</b> Graph of the social network of the Italian record industry, 1965–1999. Nodes sized by number of connections, Yifan Hu layout.</figcaption>'),
('<h3 class="sub-h">Chi compone la rete</h3>', '<h3 class="sub-h">Who makes up the network</h3>'),
('<p>La suddivisione per categorie mette in luce alcune peculiarità. I tecnici del suono sono di gran lunga la categoria più presente, quasi il doppio di studi e produttori, mentre gli addetti al mastering chiudono la lista. Le 93 case discografiche (2,69%) indicano la natura oligopolistica dell’industria; tra i turnisti, i coristi superano chitarristi e tastieristi.</p>',
 '<p>The breakdown by category reveals some peculiarities. Sound engineers are by far the largest category, almost twice as many as studios and producers, while mastering engineers close the list. The 93 record companies (2.69%) point to the oligopolistic nature of the industry; among session players, backing vocalists outnumber guitarists and keyboard players.</p>'),
('<p class="note">Tabella 2. Numero di nodi per categoria e incidenza percentuale sul totale della rete.</p>',
 '<p class="note">Table 2. Number of nodes per category and percentage of the whole network.</p>'),
('<h3 class="sub-h">Comunità e confini</h3>', '<h3 class="sub-h">Communities and boundaries</h3>'),
('<p>L’algoritmo di modularità individua cinque sottogruppi principali, ciascuno con il suo nucleo in una casa discografica e in uno studio di riferimento. Non sono compartimenti stagni: si permeano a vicenda grazie ai soggetti che agiscono all’intersezione. Il confine più netto separa i campi di RCA e CGD, le due principali etichette del periodo.</p>',
 '<p>The modularity algorithm identifies five main subgroups, each centred on a record company and a reference studio. They are not watertight compartments: they permeate each other through the people who work at their intersections. The sharpest boundary separates the fields of RCA and CGD, the two leading labels of the period.</p>'),
('alt="Sottogruppi evidenziati dall\'algoritmo di modularità"', 'alt="Subgroups identified by the modularity algorithm"'),
('<figcaption><b>Figura 2.</b> I principali sottogruppi evidenziati dall’algoritmo di modularità.</figcaption>',
 '<figcaption><b>Figure 2.</b> The main subgroups identified by the modularity algorithm.</figcaption>'),
('<blockquote>C’erano tutti questi giri quindi si erano formate delle situazioni proprio ritmiche, ognuno aveva la sua ritmica […] questo qui è un suono della Numero Uno, questa è la Ricordi, questo è un suono della RCA.<cite>Ellade Bandini, intervista, 23 maggio 2023</cite></blockquote>',
 '<blockquote>There were all these circles, so actual rhythm sections had formed, each had its own rhythm section […] this one is a Numero Uno sound, this is Ricordi, this is an RCA sound.<cite>Ellade Bandini, interview, 23 May 2023 (translated from Italian)</cite></blockquote>'),
('<h3 class="sub-h">Lo sviluppo nel tempo</h3>', '<h3 class="sub-h">Development over time</h3>'),
('<p>Divisa in quinquenni, la rete si espande dagli anni Settanta e si condensa nel decennio successivo. Il 1980–1984 è il momento di massima cooperazione: grado medio più alto (3,83), diametro (8), modularità e path length minimi. Il 1990–1994 è l’unico periodo in cui la rete forma una sola componente, alla vigilia della definitiva affermazione del digitale.</p>',
 '<p>Divided into five-year periods, the network expands from the 1970s and condenses in the following decade. 1980–1984 is the moment of greatest cooperation: highest average degree (3.83), lowest diameter (8), modularity and path length. 1990–1994 is the only period in which the network forms a single component, on the eve of the definitive rise of digital technology.</p>'),
('alt="Sviluppo diacronico della rete per quinquenni"', 'alt="Diachronic development of the network by five-year periods"'),
('<figcaption><b>Figura 3.</b> Sviluppo diacronico della rete in forma di grafi, per intervalli di cinque anni.</figcaption>',
 '<figcaption><b>Figure 3.</b> Diachronic development of the network as graphs, in five-year intervals.</figcaption>'),
('aria-label="Statistiche per quinquenni"', 'aria-label="Statistics by five-year period"'),
('<p class="note">Tabella 3. Statistiche whole-network per intervalli di cinque anni. Il dato 1965–1969 risente della scarsità di informazioni nelle note di copertina del periodo.</p>',
 '<p class="note">Table 3. Whole-network statistics in five-year intervals. The 1965–1969 figures reflect the scarcity of information in the sleeve notes of the period.</p>'),
]

# ---------- protagonisti ----------
T += [
('<h2>Protagonisti</h2>', '<h2>Key figures</h2>'),
('<p class="lede">La centralità spiega come alcuni soggetti agiscano da intermediari per informazioni, esigenze e influenze, in una continua dialettica tra centro e periferia. Ecco i venti nodi principali per grado, con i relativi indici di centralità.</p>',
 '<p class="lede">Centrality explains how certain actors act as brokers of information, needs and influence, in a constant dialectic between centre and periphery. These are the twenty leading nodes by degree, with their centrality measures.</p>'),
('aria-label="Nodi principali per grado"', 'aria-label="Leading nodes by degree"'),
('<th>#</th><th>Nome</th><th>Categoria</th><th class="n">Grado</th>', '<th>#</th><th>Name</th><th>Category</th><th class="n">Degree</th>'),
('<p class="note">Tabella 4. Nodi principali in ordine di grado, con relativi parametri di centralità calcolati in Gephi. Clicca un nome per aprirne la scheda.</p>',
 '<p class="note">Table 4. Leading nodes by degree, with centrality measures calculated in Gephi. Click a name to open its profile.</p>'),
('alt="Posizionamento nella rete dei venti nodi principali"', 'alt="Position of the twenty leading nodes in the network"'),
('<figcaption><b>Figura 4.</b> Posizionamento nella rete dei nodi della Tabella 4.</figcaption>',
 '<figcaption><b>Figure 4.</b> Position in the network of the nodes listed in Table 4.</figcaption>'),
('<h3 class="sub-h">I più presenti, ruolo per ruolo</h3>', '<h3 class="sub-h">The most frequent names, role by role</h3>'),
('<p>Per ciascuna categoria, i nomi che compaiono nel maggior numero di album del corpus.</p>',
 '<p>For each category, the names that appear on the largest number of albums in the corpus.</p>'),
('<button class="more" id="more-roles">Mostra i primi 25 per ruolo</button>', '<button class="more" id="more-roles">Show top 25 per role</button>'),
('<h3 class="sub-h">Etichette e studi, studi e tecnici</h3>', '<h3 class="sub-h">Labels and studios, studios and engineers</h3>'),
('<p>Nella diade etichette–studi la maggior parte dei nodi intrattiene legami non esclusivi: ogni studio lavora con più etichette e viceversa. Fanno eccezione le quattro maggiori case discografiche. La RCA replica il modello della casa madre americana, con un grande studio di proprietà che attrae nella sua orbita gli altri studi romani; la CGD ingloba piccole realtà private e confina con il Clan Celentano; la Ricordi si sovrappone alla CBS vicino al Mulino di Lucio Battisti; la EMI fa da ponte tra il Mersey e il Po.</p>',
 '<p>In the label–studio dyad most nodes maintain non-exclusive ties: each studio works with several labels and vice versa. The four major record companies are the exception. RCA replicates the model of its American parent company, with a large in-house studio that draws the other Roman studios into its orbit; CGD absorbs small private studios and borders on Clan Celentano; Ricordi overlaps with CBS near Lucio Battisti’s Mulino; EMI bridges the Mersey and the Po.</p>'),
('alt="Diade etichette-studi di registrazione"', 'alt="Label-recording studio dyad"'),
('<figcaption><b>Figura 5.</b> Analisi della diade etichette–studi di registrazione.</figcaption>',
 '<figcaption><b>Figure 5.</b> Analysis of the label–recording studio dyad.</figcaption>'),
('alt="Dettaglio di RCA, CGD, Ricordi, EMI"', 'alt="Detail of RCA, CGD, Ricordi, EMI"'),
('<figcaption><b>Figura 6.</b> Dettaglio delle quattro maggiori case discografiche: RCA, CGD, Ricordi, EMI.</figcaption>',
 '<figcaption><b>Figure 6.</b> Detail of the four major record companies: RCA, CGD, Ricordi, EMI.</figcaption>'),
('alt="Triade studi, tecnici del mix e del mastering"', 'alt="Triad of studios, mixing and mastering engineers"'),
('<figcaption><b>Figura 7.</b> Triade composta da studi, tecnici del mix e del mastering.</figcaption>',
 '<figcaption><b>Figure 7.</b> Triad of studios, mixing engineers and mastering engineers.</figcaption>'),
('<p>La triade studi–tecnici del suono–mastering rende visibile la divisione professionale tra i fonici residenti, il cui nodo è spesso tangente o sovrapposto a quello dello studio, e i freelance. Il mastering si emancipa dall’idea di semplice trasferimento tecnico solo alla fine degli anni Settanta, sul modello anglosassone.</p>',
 '<p>The studio–sound engineer–mastering triad makes visible the professional divide between in-house engineers, whose node often touches or overlaps that of the studio, and freelancers. Mastering moves beyond the idea of a mere technical transfer only at the end of the 1970s, following the Anglo-American model.</p>'),
('<blockquote>Ho deciso in quel momento preciso di diventare un freelance per trovare nuovi stimoli, nuove cose, nuove apparecchiature da usare.<cite>Piero Bravin, intervista, 25 settembre 2023</cite></blockquote>',
 '<blockquote>At that precise moment I decided to go freelance, to find new stimuli, new things, new equipment to use.<cite>Piero Bravin, interview, 25 September 2023 (translated from Italian)</cite></blockquote>'),
('<h3 class="sub-h">Tre ego-net</h3>', '<h3 class="sub-h">Three ego-nets</h3>'),
('<p>Mina, Paolo Gianolio e Renato Cantele: tre ruoli professionali, tre forme di rete personale. Il chitarrista resta al centro di un ego-net omogeneo; quello di Mina, prima per grado tra gli interpreti, si chiude in un circuito di fiducia serrato di soli 200 nodi. Le visualizzazioni ego-net sono state anche il punto di partenza di gran parte delle interviste: gli interlocutori vi si sono “riconosciuti”.</p>',
 '<p>Mina, Paolo Gianolio and Renato Cantele: three professional roles, three forms of personal network. The guitarist sits at the centre of a homogeneous ego-net; Mina’s, the highest-degree performer, closes into a tight circle of trust of only 200 nodes. The ego-net visualisations were also the starting point for most of the interviews: the interviewees “recognised” themselves in them.</p>'),
('alt="Ego-net di Mina"', 'alt="Ego-net of Mina"'),
('<figcaption><b>Figura 8.</b> Ego-net di Mina: 200 nodi (5,77% del totale).</figcaption>', '<figcaption><b>Figure 8.</b> Ego-net of Mina: 200 nodes (5.77% of the total).</figcaption>'),
('alt="Ego-net di Paolo Gianolio"', 'alt="Ego-net of Paolo Gianolio"'),
('<figcaption><b>Figura 9.</b> Ego-net di Paolo Gianolio: 448 nodi (12,92%).</figcaption>', '<figcaption><b>Figure 9.</b> Ego-net of Paolo Gianolio: 448 nodes (12.92%).</figcaption>'),
('alt="Ego-net di Renato Cantele"', 'alt="Ego-net of Renato Cantele"'),
('<figcaption><b>Figura 10.</b> Ego-net di Renato Cantele: 274 nodi (7,9%).</figcaption>', '<figcaption><b>Figure 10.</b> Ego-net of Renato Cantele: 274 nodes (7.9%).</figcaption>'),
('<blockquote>Lei o ti ama oppure ti esclude, ma in maniera… educata.<cite>Massimo Moriconi, intervista, 23 ottobre 2023</cite></blockquote>',
 '<blockquote>She either loves you or shuts you out, but in a… polite way.<cite>Massimo Moriconi, interview, 23 October 2023 (translated from Italian)</cite></blockquote>'),
]

# ---------- genere ----------
T += [
('<h2>Una storia al maschile?</h2>', '<h2>A man’s story?</h2>'),
('<p>Con il 7,8% di presenze femminili, la discografia italiana del periodo conferma un forte squilibrio di genere, senza segni di evoluzione. Le professioniste si concentrano nel canto, il ruolo “frontale” per eccellenza, e la loro presenza crolla nei mestieri tecnico-produttivi: 2,3% tra i produttori, zero nel mastering.</p>',
 '<p>With women making up 7.8% of the network, the Italian record industry of the period shows a marked gender imbalance, with no sign of change. Women professionals are concentrated in singing, the “front-facing” role par excellence, and their presence collapses in technical and production jobs: 2.3% of producers, none in mastering.</p>'),
('<blockquote>Era palese che il mio parere valesse meno di quello dei colleghi. Malgrado la mia esperienza.<cite>Marti Jane Robertson, intervista, 20 novembre 2023</cite></blockquote>',
 '<blockquote>It was obvious that my opinion counted for less than my colleagues’. Despite my experience.<cite>Marti Jane Robertson, interview, 20 November 2023 (translated from Italian)</cite></blockquote>'),
('<p class="note">Tabella 5. Professioniste per categoria, 1965–1999 (192 su 2460 nodi non-album, 7,8%).</p>',
 '<p class="note">Table 5. Women professionals by category, 1965–1999 (192 of 2460 non-album nodes, 7.8%).</p>'),
]

# ---------- studi ----------
T += [
('<h2>Gli studi di registrazione in Italia</h2>', '<h2>Recording studios in Italy</h2>'),
('<p class="lede">Lo studio di registrazione è il <i>focus</i> della rete: uno spazio fisico che aggrega persone, tecnologie, convenzioni e gusti. Il loro numero cresce lungo tutto il periodo, con i tassi più alti nei primi tre quinquenni.</p>',
 '<p class="lede">The recording studio is the <i>focus</i> of the network: a physical space that brings together people, technologies, conventions and tastes. Their number grows throughout the period, with the highest rates in the first three five-year periods.</p>'),
('<p>Nel 1965–1969 solo il 31% dei dischi indica lo studio, e se ne contano nove: la RCA a Roma, il resto a Milano. Negli anni Settanta il sistema resta bipolare, ma si aprono piccoli poli a Genova e Venezia e i primi studi residenziali extraurbani, come lo Stone Castle di Carimate e il Mulino di Battisti. Nel 1980–1984 Carimate sottrae per la prima volta il primato alla RCA, mentre lungo la via Emilia nasce il terzo polo, quello di Bologna e Modena. Gli anni Novanta portano la frammentazione e il passaggio di testimone tra analogico e digitale.</p>',
 '<p>In 1965–1969 only 31% of records name the studio, and there are nine of them: RCA in Rome, the rest in Milan. In the 1970s the system remains bipolar, but small hubs open in Genoa and Venice, along with the first residential studios outside the cities, such as Stone Castle in Carimate and Battisti’s Mulino. In 1980–1984 Carimate takes the lead from RCA for the first time, while a third hub, Bologna and Modena, emerges along the Via Emilia. The 1990s bring fragmentation and the handover from analogue to digital.</p>'),
('<p class="note">Tabella 6. Studi censiti per quinquennio, compresi quelli all’estero; tra parentesi l’incremento rispetto al periodo precedente.</p>',
 '<p class="note">Table 6. Studios recorded per five-year period, including those abroad, with the increase over the previous period.</p>'),
('<h3 class="sub-h">Gli studi più ricorrenti</h3>', '<h3 class="sub-h">The most frequent studios</h3>'),
('<p>Gli studi italiani in cui è stato realizzato il maggior numero di album del corpus. I primi quattordici, con almeno dieci album, sono evidenziati: tre poli dominano, con la RCA in testa nel lungo periodo e il Fonoprint secondo nonostante l’ingresso tardivo.</p>',
 '<p>The Italian studios where the largest number of albums in the corpus were made. The top fourteen, with at least ten albums each, are highlighted: three hubs dominate, with RCA leading over the long term and Fonoprint second despite its late arrival.</p>'),
('aria-label="Studi di registrazione per numero di album"', 'aria-label="Recording studios by number of albums"'),
('<th>Studio</th><th>Località</th><th class="n">Album</th><th class="n">Attività nel corpus</th>', '<th>Studio</th><th>Location</th><th class="n">Albums</th><th class="n">Active in corpus</th>'),
('<p class="note">Tabella 7. Studi di registrazione italiani per numero di album del corpus; evidenziati quelli con almeno dieci album.</p>',
 '<p class="note">Table 7. Italian recording studios by number of albums in the corpus; those with at least ten albums are highlighted.</p>'),
('<button class="more" id="more-studi">Mostra tutti gli studi geolocalizzati</button>', '<button class="more" id="more-studi">Show all geolocated studios</button>'),
]

# ---------- mappa ----------
T += [
('<h2>La mappa degli studi, anno per anno</h2>', '<h2>The studio map, year by year</h2>'),
('<p class="lede">Fai scorrere la linea del tempo, o premi play: gli studi compaiono nell’anno del loro primo album nel corpus, crescono con il numero di dischi e si spostano quando cambiano sede.</p>',
 '<p class="lede">Drag the timeline, or press play: studios appear in the year of their first album in the corpus, grow with the number of records and move when they relocate.</p>'),
('aria-label="Mappa animata degli studi di registrazione italiani, 1965-1999"', 'aria-label="Animated map of Italian recording studios, 1965-1999"'),
('<h4>Nuovi studi</h4>', '<h4>New studios</h4>'),
('<h4>Trasferimenti</h4>', '<h4>Relocations</h4>'),
('<h4>I più attivi nell’anno</h4>', '<h4>Most active this year</h4>'),
('aria-label="Avvia la linea del tempo"', 'aria-label="Play the timeline"'),
('aria-label="Anno"', 'aria-label="Year"'),
('<button data-v="italia" class="on">Italia</button><button data-v="milano">Milano e Brianza</button><button data-v="roma">Roma</button><button data-v="emilia">Bologna e Modena</button>',
 '<button data-v="italia" class="on">Italy</button><button data-v="milano">Milan &amp; Brianza</button><button data-v="roma">Rome</button><button data-v="emilia">Bologna &amp; Modena</button>'),
('<label><input type="checkbox" id="m-cum" checked> mostra anche gli studi non più attivi</label>', '<label><input type="checkbox" id="m-cum" checked> also show studios no longer active</label>'),
('119 studi geolocalizzati. Colore pieno: attivo nell’anno o nei quattro precedenti. Le sedi seguono la mappatura per quinquenni; la linea tratteggiata indica un trasferimento. Gli studi esteri non sono in mappa.',
 '119 geolocated studios. Solid colour: active in the year or in the previous four. Locations follow the five-year mapping; the dashed line marks a relocation. Studios abroad are not shown.'),
('>Apri la mappa su Google My Maps</a>', '>Open the map in Google My Maps</a>'),
]

# ---------- tre città ----------
T += [
('<h2>Milano, Roma, Bologna</h2>', '<h2>Milan, Rome, Bologna</h2>'),
('<p class="lede">Le tre reti cittadine non sono separate: buona parte dei nodi è presente in tutti e tre i mondi musicali. Milano e Bologna incrociano di più i loro collegamenti, Roma resta in posizione eccentrica.</p>',
 '<p class="lede">The three city networks are not separate: many nodes appear in all three music worlds. Milan and Bologna share more connections, while Rome remains off-centre.</p>'),
('<p>I tre network hanno lo stesso diametro (8), più basso di quello nazionale, a conferma delle loro radici locali. Bologna, per tutto il periodo, è una sola componente: i nodi più centrali fanno da ponte e tengono insieme l’intera rete.</p>',
 '<p>The three networks have the same diameter (8), lower than the national one, confirming their local roots. Throughout the period Bologna forms a single component: the most central nodes act as bridges and hold the whole network together.</p>'),
('alt="Grafo dei tre poli discografici Milano Roma Bologna"', 'alt="Graph of the three recording hubs Milan Rome Bologna"'),
('<figcaption><b>Figura 11.</b> La rete nazionale dei tre poli principali, con gli studi di registrazione come sorgenti delle connessioni. Blu Milano, arancio Roma, rosso Bologna.</figcaption>',
 '<figcaption><b>Figure 11.</b> The national network of the three main hubs, with recording studios as the sources of connections. Blue Milan, orange Rome, red Bologna.</figcaption>'),
('aria-label="Proprietà delle tre reti locali"', 'aria-label="Properties of the three local networks"'),
('<th class="n">Milano</th><th class="n">Roma</th><th class="n">Bologna</th><th class="n">Italia</th>', '<th class="n">Milan</th><th class="n">Rome</th><th class="n">Bologna</th><th class="n">Italy</th>'),
('<p class="note">Tabella 8. Proprietà dei tre music world locali e confronto con il dato nazionale.</p>',
 '<p class="note">Table 8. Properties of the three local music worlds compared with the national network.</p>'),
('<p class="note">Tabella 9. Ordine (numero di nodi) delle tre reti per quinquennio. Bologna entra in campo solo negli anni Ottanta e nel 1995–1999 raggiunge quasi Milano.</p>',
 '<p class="note">Table 9. Order (number of nodes) of the three networks per five-year period. Bologna only enters the field in the 1980s and by 1995–1999 almost matches Milan.</p>'),
('alt="Grafi dei social network di Milano, Roma e Bologna"', 'alt="Social network graphs of Milan, Rome and Bologna"'),
('<figcaption><b>Figura 12.</b> Grafi dei social network di Milano (a), Roma (b) e Bologna (c).</figcaption>',
 '<figcaption><b>Figure 12.</b> Social network graphs of Milan (a), Rome (b) and Bologna (c).</figcaption>'),
('<h3>Milano</h3>', '<h3>Milan</h3>'),
('<p>La città della musica per eccellenza vede le sale d’incisione fiorire in ogni angolo: Fonorama e Ricordi a sud, la Basilica della EMI in piazza Sant’Eufemia, poi il polo di via Quintiliano vicino a Linate (CGD, Idea Recording, Morning, Logic) e gli studi residenziali in Brianza.</p>',
 '<p>Italy’s music city par excellence sees recording rooms flourish in every corner: Fonorama and Ricordi to the south, EMI’s Basilica in Piazza Sant’Eufemia, then the Via Quintiliano hub near Linate airport (CGD, Idea Recording, Morning, Logic) and the residential studios in Brianza.</p>'),
('alt="Mappatura degli studi milanesi da Gephi"', 'alt="Map of Milan studios from Gephi"'),
('<figcaption><b>Figura 13.</b> Gli studi milanesi, da Gephi.</figcaption>', '<figcaption><b>Figure 13.</b> Milan studios, from Gephi.</figcaption>'),
('<h3>Roma</h3>', '<h3>Rome</h3>'),
('<p>La Capitale è dominata dal grande centro della RCA, aperto alla fine del 1961 al km 12 della Tiburtina. Attorno nascono studi attratti dal suo indotto e da quello di RAI e Cinecittà: Ortophonic, Sonic, Studio 38, il Quattro Uno, il Forum Music Village.</p>',
 '<p>The capital is dominated by RCA’s large complex, opened at the end of 1961 at km 12 of the Via Tiburtina. Around it, studios spring up drawn by its business and by that of RAI and Cinecittà: Ortophonic, Sonic, Studio 38, Quattro Uno, Forum Music Village.</p>'),
('alt="Mappatura degli studi romani da Gephi"', 'alt="Map of Rome studios from Gephi"'),
('<figcaption><b>Figura 14.</b> Gli studi romani, da Gephi.</figcaption>', '<figcaption><b>Figure 14.</b> Rome studios, from Gephi.</figcaption>'),
('<p>Dalla fine degli anni Settanta l’Emilia sviluppa una propria rete, grazie al calo dei costi della tecnologia, a un mercato immobiliare favorevole e al milieu di DAMS, radio libere e Movimento del ’77. Fonoprint ne è il centro, con Modena e Reggio Emilia lungo la via Emilia.</p>',
 '<p>From the late 1970s Emilia develops its own network, thanks to falling technology costs, a favourable property market and the milieu of the DAMS, free radio and the 1977 movement. Fonoprint is its centre, with Modena and Reggio Emilia along the Via Emilia.</p>'),
('alt="Mappatura degli studi bolognesi da Gephi"', 'alt="Map of Bologna studios from Gephi"'),
('<figcaption><b>Figura 15.</b> Gli studi emiliani, da Gephi.</figcaption>', '<figcaption><b>Figure 15.</b> Emilian studios, from Gephi.</figcaption>'),
]

# ---------- interviste, esplora, dati, citare, autore ----------
T += [
('<h2>Interviste</h2>', '<h2>Interviews</h2>'),
('<p class="lede">Le persone intervistate per la ricerca, tra il 2019 e il 2025.</p>', '<p class="lede">The people interviewed for the research, between 2019 and 2025.</p>'),
('aria-label="Elenco degli intervistati"', 'aria-label="List of interviewees"'),
('<th>#</th><th>Nome</th><th>Ruolo</th><th class="n">Data</th>', '<th>#</th><th>Name</th><th>Role</th><th class="n">Date</th>'),
('<p class="note">Tabella 10. Indice degli intervistati.</p>', '<p class="note">Table 10. Index of interviewees.</p>'),
('<span class="kicker">Esplora il dataset</span>', '<span class="kicker">Explore the dataset</span>'),
('<h2>Cerca un nome, uno studio o un album</h2>', '<h2>Search for a name, a studio or an album</h2>'),
('<p class="lede">Ogni scheda mostra i dischi a cui una persona o uno studio hanno lavorato e con chi hanno collaborato più spesso; per ogni album, la squadra completa accreditata.</p>',
 '<p class="lede">Each profile shows the records a person or studio worked on and who they collaborated with most often; for each album, the full credited team.</p>'),
('placeholder="Es. Fonoprint, Celso Valli, Anime salve…"', 'placeholder="e.g. Fonoprint, Celso Valli, Anime salve…"'),
('aria-label="Cerca nel dataset"', 'aria-label="Search the dataset"'),
('<p class="try">Prova:', '<p class="try">Try:'),
('<span class="kicker">Dati aperti</span>', '<span class="kicker">Open data</span>'),
('<h2>Scarica il dataset</h2>', '<h2>Download the dataset</h2>'),
('<p class="lede">I file sono pronti per Gephi, Palladio, R o Python. Nodi e relazioni si collegano tramite l’identificativo numerico (<code>Id</code> → <code>Source</code>/<code>Target</code>).</p>',
 '<p class="lede">The files are ready for Gephi, Palladio, R or Python. Nodes and edges are linked by their numeric identifier (<code>Id</code> → <code>Source</code>/<code>Target</code>). File contents are in Italian.</p>'),
('<h3>Nodi</h3><p>Persone, studi, etichette e album, con il ruolo principale.</p>', '<h3>Nodes</h3><p>People, studios, labels and albums, with their main role.</p>'),
('<h3>Relazioni</h3><p>Un credito per riga: anno, chi (Source), su quale album (Target).</p>', '<h3>Edges</h3><p>One credit per row: year, who (Source), on which album (Target).</p>'),
('<h3>Discografia</h3><p>Il corpus degli album con anno, interprete, etichetta, numero di catalogo e crediti.</p>', '<h3>Discography</h3><p>The album corpus with year, performer, label, catalogue number and credits.</p>'),
('<h3>Indice dei nomi</h3><p>I nomi ordinati per ruolo e per numero di presenze.</p>', '<h3>Index of names</h3><p>Names sorted by role and number of appearances.</p>'),
('<h3>Studi geolocalizzati 1965–1999</h3><p>119 studi con indirizzo, anni di attività, numero di album e coordinate per quinquennio.</p>',
 '<h3>Geolocated studios 1965–1999</h3><p>119 studios with address, years of activity, number of albums and coordinates per five-year period.</p>'),
('<h3>Rete in JSON</h3><p>La versione compatta usata da questo sito: album, anno e crediti.</p>', '<h3>Network in JSON</h3><p>The compact version used by this site: album, year and credits.</p>'),
('<span class="kicker">Metodo e fonti</span>', '<span class="kicker">Method and sources</span>'),
('<h2>Come è costruito</h2>', '<h2>How it was built</h2>'),
('<p>Il corpus raccoglie i venti album italiani più venduti di ogni anno tra il 1965 e il 1999, ricavati da FIMI, <i>Musica e dischi</i> e Hit Parade Italia. Per ciascun album sono stati trascritti i crediti di copertine e libretti, integrati con fonti d’archivio e con le interviste ai protagonisti.</p>',
 '<p>The corpus gathers the twenty best-selling Italian albums of each year between 1965 and 1999, drawn from FIMI, <i>Musica e dischi</i> and Hit Parade Italia. For each album the credits on sleeves and booklets were transcribed and supplemented with archival sources and interviews with the people involved.</p>'),
('<p>Ogni credito diventa una relazione non orientata tra una persona (o uno studio, o un’etichetta) e un album. La rete è stata analizzata con la social network analysis in Gephi e con la mappatura geostorica. Il dataset si fonda sulle classifiche ufficiali: la circolazione informale resta, per scelta, fuori dal perimetro.</p>',
 '<p>Each credit becomes an undirected edge between a person (or a studio, or a label) and an album. The network was analysed with social network analysis in Gephi and with geo-historical mapping. The dataset is based on official charts: informal circulation is deliberately left out of scope.</p>'),
('<span class="kicker">Citare</span>', '<span class="kicker">Cite</span>'),
('<h2>Come citare</h2>', '<h2>How to cite</h2>'),
('<p>Se usi i dati o le visualizzazioni, cita la tesi:</p>', '<p>If you use the data or the visualisations, please cite the thesis:</p>'),
(', tesi di dottorato, Dipartimento di Musicologia e Beni Culturali, Università di Pavia, a.a. 2024-2025.<button type="button" id="copycite">Copia</button>',
 ', PhD thesis, Department of Musicology and Cultural Heritage, University of Pavia, academic year 2024-2025.<button type="button" id="copycite">Copy</button>'),
('<p style="margin-top:28px">Per correzioni, integrazioni o collaborazioni scrivi tramite <a',
 '<p style="margin-top:28px">For corrections, additions or collaborations, get in touch via <a'),
('alt="Francesco Brusco legge durante un incontro pubblico"', 'alt="Francesco Brusco reading at a public event"'),
('<span class="kicker">L’autore</span>', '<span class="kicker">The author</span>'),
('<p>Docente di Musiche Popolari Contemporanee presso l’Università di Salerno. Ha conseguito il dottorato in Scienze del Testo Letterario e Musicale all’Università di Pavia, svolgendo un periodo di ricerca presso l’Institute of Popular Music dell’Università di Liverpool. Giornalista per <i>Il Manifesto</i> e <i>il Giornale della Musica</i>, è autore di monografie dedicate principalmente ai Beatles e alla canzone d’autore italiana (l’ultimo libro si intitola <i>Un altro libro sui Beatles. Eredità culturali tra Penny Lane e il metaverso</i>). Come musicista ha all’attivo due album con i Là Nua.</p>',
 '<p>Lecturer in Contemporary Popular Music at the University of Salerno. He holds a PhD in Literary and Musical Text Studies from the University of Pavia, including a research period at the Institute of Popular Music, University of Liverpool. A journalist for <i>Il Manifesto</i> and <i>il Giornale della Musica</i>, he is the author of monographs devoted mainly to the Beatles and to the Italian singer-songwriter tradition (his latest book is <i>Un altro libro sui Beatles. Eredità culturali tra Penny Lane e il metaverso</i>). As a musician he has released two albums with Là Nua.</p>'),
('<span>© 2026 Francesco Brusco · La produzione discografica in Italia come pratica sociale (1965–1999)</span>',
 '<span>© 2026 Francesco Brusco · Record production in Italy as social practice (1965–1999)</span>'),
('>Codice e dati su GitHub</a>', '>Code and data on GitHub</a>'),
('aria-label="Immagine ingrandita"', 'aria-label="Enlarged image"'),
]

# ---------- script ----------
T += [
("[['album',700,'20,18'],['mixer',414,'11,95'],['cori',265,'7,65'],['chitarre',264,'7,62'],['tastiere',261,'7,54'],['produttore',217,'6,27'],['studio',210,'6,06'],['batteria-percussioni',203,'5,86'],['performer',201,'5,80'],['arrangiatore',183,'5,28'],['basso-contrabbasso',164,'4,74'],['fiati',143,'4,22'],['etichetta',93,'2,69'],['archi',87,'2,48'],['mastering',57,'1,65']]",
 "[['albums',700,'20.18'],['sound engineers',414,'11.95'],['backing vocals',265,'7.65'],['guitars',264,'7.62'],['keyboards',261,'7.54'],['producers',217,'6.27'],['studios',210,'6.06'],['drums & percussion',203,'5.86'],['performers',201,'5.80'],['arrangers',183,'5.28'],['bass & double bass',164,'4.74'],['winds',143,'4.22'],['labels',93,'2.69'],['strings',87,'2.48'],['mastering',57,'1.65']]"),
("[['cori',44.52,'118/265'],['performer',19.90,'40/201'],['archi',9.19,'8/87'],['fiati',4.19,'6/143'],['produttore',2.30,'5/217'],['batteria-percussioni',1.47,'3/203'],['mixer',1.20,'5/414'],['tastiere',1.14,'3/261'],['chitarre',.75,'2/264'],['basso-contrabbasso',.60,'1/164'],['arrangiatore',.54,'1/183'],['mastering',0,'0/58']],50,function(d){return d[1].toFixed(1).replace('.',',')+'%'}",
 "[['backing vocals',44.52,'118/265'],['performers',19.90,'40/201'],['strings',9.19,'8/87'],['winds',4.19,'6/143'],['producers',2.30,'5/217'],['drums & percussion',1.47,'3/203'],['sound engineers',1.20,'5/414'],['keyboards',1.14,'3/261'],['guitars',.75,'2/264'],['bass & double bass',.60,'1/164'],['arrangers',.54,'1/183'],['mastering',0,'0/58']],50,function(d){return d[1].toFixed(1)+'%'}"),
("S=[['Milano','#3c6fd8',", "S=[['Milan','#3c6fd8',"),
("['Roma','#f08a3c',", "['Rome','#f08a3c',"),
("var ROLE={performer:'Interprete',etichetta:'Etichetta',studio:'Studio di registrazione',produttore:'Produttore',arrangiatore:'Arrangiatore',mixer:'Tecnico del suono',master:'Mastering','batteria-percussioni':'Batteria e percussioni','basso-contrabbasso':'Basso e contrabbasso',chitarre:'Chitarre',tastiere:'Tastiere',archi:'Archi',fiati:'Fiati',cori:'Cori',album:'Album'};",
 "var ROLE={performer:'Performer',etichetta:'Label',studio:'Recording studio',produttore:'Producer',arrangiatore:'Arranger',mixer:'Sound engineer',master:'Mastering','batteria-percussioni':'Drums & percussion','basso-contrabbasso':'Bass & double bass',chitarre:'Guitars',tastiere:'Keyboards',archi:'Strings',fiati:'Winds',cori:'Backing vocals',album:'Album'};"),
("this.textContent=on?'Mostra i primi 25 per ruolo':'Mostra solo i primi 10'", "this.textContent=on?'Show top 25 per role':'Show top 10 only'"),
("textContent='Altri '+s.esteri.length+' studi del corpus non sono geolocalizzati, in gran parte esteri: da Abbey Road, Air e Trident a Londra fino al Record Plant di Los Angeles, a Musicland a Monaco e al Château d’Hérouville in Francia.'",
 "textContent='Another '+s.esteri.length+' studios in the corpus are not geolocated, most of them abroad: from Abbey Road, Air and Trident in London to the Record Plant in Los Angeles, Musicland in Munich and the Château d’Hérouville in France.'"),
("this.textContent=studiAll?'Mostra solo i primi 30':'Mostra tutti gli studi geolocalizzati'", "this.textContent=studiAll?'Show top 30 only':'Show all geolocated studios'"),
("'<p style=\"padding:24px;color:#333\">Mappa non disponibile.</p>'", "'<p style=\"padding:24px;color:#333\">Map not available.</p>'"),
("'<b>'+nAct+'</b> studi attivi (ultimi 5 anni)<br><b>'+nTot+'</b> comparsi dal 1965'", "'<b>'+nAct+'</b> active studios (last 5 years)<br><b>'+nTot+'</b> appeared since 1965'"),
("' <small>'+t[1]+' album</small></li>'", "' <small>'+t[1]+(t[1]===1?' album':' albums')+'</small></li>'"),
("'<li><small>nessuno studio indicato in copertina</small></li>'", "'<li><small>no studio credited on sleeves</small></li>'"),
("setAttribute('aria-label','Metti in pausa')", "setAttribute('aria-label','Pause')"),
("setAttribute('aria-label','Avvia la linea del tempo')", "setAttribute('aria-label','Play the timeline')"),
("tot+' album nel corpus · sede nel '+year+': '", "tot+' albums in the corpus · location in '+year+': '"),
('title="Album per anno, 1965–1999"', 'title="Albums per year, 1965–1999"'),
("'<a href=\"#n='+s.id+'\">Apri la scheda →</a>'", "'<a href=\"#n='+s.id+'\">Open profile →</a>'"),
("'<div class=\"empty\" style=\"padding:12px 18px\">Nessun risultato</div>'", "'<div class=\"empty\" style=\"padding:12px 18px\">No results</div>'"),
("al_.length+' album nel corpus · '", "al_.length+(al_.length===1?' album':' albums')+' in the corpus · '"),
('<h4>Collaboratori più frequenti</h4>', '<h4>Most frequent collaborators</h4>'),
("a.c.length+' crediti</div>", "a.c.length+' credits</div>"),
("sub:ROLE[N[k][1]]+' · '+byNode[k].length+' album'", "sub:ROLE[N[k][1]]+' · '+byNode[k].length+(byNode[k].length===1?' album':' albums')"),
(".replace(/Copia$/,'')", ".replace(/Copy$/,'')"),
("b.textContent='Copiato';setTimeout(function(){b.textContent='Copia'}", "b.textContent='Copied';setTimeout(function(){b.textContent='Copy'}"),
]

for it, en in T:
    sub(it, en)

# Tabella 4: categorie e decimali
CAT = {'etichetta': 'label', 'batterista': 'drummer', 'chitarrista': 'guitarist', 'bassista': 'bassist',
       'tastierista': 'keyboardist', 'corista': 'backing vocalist'}
m = re.search(r"function centr\(\)\{var T=\[.*?\];", s, re.S)
blk = m.group(0)
for a, b in CAT.items():
    blk = blk.replace(f",'{a}',", f",'{b}',")
blk = re.sub(r"'(\d+),(\d+)'", r"'\1.\2'", blk)
s = s[:m.start()] + blk + s[m.end():]

# decimali nelle tabelle: 0,001 -> 0.001
s = re.sub(r'(<td class="n">\d+),(\d+)</td>', r'\1.\2</td>', s)

# Tabella 10: ruoli e date degli intervistati
ROLES = [('tecnico del mastering', 'mastering engineer'), ('tecnico del suono', 'sound engineer'),
         ('assistente di studio', 'studio assistant'), ('studio manager', 'studio manager'),
         ('pluristrumentista', 'multi-instrumentalist'), ('contrabbassista', 'double bassist'),
         ('cantautore', 'singer-songwriter'), ('batterista', 'drummer'), ('tastierista', 'keyboardist'),
         ('chitarrista', 'guitarist'), ('cantante', 'singer'), ('autore', 'songwriter'), ('bassista', 'bassist'),
         ('produttore', 'producer'), ('corista', 'backing vocalist'), ('arrangiatore', 'arranger'),
         ('violinista', 'violinist'), ('sassofonista', 'saxophonist'), ('percussionista', 'percussionist'),
         ('flautista', 'flautist'), ('pianista', 'pianist')]
MESI = dict(gennaio='January', febbraio='February', marzo='March', aprile='April', maggio='May', giugno='June',
            luglio='July', agosto='August', settembre='September', ottobre='October', novembre='November', dicembre='December')
a = s.index('aria-label="List of interviewees"'); b = s.index('</table>', a)
tab = s[a:b]
def fix_row(m):
    role = m.group(2)
    for it, en in ROLES:
        role = re.sub(r'\b' + it + r'\b', en, role)
    date = m.group(3)
    for it, en in MESI.items():
        date = date.replace(' ' + it + ' ', ' ' + en + ' ')
    return m.group(1) + role + '</td><td class="n">' + date + '</td></tr>'
tab = re.sub(r'(<tr><td class="n" style="text-align:left">\d+</td><td>[^<]*</td><td>)([^<]*)</td><td class="n">(.*?)</td></tr>', fix_row, tab)
tab = tab.replace('Juan Carlos detto Flaco', 'Juan Carlos, known as Flaco')
s = s[:a] + tab + s[b:]

# controllo finale: nessun mese o ruolo italiano residuo nella tabella interviste
left = [w for w in list(MESI) + [r[0] for r in ROLES if r[0] != r[1]] if re.search(r'\b' + w + r'\b', tab)]
if left:
    sys.exit('Traduzioni mancanti nella tabella interviste: ' + ', '.join(left))

out = ROOT / 'en' / 'index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(s, encoding='utf-8')
print('Scritto', out.relative_to(ROOT))
