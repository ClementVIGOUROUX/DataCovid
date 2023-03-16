import pandas
import streamlit as st
import altmetricFonction as alt
import connexionDB as cdb

st.title(
    "Publications du mois courant (ex mai 2020) triées par score altmetric décroissant et départagées par citations décroissantes")
tab1, tab2 = st.tabs(["Publications d'Observation", "Publications Aléatoires "])

# Main
db = cdb.connexionDB()

# Acces aux collections
cts = "db.ClinicalTrials_ObsStudies"
ctt = "db.ClinicalTrials_RandTrials"
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

with tab1:
    fichier = alt.sortByAltmetric(pbs)
    st.write("Publications triées par Altmetric et départagées par le nombre de fois que la publication a été cité :",
             len(fichier))
    st.dataframe(fichier)


with tab2:
    fichier = alt.sortByAltmetric(pbt)
    st.write("Publications triées par Altmetric et départagées par le nombre de fois que la publication a été cité :",
             len(fichier))
    st.dataframe(fichier)