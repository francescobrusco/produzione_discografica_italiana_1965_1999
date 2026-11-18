# Produzione discografica italiana 1965–1999

Dataset e sito di esplorazione delle reti di produzione dietro i venti album italiani più venduti di ogni anno, dal 1965 al 1999: interpreti, studi di registrazione, produttori, arrangiatori, tecnici del suono, turnisti ed etichette.

**Sito:** https://francescobrusco.github.io/produzione_discografica_italiana_1965_1999/

Ricerca di dottorato di **Francesco Brusco** (Scienze del testo letterario e musicale, Università di Pavia).

## Dati

| File | Contenuto |
|---|---|
| `dati/nodi_1965-1999.csv` | Nodi: persone, studi, etichette e album (`Id`, `Label`, `nome`, `ruolo`) |
| `dati/relazioni_1965-1999.csv` | Relazioni: un credito per riga (`Anno`, `Source`, `Target`) |
| `dati/discografia_1965-1999.xlsx` | Corpus degli album con catalogo e crediti |
| `dati/indice_nomi.xlsx` | Indice dei nomi per ruolo e frequenza |
| `dati/studi_geolocalizzati_1965-1969.csv` | Studi con indirizzo e coordinate |
| `dati/rete.json` | Versione compatta usata dal sito |

Nodi e relazioni si collegano tramite `Id` → `Source`/`Target` e si possono importare direttamente in Gephi o Palladio.

## Fonti e metodo

Classifiche FIMI, *Musica e dischi* e Hit Parade Italia per la selezione del corpus; crediti da copertine e libretti, fonti d'archivio e interviste per la ricostruzione delle reti. Analisi con social network analysis (Gephi) e mappatura geostorica.

## Come citare

Brusco, Francesco. *Produzione discografica italiana 1965–1999: dataset delle reti di produzione*. 2026. https://francescobrusco.github.io/produzione_discografica_italiana_1965_1999/

## Sito

Il sito è un'unica pagina statica (`index.html`) pubblicata con GitHub Pages dal ramo `main`. Per aggiornare i dati, sostituisci i CSV in `dati/` e rigenera `dati/rete.json`.
