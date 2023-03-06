import streamlit as st
import accueil
import phaseFonction as pf


# Title
st.title("Petit titre et c'est ok")
tab1, tab2 = st.tabs(["Essais d'Observation", "Essais Aleatoire "])

accueil.sidebar()

with tab1 :
    option = pf.find_Different_Type_Phase('ClinicalTrials_ObsStudies')
    phase = st.multiselect('quel truc vous voulez voir',option)
    fichier = pf.find_All_Phase('ClinicalTrials_ObsStudies',phase)
    st.write("Nombre d'essais :", len(fichier))
    st.dataframe(fichier)
    dict = pf.count_all_Phase('ClinicalTrials_ObsStudies',option)
    st.bar_chart(dict)

with tab2 :
    option2 = pf.find_Different_Type_Phase('ClinicalTrials_RandTrials')
    phase2 = st.multiselect('quel truc vous voulez voir', option2)
    fichier2 = pf.find_All_Phase('ClinicalTrials_RandTrials', phase2)
    st.write("Nombre d'essais :", len(fichier2))
    st.dataframe(fichier2)
    dict2 = pf.count_all_Phase('ClinicalTrials_RandTrials', option2)
    st.bar_chart(dict2)

