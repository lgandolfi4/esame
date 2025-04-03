import os
import sys 
sys.path.append(os.path.abspath('..'))
 
import sqlite3
from src import config
import streamlit as st
import pickle
import pandas as pd
import numpy as np
 

with open(os.path.join(config.MODELS_PATH, "rf.pickle"), "rb") as file:
        modello = pickle.load(file)
with open(os.path.join(config.MODELS_PATH, "rf.pickle_bonus"), "rb") as file:
        modello_bonus = pickle.load(file)


 
# Creazione interfaccia Streamlit
st.set_page_config(page_title="Real Estate Valuation", page_icon="🏠", layout="centered")  # Imposta il layout della pagina
st.title("🏡 Real Estate Valuation")

# Selezione del modello
st.sidebar.header("Opzioni")  # sposta la selezione del modello laterale
modello_scelto = st.sidebar.selectbox("Scegli il modello di previsione:", ["Modello Base", "Modello Bonus"])

# Input dinamici in base al modello scelto
if modello_scelto == "Modello Base":
    st.subheader("📍 Inserisci le coordinate")  # Aggiunto sottotitolo
    Latitudine = st.number_input("Inserisci la latitudine:", key="latitudine")
    Longitudine = st.number_input("Inserisci la longitudine:", key="longitudine")
    if st.button("📊 Calcola costo dell'immobile"):
        if (Latitudine < 24.93207 or Latitudine > 25.01459) or (Longitudine < 121.47353 or Longitudine > 121.56627):
            st.warning("⚠️ Coordinate non valide!")
        else:
            X_vector = [[Latitudine, Longitudine]]
            prediction = abs(modello.predict(X_vector))
            st.success(f"💰 Il costo stimato al m^2 dell'immobile è: {prediction.round(2)}")
else:
    st.subheader("🏠 Inserisci i dettagli dell'immobile")  #Aggiunto sottotitolo
    Età_casa = st.number_input("🏗️ Inserisci età della casa:")
    Distanza_MRT = st.number_input("🚆 Inserisci distanza da stazione più vicina:")
    Numero_convenience_store = st.number_input("🏪 Inserisci numero di mini market nelle vicinanze:")
    if st.button("📊 Calcola costo dell'immobile"):
        if (Età_casa < 0 or Distanza_MRT < 0  or Numero_convenience_store < 0):
            st.warning("⚠️ Valori immessi non validi!")
        else:
            X_vector = [[Età_casa, Distanza_MRT, Numero_convenience_store]]
            prediction = abs(modello_bonus.predict(X_vector))
            st.success(f"💰 Il costo stimato al m^2 dell'immobile è: {prediction.round(2)}")
