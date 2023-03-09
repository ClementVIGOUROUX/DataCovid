import pandas
import streamlit as st
import reportingFonction as rF
import plotly.express as px

col1, col2 , col3= st.columns(3)

with st.container():
    with col1:
        total1 = rF.count_Collection("ClinicalTrials_ObsStudies")
        total2 = rF.count_Collection("ClinicalTrials_RandTrials")
        st.header("Nombre d'essai : "+str(total1+total2))
        st.subheader("ObsStudies : "+str(total1))
        st.subheader("RandTrials : "+str(total2))
    with col2:
        st.write()
    with col3:
        total3 = rF.count_Collection("Publications_ObsStudies")
        total4 = rF.count_Collection("Publications_RandTrials")
        st.header("Nombre de Publication : "+str(total3 + total4))
        st.subheader("ObsStudies : "+str(total3))
        st.subheader("RandTrials : "+str(total4))

col4, col5, col6 = st.columns(3)

with st.container():
    with col4:

        nbListe = [total1,total2,total3,total4]
        nomListe = ["ClinicalTrials_ObsStudies","ClinicalTrials_RandTrials","Publications_ObsStudies","Publications_RandTrials"]
        d = {'value':nomListe,'nb':nbListe}
        dataNb = pandas.DataFrame(d)
        fig = px.pie(dataNb,values='nb',names='value',width=500, height=400)
        fig.update_layout(legend=dict(orientation="h",yanchor="bottom",y=-0.5,xanchor="right",x=0.5))
        st.plotly_chart(fig)
    with col5:
        st.write()
    with col6:
        fig = px.histogram(dataNb, y='nb', x='value',width=500, height=400)
        st.plotly_chart(fig)

with st.container():
    data = rF.nb_par_Mois("ClinicalTrials_ObsStudies")
    d = pandas.DataFrame(data)
    count = []
    boup = []
    for i in range(len(d)):
        count.append((d['count'][i]))
        boup.append(d['_id'][i])
    final = []
    for j in range(len(boup)):
        a = boup[j].get('mois')
        b = boup[j].get('annee')
        date = str(a)+'/'+str(b)
        final.append(date)
    data = pandas.DataFrame({'date':final,'nb':count})
    g = data.set_index('date')
    st.area_chart(g)