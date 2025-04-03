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

Data la natura quantitativa della variabile di risposta, ho optato per l'applicazione del modello KNeighborsRegressor, senza precederlo da una fase di standardizzazione 
delle variabili. Durante le prove, infatti, ho osservato che la standardizzazione peggiorava significativamente le performance predittive del modello. È possibile che il 
modello ottenga risultati migliori con covariate non scalate, grazie alla scala simile delle variabili, alla tipologia del modello impiegato o alle caratteristiche specifiche 
del dataset, come la sua dimensione o la correlazione tra le variabili.

# Modelli di Predizione
Tramite questo algoritmo vado a costruire due modelli per predirre il prezzo al metro quadro di immobili:
1) Modello base: Latitudine + Longitudine
2) Modello bonus: Età dell’immobile + Distanza dalla stazione MRT più vicina + numero di minimarket nelle vicinanze

# Come utilizzare l'applicazione
Dopo aver scaricato la cartella del progetto, aprire un IDE come VsCode
Successivamente imposta la cartella di lavoro "scripts" digitando "python run_pipeline.py" (oppure "python3 run_pipeline.py" se la prima non funziona) ed infine "streamlit run ui.py". Verrete reindirizzati al vostro browser predefinito, dove si aprirà la pagina web utile per stimare il prezzo al metro quadro degli immobili. Sulla sinistra noterete la possibilità di scegliere il modello di previsione che preferite, il quale, in modo molto intuitivo, vi permetterà di calcolare il costo al metro quadro dell'immobile.

#  Visualizzazione dei Dati con Tableau:
Al seguente link:

https://public.tableau.com/shared/CF9JM2HKX?:display_count=n&:origin=viz_share_link

è riportata una mappa satellitare interattiva dei prezzi originali (del dataset originale) ottenuta utilizzando Tableau.
Per una consultazione più dettagliata, utilizza i filtri a destra della mappa per selezionare intervalli di dati come l'età delle case, e altre variabili.



