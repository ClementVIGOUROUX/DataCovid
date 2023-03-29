import streamlit as st
import venueFonction as iff
import plotly.express as px


col1 = "Publications_ObsStudies"
col2="Publications_RandTrials"

st.header("Revues (colonne venue) publiant le plus d'absract au total et par trimestre")
option = iff.getAllYear(col1)
phase = st.selectbox("choisissez l'année",option)

tabP1, tabP2 = st.tabs(["Publication d'études d'Observation", "Publication d'essais Aleatoire "])

with tabP1:
    tab1, tab2, tab3, tab4 = st.tabs(["trimestre 1", "trimestre 2", "trimestre 3", "trimestre 4 "])
    with tab1 :
        t1 = iff.nb_publisher_venueT1(col1,phase)
        st.dataframe(t1)

        fig = px.bar(t1, x="_id", y="count", labels={"_id": "Venue", "count": "Nombre d'occurrences"})
        st.plotly_chart(fig)
    with tab2 :
        t2 = iff.nb_publisher_venueT2(col1, phase)
        st.dataframe(t2)
        fig = px.bar(t2, x="_id", y="count", labels={"_id": "Venue", "count": "Nombre d'occurrences"})
        st.plotly_chart(fig)
    with tab3 :
        t3 = iff.nb_publisher_venueT3(col1, phase)
        st.dataframe(t3)
        fig = px.bar(t3, x="_id", y="count", labels={"_id": "Venue", "count": "Nombre d'occurrences"})
        st.plotly_chart(fig)
    with tab4:
        t4 = iff.nb_publisher_venueT4(col1, phase)
        st.dataframe(t4)
        fig = px.bar(t4, x="_id", y="count", labels={"_id": "Venue", "count": "Nombre d'occurrences"})
        st.plotly_chart(fig)


with tabP2 :
    tab1, tab2, tab3, tab4 = st.tabs(["trimestre 1", "trimestre 2", "trimestre 3", "trimestre 4 "])
    with tab1:
        t1 = iff.nb_publisher_venueT1(col2, phase)
        st.dataframe(t1)

        fig = px.bar(t1, x="_id", y="count", labels={"_id": "Venue", "count": "Nombre d'occurrences"})
        st.plotly_chart(fig)
    with tab2:
        t2 = iff.nb_publisher_venueT2(col2, phase)
        st.dataframe(t2)
        fig = px.bar(t2, x="_id", y="count", labels={"_id": "Venue", "count": "Nombre d'occurrences"})
        st.plotly_chart(fig)
    with tab3:
        t3 = iff.nb_publisher_venueT3(col2, phase)
        st.dataframe(t3)
        fig = px.bar(t3, x="_id", y="count", labels={"_id": "Venue", "count": "Nombre d'occurrences"})
        st.plotly_chart(fig)
    with tab4:
        t4 = iff.nb_publisher_venueT4(col2, phase)
        st.dataframe(t4)
        fig = px.bar(t4, x="_id", y="count", labels={"_id": "Venue", "count": "Nombre d'occurrences"})
        st.plotly_chart(fig)



