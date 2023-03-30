import pandas
import streamlit as st
import altmetricFonction as alt
import connexionDB as cdb

st.title(
    "Publications du mois courant triées par score altmetric décroissant")
tab1, tab2 = st.tabs(["Publications d'Observation", "Publications Aléatoires "])

# Main
db = cdb.connexionDB()

# Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

with tab1:
    fichier = alt.sortByAltmetric(pbs)
    st.write("Publications triées par Altmetric :",
             len(fichier))
    st.dataframe(fichier)


with tab2:
    fichier = alt.sortByAltmetric(pbt)
    st.write("Publications triées par Altmetric :",
             len(fichier))
    st.dataframe(fichier)