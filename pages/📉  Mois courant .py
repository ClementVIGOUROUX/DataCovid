import pandas
import streamlit as st
import altmetricFonction as alt
import connexionDB as cdb
from datetime import datetime

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

date = datetime.combine(st.date_input("Date :"), datetime.min.time())

with tab1:
    fichier = alt.sortByAltmetric(pbs, date)
    st.write("Publications triées par Altmetric :",
             len(fichier))
    st.dataframe(fichier)


with tab2:
    fichier = alt.sortByAltmetric(pbt, date)
    st.write("Publications triées par Altmetric :",
             len(fichier))
    st.dataframe(fichier)