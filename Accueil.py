import pandas as pd
import streamlit as st
import reportingFonction as rF
import insererFonction as iF
import plotly.express as px
import connexionDB as cdb

#Main
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

def sidebar():
    with st.sidebar:
        st.title("Mettez votre fichier excel")
        file = st.file_uploader("")
        if file is not None:
            if iF.verif(file):
                data = iF.fichier_toJson(file)
                iF.inserer(data)
            else:
                st.error("Veuillez rentre un fichier xslx")

sidebar()

with st.container():
    col1, col2, = st.columns(2)

    with col1:
        total1 = rF.count_Collection(cts)
        total2 = rF.count_Collection(ctt)
        st.header("Nombre d'essai : "+str(total1+total2))
        st.subheader("ObsStudies : "+str(total1))
        st.subheader("RandTrials : "+str(total2))

    with col2:
        tab1, tab2 = st.tabs(["Essais d'Observation", "Essais Aleatoire "])
        with tab1:
            data = rF.nb_publisher_registry(cts)
            dataFrame = pd.DataFrame(data)
            dataFrame = dataFrame.head()
            fig = px.bar(dataFrame, y='nb', x='_id', title='Nombre d\'essais par ID', labels={'nb': 'Nombre d\'essais', '_id': 'ID'})

            st.plotly_chart(fig)

        with tab2:
            data2 = rF.nb_publisher_registry(ctt)
            dataFrame2 = pd.DataFrame(data2)
            dataFrame2 = dataFrame2.head()
            fig2 = px.bar(dataFrame, y='nb', x='_id', title='Nombre d\'essais par ID', labels={'nb': 'Nombre d\'essais', '_id': 'ID'})
            st.plotly_chart(fig2)


with st.container():

    col4, col5 = st.columns(2)

    with col4:
        total3 = rF.count_Collection(pbs)
        total4 = rF.count_Collection(pbt)
        st.header("Nombre de Publication : " + str(total3 + total4))
        st.subheader("ObsStudies : " + str(total3))
        st.subheader("RandTrials : " + str(total4))

    with col5:
        tab1, tab2 = st.tabs(["Publications_ObsStudies","Publications_RandTrials"])

        with tab1:
            data = rF.nb_publisher_venue(pbs)
            dataFrame = pd.DataFrame(data)
            dataFrame = dataFrame.head()
            fig = px.bar(dataFrame, y='nb', x='_id', title='Nombre de publications par ID', labels={'nb': 'Nombre de publications', '_id': 'ID'})
            st.plotly_chart(fig)

        with tab2:
            data2 = rF.nb_publisher_venue(pbt)
            dataFrame2 = pd.DataFrame(data2)
            dataFrame2 = dataFrame2.head()
            fig = px.bar(dataFrame, y='nb', x='_id', title='Nombre de publications par ID', labels={'nb': 'Nombre de publications', '_id': 'ID'})
            st.plotly_chart(fig2)

with st.container():
    st.header("Repartition des Essais et des Publications")
    col6, col7,col8 = st.columns(3)
    with col6:
        nbListe = [total1, total2, total3, total4]
        nomListe = ["ClinicalTrials_ObsStudies", "ClinicalTrials_RandTrials", "Publications_ObsStudies",
                    "Publications_RandTrials"]
        d = {'value': nomListe, 'nb': nbListe}
        dataNb = pd.DataFrame(d)
        fig = px.pie(dataNb, values='nb', names='value', width=500, height=400)
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="right", x=0.5))
        st.plotly_chart(fig)


tab1, tab2, tab3, tab4 = st.tabs(["ClinicalTrials_ObsStudies", "ClinicalTrials_RandTrials", "Publications_ObsStudies", "Publications_RandTrials"])

with tab1:
    liste =[]
    results = cts.find()
    for x in results:
        liste.append(x)
    fichier = pd.DataFrame(liste)
    st.write("Nombre d'essais :",
             len(fichier))
    st.dataframe(fichier)

    # Pipeline d'agrégation
    pipeline = [
        {
            "$group": {
                "_id": {"$year":"$date"},
                "count": {"$sum": 1}
            }
        }
    ]

    results = list(cts.aggregate(pipeline))
    if (len(results) != 0):
        fichier = pd.DataFrame(results)
        st.dataframe(fichier)

with tab3:
    liste =[]
    results = pbs.find()
    for x in results:
        liste.append(x)
    fichier = pd.DataFrame(liste)
    st.write("Nombre de publications :",
             len(fichier))
    st.dataframe(fichier)

    # Pipeline d'agrégation
    pipeline = [
        {
            "$group": {
                "_id": "$year",
                "count": {"$sum": 1}
            }
        }
    ]

    results = list(pbs.aggregate(pipeline))
    if (len(results) != 0):
        fichier = pd.DataFrame(results)
        st.dataframe(fichier)

with tab4:
    liste =[]
    results = pbt.find()
    for x in results:
        liste.append(x)
    fichier = pd.DataFrame(liste)
    st.write("Nombre de publications :",
             len(fichier))
    st.dataframe(fichier)

    # Pipeline d'agrégation
    pipeline = [
        {
            "$group": {
                "_id": "$year",
                "count": {"$sum": 1}
            }
        }
    ]

    results = list(pbt.aggregate(pipeline))
    if (len(results) != 0):
        fichier = pd.DataFrame(results)
        st.dataframe(fichier)

with tab2:
    liste =[]
    results = ctt.find()
    for x in results:
        liste.append(x)
    fichier = pd.DataFrame(liste)
    st.write("Nombre d'essais :",
             len(fichier))
    st.dataframe(fichier)