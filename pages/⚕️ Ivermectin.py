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
st.title("Ivermectin Related Trials and Studies")
tab1, tab2, tab3 = st.tabs(["Publications", "Clinical Trials Studies","Clinical Trials Random Trials"])

with tab1 :
    option = iF.find_ivermectin_related(pbt)
    st.dataframe(option)

with tab2 :
    option2 = iF.find_ivermectin_related(cts)
    st.dataframe(option2)

with tab3 :
    option3 = iF.find_ivermectin_related(ctt)
    st.dataframe(option3)
