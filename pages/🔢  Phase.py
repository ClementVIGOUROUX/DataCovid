import streamlit as st
import phaseFonction as pf
import connexionDB as cdb
import plotly.express as px

# Connexion à la base de données
db = cdb.connexionDB()

# Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

# Titre
st.title("Nombre d'essais en phase 1 / 2 / 3 / 4")
tab1, tab2 = st.tabs(["Essais d'Observation", "Essais Aleatoire "])


with tab1 :
    option = pf.find_Different_Type_Phase(cts)
    phase = st.multiselect('Phase', option)
    fichier = pf.find_All_Phase(cts, phase)
    st.write("Nombre d'essais :", len(fichier))
    st.dataframe(fichier)
    dict = pf.count_all_Phase(cts, option)
    fig = px.bar(x=list(dict.keys()), y=list(dict.values()), labels={'x': 'Phase', 'y': 'Nombre d\'essais'})
    fig.update_layout(title='Nombre d\'essais par phase', xaxis_title='Phase',
                      yaxis_title='Nombre d\'essais')
    st.plotly_chart(fig)

with tab2 :
    option2 = pf.find_Different_Type_Phase(ctt)
    phase2 = st.multiselect('Phase', option2)
    fichier2 = pf.find_All_Phase(ctt, phase2)
    st.write("Nombre d'essais :", len(fichier2))
    st.dataframe(fichier2)
    dict2 = pf.count_all_Phase(ctt, option2)
    fig = px.bar(x=list(dict2.keys()), y=list(dict2.values()), labels={'x': 'Phase', 'y': 'Nombre d\'essais'})
    fig.update_layout(title='Nombre d\'essais par phase', xaxis_title='Phase',
                      yaxis_title='Nombre d\'essais')
    st.plotly_chart(fig)
