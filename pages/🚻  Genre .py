import streamlit as st
import genreFonction as gf
import plotly.express as px
import connexionDB as cdb

st.title("Essais par genre")
tab1, tab2 = st.tabs(["Essais d'Observation", "Essais Aleatoire "])

# Connexion à la base de données
db = cdb.connexionDB()

# Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials

with tab1 :

    option = gf.find_Different_Type_Genre(cts)
    phase = st.multiselect('Genre',option)
    fichier = gf.find_All_Genre(cts,phase)
    st.write("Nombre d'essais :", len(fichier))
    st.dataframe(fichier)
    dict = gf.count_all_Genre(cts, option)
    fig = px.bar(x=list(dict.keys()), y=list(dict.values()), labels={'x': 'Phase', 'y': 'Nombre d\'essais'})
    fig.update_layout(title='Nombre d\'essais par genre', xaxis_title='Genre',
                      yaxis_title='Nombre d\'essais')
    st.plotly_chart(fig)

with tab2 :

    option2 = gf.find_Different_Type_Genre(ctt)
    phase2 = st.multiselect('Genre', option2)
    fichier2 = gf.find_All_Genre(ctt, phase2)
    st.write("Nombre d'essais :", len(fichier2))
    st.dataframe(fichier2)
    dict = gf.count_all_Genre(ctt, option)
    fig = px.bar(x=list(dict.keys()), y=list(dict.values()), labels={'x': 'Phase', 'y': 'Nombre d\'essais'})
    fig.update_layout(title='Nombre d\'essais par genre', xaxis_title='Genre',
                      yaxis_title='Nombre d\'essais')
    st.plotly_chart(fig)
