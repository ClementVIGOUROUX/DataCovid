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
st.title("Drug Related Trials")
st.subheader("Clinical Trials with Type : Drug")

option = drf.find_drug_related(cts)
st.dataframe(option)
option['month'] = option['date'].dt.month
grouped = option.groupby('month').size().reset_index(name='count')

fig = px.line(grouped, x='month', y='count', title='Nombre des essais type Drug par mois', labels={'month': 'Mois', 'count': 'Nombre des essais'})

fig.update_layout(
    legend_title_text='Legend Title'
)

st.plotly_chart(fig, use_container_width=True)
