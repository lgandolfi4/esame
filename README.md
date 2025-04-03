# 🏡 Real Estate Valuation
Benvenuto nel progetto Real Estate Valuation!
Questo repository contiene un'analisi predittiva dei prezzi immobiliari nella regione di Sindian, Nuova Taipei, Taiwan.

-   Esplorazione dei Dati
L'analisi inizia con l'esplorazione del database utilizzando il notebook eda.ipynb.
No → Numero identificativo della transazione; è la chiave primaria del dataset.
X1 transaction date → Data della transazione immobiliare (espressa in un formato numerico).
X2 house age → Età dell’immobile in anni. Assume valori compresi tra 0 e 43.8.
X3 distance to the nearest MRT station → Distanza dalla stazione MRT più vicina (in metri). Assume valori compresi tra 23.38284 e 6488.021.
X4 number of convenience stores → Numero di minimarket nelle vicinanze. Assume valori compresi tra 0 e 10.
X5 latitude e X6 longitude → Coordinate geografiche dell’immobile. La prima assume valori compresi tra 24.93207 e 25.01459 e la seconda tra 121.47353 e 121.56627.
Y house price of unit area → Prezzo dell'immobile per unità di area (es. per metro quadro). Assume valori compresi tra 7.6 e 117.5.

Data la natura quantitativa della variabile di risposta, ho scelto di applicare il modello KNeighborsRegressor, che non viene preceduto da un'operazione di standardizzazione delle variabili poichè effettuando dei test ho notato come questa peggiorasse siginifcativamente la capacità di previsione dei modelli; infatti, il modello potrebbe performare meglio con covariate non scalate a causa della scala simile delle variabili, del tipo di modello utilizzato o delle specifiche caratteristiche del dataset, come la dimensione o la correlazione tra le variabili.

-   Modelli di Predizione
Tramite questo algoritmo vado a costruire due modelli per predirre il prezzo al metro quadro di immobili:
1) Modello base: Latitudine + Longitudine
2) Modello bonus: Età dell’immobile + Distanza dalla stazione MRT più vicina + numero di minimarket nelle vicinanze

-   Come utilizzare l'applicazione
Utilizzate il vostro terminale spostandovi nella directory "scripts" e digitando prima "python run_pipeline.py" (oppure "python3 run_pipeline.py" se non funziona la prima) e successivamente "streamlit run ui.py" verrete reindirizzati sul vostro browser predefinito di ricerca dove si aprirà la pagina web utile per stimare il prezzo al metro quadro degli immobili.
Sulla sinistra noterete la possibilità di scegliere il modello di previsione da voi preferito che in maodo molto intuitivo vi darà la possibilità di calcolare il costo al metro quadro dell'immobile.



