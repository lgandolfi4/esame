# 🏡 Real Estate Valuation
Benvenuto nel progetto Real Estate Valuation!
Questo repository contiene un'analisi predittiva dei prezzi immobiliari nella regione di Sindian, Nuova Taipei, Taiwan.

# Esplorazione dei Dati
L'analisi inizia con l'esplorazione del database utilizzando il notebook eda.ipynb.
-   No → Numero identificativo della transazione; è la chiave primaria del dataset.
-   X1 transaction date → Data della transazione immobiliare (espressa in un formato numerico).
-   X2 house age → Età dell’immobile in anni. Assume valori compresi tra 0 e 43.8.
-   X3 distance to the nearest MRT station → Distanza dalla stazione MRT più vicina (in metri). Assume valori compresi tra 23.38284 e 6488.021.
-   X4 number of convenience stores → Numero di minimarket nelle vicinanze. Assume valori compresi tra 0 e 10.
-   X5 latitude e X6 longitude → Coordinate geografiche dell’immobile. La prima assume valori compresi tra 24.93207 e 25.01459 e la seconda tra 121.47353 e 121.56627.
-   Y house price of unit area → Prezzo dell'immobile per unità di area (es. per metro quadro). Assume valori compresi tra 7.6 e 117.5

# Modelli di Predizione
Ho scelto di utilizzare un modello Random Forest Regressor perché generalmente offre un'elevata accuratezza nelle previsioni e non richiede complesse strategie di preprocessing.
Tramite questo algoritmo costruisco due modelli per predire il prezzo al metro quadro degli immobili:

1) Modello base: Latitudine + Longitudine
2) Modello bonus: Età dell’immobile + Distanza dalla stazione MRT più vicina + numero di minimarket nelle vicinanze

Tutti i modelli sono stati addestrati utilizzando Random Forest Regressor, con i parametri lasciati al valore predefinito.
# Come utilizzare l'applicazione
Dopo aver scaricato la cartella del progetto, apri un IDE come VS Code
Successivamente, imposta la cartella di lavoro 'scripts', digita 'python run_pipeline.py' (oppure 'python3 run_pipeline.py' se la prima non funziona) e infine 'streamlit run ui.py'. Verrete reindirizzati al vostro browser predefinito, dove si aprirà la pagina web utile per stimare il prezzo al metro quadro degli immobili. Sulla sinistra noterete la possibilità di scegliere il modello di previsione che preferite, il quale, in modo molto intuitivo, vi permetterà di calcolare il costo al metro quadro dell'immobile.

#  Visualizzazione dei Dati con l'utilizzo di Tableau:
Al seguente link:

https://public.tableau.com/shared/CF9JM2HKX?:display_count=n&:origin=viz_share_link

è riportata una mappa satellitare interattiva dei prezzi originali (del dataset originale) ottenuta utilizzando Tableau.
Per una consultazione più dettagliata, utilizza i filtri a destra della mappa per selezionare intervalli di dati come l'età delle case e altre variabili.





