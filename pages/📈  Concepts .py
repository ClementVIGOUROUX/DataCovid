import streamlit as st
import connexionDB as cdb
from datetime import datetime
import pandas as pd
import plotly.express as px

st.title("Concepts (colonne concepts) les plus fréquents dans les publications (hors preprints) pendant une période donnée.")

#Connexion à la base de données mongoDB Atlas
db = cdb.connexionDB()

#Acces aux collections
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

# Affichage des widgets pour la date de début et de fin
start_date = datetime.combine(st.date_input("Date de début :"), datetime.min.time())
end_date = datetime.combine(st.date_input("Date de fin :"), datetime.min.time())

# Pipeline d'agrégation
pipeline = [
    {
        "$match": {
            "doctype": {"$ne": "preprint"},
            "datePublished": {"$gte": start_date, "$lte": end_date}
        }
    }, {
        "$unwind": "$concepts"
    }, {
        "$group": {
            "_id": "$concepts",
            "count": {"$sum": 1}
        }
    }, {
        "$sort": {"count": -1},
    }, {
        "$limit": 50
    }
]

tab1, tab2 = st.tabs(["Publications_ObsStudies", "Publications_RandTrials"])

with tab1:
    # Exécuter le pipeline d'agrégation
    results = list(pbs.aggregate(pipeline))
    if (len(results) != 0):
        fichier = pd.DataFrame(results)
        st.dataframe(fichier)

        # Extraire les colonnes "_id" et "count" de "fichier"
        data = fichier[["_id", "count"]]
        fig = px.bar(data, x="_id", y="count", labels={"_id": "Concepts", "count": "Nombre d'occurrences"})
        st.plotly_chart(fig)

    else:
        st.text("Pas de publications pendant la période choisie. Veuillez changer la période")

with tab2:
    # Exécuter le pipeline d'agrégation
    results = list(pbt.aggregate(pipeline))
    if (len(results) != 0):
        fichier = pd.DataFrame(results)
        st.dataframe(fichier)

        # Extraire les colonnes "_id" et "count" de "fichier"
        data = fichier[["_id", "count"]]
        fig = px.bar(data, x="_id", y="count", labels={"_id": "Concepts", "count": "Nombre d'occurrences"})
        st.plotly_chart(fig)

    else:
        st.text("Pas de publications pendant la période choisie. Veuillez changer la période")