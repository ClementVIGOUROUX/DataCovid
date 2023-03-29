import streamlit as st
import genreFonction as gf
import connexionDB as cdb

st.title("Essais par genre")
tab1, tab2 = st.tabs(["Essais d'Observation", "Essais Aleatoire "])

# Connexion à la base de données
db = cdb.connexionDB()

# Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

with tab1 :

    option = gf.find_Different_Type_Genre(cts)
    phase = st.multiselect('Genre',option)
    fichier = gf.find_All_Genre_Observation(cts,phase)
    st.write("Nombre d'essais :", len(fichier))
    st.dataframe(fichier)

with tab2 :

    option2 = gf.find_Different_Type_Genre(ctt)
    phase2 = st.multiselect('Genre', option2)
    fichier2 = gf.find_All_Genre_Aleatoire(ctt, phase2)
    st.write("Nombre d'essais :", len(fichier2))
    st.dataframe(fichier2)
