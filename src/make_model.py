from src import config
import sqlite3
import pandas as pd
import numpy as np
import pickle

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

import os
import sys
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path

import logging
# Set up logging

def load_data():
    """Loads data from the SQLite database."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    query =f"SELECT * FROM {config.RAW_TABLE}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def train_model():
     """train logistic model"""
     df = load_data()
     X=df[['Latitude','Longitude']]
     y=df['HousePrice']
     df_indices = df.index

     # Train-test split (preserve indices)
     X_train, X_test, y_train, y_test, train_idx, test_idx = train_test_split(
         X, y, df_indices, test_size=0.2, random_state=42
     )
     
     modello=KNeighborsRegressor(n_neighbors=
                              5)
     modello.fit(X_train, y_train)
     y_pred= modello.predict(X_test)
 
     logging.info('saving KNN model...')
     with open(os.path.join(config.MODELS_PATH, "knn.pickle"), "wb") as file:
         pickle.dump(modello,file)


def train_model_bonus():
     """train logistic model"""
     df = load_data()
     X=df[['HouseAge','DistanceToMRT','NumberOfConvenienceStores']]
     y=df['HousePrice']
     df_indices = df.index
    
     # Train-test split (preserve indices)
     X_train, X_test, y_train, y_test, train_idx, test_idx = train_test_split(
         X, y, df_indices, test_size=0.2, random_state=42
     )
     
     modello_bonus=KNeighborsRegressor(n_neighbors=
                              5)
     modello_bonus.fit(X_train, y_train)
     y_pred= modello_bonus.predict(X_test)
 
     logging.info('saving KNN model...')
     with open(os.path.join(config.MODELS_PATH, "knn.pickle_bonus"), "wb") as file:
         pickle.dump(modello_bonus,file)

    
    