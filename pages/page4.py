import pandas
import streamlit as st
import genreFonction as gf


st.title("Petit titre et c'est ok")
tab1, tab2 = st.tabs(["Essais d'Observation", "Essais Aleatoire "])

with tab1 :

    option = gf.find_Different_Type_Genre('ClinicalTrials_ObsStudies')
    phase = st.multiselect('quel truc vous voulez voir',option)
    fichier = gf.find_All_Genre('ClinicalTrials_ObsStudies',phase)
    st.write("Nombre d'essais :", len(fichier))
    st.dataframe(fichier)

with tab2 :
    option2 = gf.find_Different_Type_Genre('ClinicalTrials_RandTrials')
    phase2 = st.multiselect('quel truc vous voulez voir', option2)
    fichier2 = gf.find_All_Genre('ClinicalTrials_RandTrials', phase2)
    st.write("Nombre d'essais :", len(fichier2))
    st.dataframe(fichier2)
