import streamlit as st
import drugrelatedFunction as drf
import plotly.express as px
import connexionDB as cdb

#Main
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

# Title
st.title("Recherche mot cle d'intervention dans les essais")

mot = st.text_input("Recherche")

option = drf.find_drug_related(cts, mot)
st.dataframe(option)
option['month'] = option['date'].dt.month
grouped = option.groupby('month').size().reset_index(name='count')

fig = px.bar(grouped, x='month', y='count', title='Nombre d\'essais '+mot+' par mois', labels={'month': 'Mois', 'count': 'Nombre des essais'})

fig.update_layout(
    legend_title_text='Legend Title'
)

st.plotly_chart(fig, use_container_width=True)
