import streamlit as st
import ivermectinFunction as iF
import connexionDB as cdb

#Main
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

# Title
st.title("Recherche d'un mot clé dans les essais et les publications")
search_term = st.text_input("Recherche")
tab1, tab2, tab3 = st.tabs(["Publications", "Clinical Trials Studies","Clinical Trials Random Trials"])

with tab1 :
    option = iF.find_ivermectin_related(pbt,search_term)
    st.dataframe(option)

with tab2 :
    option2 = iF.find_ivermectin_related(cts,search_term)
    st.dataframe(option2)

with tab3 :
    option3 = iF.find_ivermectin_related(ctt,search_term)
    st.dataframe(option3)
