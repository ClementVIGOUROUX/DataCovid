import streamlit as st
import pandas as pd
import connexionDB as cdb

# Connexion à la base de donnees
db = cdb.connexionDB()

# Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials

st.title("Recherche de conditions d’un essai")

mot = st.text_input("Recherche", "")

tab1, tab2 = st.tabs(["ClinicalTrials_ObsStudies", "ClinicalTrials_RandTrials"])

query = {"conditions": {"$regex": mot, "$options": "i"}}

with tab1:
    results = cts.find(query)
    fichier = pd.DataFrame(results)
    st.dataframe(fichier)

with tab2:
    results = ctt.find(query)
    fichier = pd.DataFrame(results)
    st.dataframe(fichier)