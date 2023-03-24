import streamlit as st
import connexionDB as cdb
from datetime import datetime
import pandas as pd
import plotly.express as px

st.title("Concepts (colonne concepts) les plus fréquents dans les publications (hors preprints) pendant une période donnée.")

#Connexion à la base de données mongoDB Atlas
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

# Affichage des widgets pour la date de début et de fin
start_date = st.date_input("Date de début :", datetime(2020, 1, 1))
end_date = st.date_input("Date de fin :", datetime(2020, 12, 31))

# Pipeline d'agrégation
pipeline = [
    {
        "$match": {
            "doctype": {"$ne": "preprint"},
            #"datePublished": {"$gte": start_date, "$lte": end_date}
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

# Exécuter le pipeline d'agrégation
results = list(pbt.aggregate(pipeline))
fichier = pd.DataFrame(results)
st.dataframe(fichier)

# Extraire les colonnes "_id" et "count" de "fichier"
data = fichier[["_id", "count"]]
fig = px.bar(data, x="_id", y="count", labels={"_id": "Concepts", "count": "Nombre d'occurrences"})
st.plotly_chart(fig)