import pandas
import streamlit as st
import accueil


# Title
st.title("Page 2")
accueil.sidebar()

with st.container():
    recherche = st.text_input('rechercher un mot')
    #fichier = pf.find_all('ClinicalTrials_ObsStudies')

    #st.dataframe(fichier)

