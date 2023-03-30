import streamlit as st
import phaseFonction as pf
import connexionDB as cdb

# Connexion à la base de données
db = cdb.connexionDB()

# Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

# Title
st.title("Nombre d'essais en phase 1 / 2 / 3 / 4")
tab1, tab2 = st.tabs(["Essais d'Observation", "Essais Aleatoire "])


with tab1 :
    option = pf.find_Different_Type_Phase(cts)
    phase = st.multiselect('quel truc vous voulez voir',option)
    fichier = pf.find_All_Phase_Observation(cts,phase)
    st.write("Nombre d'essais :", len(fichier))
    st.dataframe(fichier)
    dict = pf.count_all_Phase(cts,option)
    st.bar_chart(dict)

with tab2 :
    option2 = pf.find_Different_Type_Phase(ctt)
    phase2 = st.multiselect('quel truc vous voulez voir', option2)
    fichier2 = pf.find_All_Phase_Aleatoire(ctt, phase2)
    st.write("Nombre d'essais :", len(fichier2))
    st.dataframe(fichier2)
    dict2 = pf.count_all_Phase(ctt, option2)
    st.bar_chart(dict2)

