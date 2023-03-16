import pandas
import streamlit as st

# Title
st.title("Rechercher document(s) par mot")

with st.container():
    recherche = st.text_input('Rechercher un mot (concept)')
    #fichier = pf.find_all('ClinicalTrials_ObsStudies')

    #st.dataframe(fichier)

