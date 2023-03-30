import streamlit as st
import connexionDB as cdb
import pandas as pd

st.title("Nombre d'essais par type de groupe")

#Connexion à la base de données mongoDB Atlas
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies

# Pipeline d'agrégation
pipeline = [
    {
        "$group": {
            "_id": "$interventions.arm_group_labels",
            "count": {"$sum": 1}
        }
    }
]

results = list(cts.aggregate(pipeline))
if (len(results) != 0):
    fichier = pd.DataFrame(results)
    st.dataframe(fichier)