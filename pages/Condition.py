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
    liste =[]
    results = cts.find(query)
    for x in results:
        if(isinstance(x['interventions'], list)):
            liste.append(x)
    fichier = pd.DataFrame(liste)
    if not fichier.empty:
        st.dataframe(fichier)
    else:
        st.write("Aucun essai avec cette condition")

with tab2:
    results = ctt.find(query)
    fichier = pd.DataFrame(results)
    if not fichier.empty:
        st.dataframe(fichier)
    else:
        st.write("Aucun essai avec cette condition")