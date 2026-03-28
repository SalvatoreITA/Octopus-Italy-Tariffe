# 🐙 Octopus Tariffe - Home Assistant Custom Component

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![version](https://img.shields.io/badge/version-v1.0.0-blue.svg)]()
[![maintainer](https://img.shields.io/badge/maintainer-Salvatore_Lentini_--_DomHouse.it-green.svg)](https://www.domhouse.it)

Un'integrazione personalizzata, ultra-stabile e invisibile per Home Assistant che estrae in tempo reale i **costi fissi di commercializzazione (PCV/QVD)** e i **prezzi della materia prima** dal sito ufficiale di [Octopus Energy Italia](https://octopusenergy.it/le-nostre-tariffe).

*(Inserisci qui uno screenshot della schermata dei tuoi 9 sensori su Home Assistant)*

---

## 🌟 Perché nasce questa integrazione?

Mentre esistono già ottime integrazioni per leggere i dati del *proprio* contratto, spesso è difficile avere a disposizione sulla dashboard i **prezzi attuali pubblici** per poter fare un confronto e capire se conviene cambiare tariffa.

Questa integrazione risolve il problema alla radice con un approccio da veri "Pro":
* **Motore JSON Infallibile:** Non usa fragili Regex sull'HTML, ma legge direttamente il database nascosto (Next.js JSON) del sito Octopus. Se cambiano la grafica del sito, l'integrazione continua a funzionare perfettamente!
* **Zero YAML:** Si configura tutto dall'interfaccia grafica di Home Assistant in 2 clic.
* **Super Leggera:** Fa una singola richiesta al sito ogni 12 ore, popolando istantaneamente 9 sensori. Zero stress per il tuo server e per quelli di Octopus.
* **Perfetta per le Automazioni:** I sensori creati sono l'ideale per essere inseriti in Blueprints e automazioni che ti avvisano quando i prezzi crollano.

---

## 📊 Sensori Creati (9 Entità)

L'integrazione crea automaticamente due categorie di sensori, estraendo i valori precisi al centesimo delle tariffe Fissa 12M e Flex:

### 💰 Costi Fissi (PCV / QVD)
I costi di commercializzazione, già calcolati su base annuale:
* `sensor.octopus_fissa_commercializzazione_luce` (€/anno)
* `sensor.octopus_fissa_commercializzazione_gas` (€/anno)
* `sensor.octopus_variabile_commercializzazione_luce` (€/anno)
* `sensor.octopus_variabile_commercializzazione_gas` (€/anno)

### ⚡ Materia Prima (Energia / Spread)
Il costo nudo dell'energia o lo spread per le tariffe indicizzate:
* `sensor.octopus_fissa_12m_luce` (€/kWh)
* `sensor.octopus_fissa_12m_gas` (€/Smc)
* `sensor.octopus_flex_mono_luce` (€/kWh)
* `sensor.octopus_flex_multi_luce` (€/kWh)
* `sensor.octopus_flex_gas` (€/Smc)

---

## 📥 Installazione tramite HACS (Consigliata)

Il metodo più semplice e veloce per installare l'integrazione e mantenerla aggiornata.

1. Apri **HACS** nel tuo Home Assistant.
2. Clicca sui tre puntini in alto a destra e seleziona **Repository personalizzati**.
3. Incolla l'URL di questo repository: `https://github.com/SalvatoreITA/Octopus-Italy-Tariffe`
4. Come categoria scegli **Integrazione**.
5. Clicca su **Aggiungi**.
6. Cerca "Octopus Tariffe" in HACS, scaricala e **riavvia Home Assistant**.

---

## ⚙️ Configurazione

Questa integrazione si installa in modo 100% visivo!

1. Vai su **Impostazioni** > **Dispositivi e servizi**.
2. Clicca sul pulsante in basso a destra **+ AGGIUNGI INTEGRAZIONE**.
3. Cerca **Octopus Tariffe**.
4. Clicca su Invia nella finestra che ti appare. Fatto! I tuoi 9 sensori sono immediatamente pronti all'uso.

## ☕ Supporta il Progetto

Ogni piccolo supporto fa un'enorme differenza: mi aiuta a mantenere vivo l'entusiasmo e mi stimola a creare e condividere nuove soluzioni per la community. Grazie di cuore per il tuo aiuto! 🚀

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/salvatore_dh)

## ❤️ Crediti
Sviluppato da [Salvatore Lentini - DomHouse.it](https://www.domhouse.it)
