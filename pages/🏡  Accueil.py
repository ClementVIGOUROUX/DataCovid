import pandas
import streamlit as st
import reportingFonction as rF
import plotly.express as px
import plotly.figure_factory as ff
import connexionDB as cdb

#Main
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

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
            dataFrame = pandas.DataFrame(data)
            dataFrame = dataFrame.head()
            fig = px.bar(dataFrame, y='nb', x='_id')

            st.plotly_chart(fig)

        with tab2:
            data2 = rF.nb_publisher_registry(ctt)
            dataFrame2 = pandas.DataFrame(data2)
            dataFrame2 = dataFrame2.head()
            fig2 = px.bar(dataFrame2, y='nb', x='_id')
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
            dataFrame = pandas.DataFrame(data)
            dataFrame = dataFrame.head()
            fig = px.bar(dataFrame, y='nb', x='_id')
            st.plotly_chart(fig)

        with tab2:
            data2 = rF.nb_publisher_venue(pbt)
            dataFrame2 = pandas.DataFrame(data2)
            dataFrame2 = dataFrame2.head()
            fig2 =px.bar(dataFrame2,y='nb',x='_id')
            st.plotly_chart(fig2)

with st.container():
    st.header("erfgfdrtgfdg")
    col6, col7,col8 = st.columns(3)
    with col6:
        nbListe = [total1, total2, total3, total4]
        nomListe = ["ClinicalTrials_ObsStudies", "ClinicalTrials_RandTrials", "Publications_ObsStudies",
                    "Publications_RandTrials"]
        d = {'value': nomListe, 'nb': nbListe}
        dataNb = pandas.DataFrame(d)
        fig = px.pie(dataNb, values='nb', names='value', width=500, height=400)
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="right", x=0.5))
        st.plotly_chart(fig)
    with col7:
        fig2 = px.pie(dataNb, values='nb', names='value', width=500, height=400)
        fig2.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="right", x=0.5))
        st.plotly_chart(fig2)
    with col8:
        fig3 = px.pie(dataNb, values='nb', names='value', width=500, height=400)
        fig3.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="right", x=0.5))
        st.plotly_chart(fig3)


data = rF.nb_par_Mois(cts)
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

