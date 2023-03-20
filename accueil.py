# import module
import streamlit as st
import insererFonction as iF
import connexionDB as cdb

#Main
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

def sidebar():
    with st.sidebar:
        st.title("Mettez votre fichier excel")
        file = st.file_uploader("")
        if file is not None:
            if iF.verif(file):
                data = iF.fichier_toJson(file)
                iF.inserer(data)
            else:
                st.error("Veuillez rentre un fichier xslx")

sidebar()

# Title
st.title("DataCovid")

st.latex(r'''
   cl-x+mx*n^t= clement
    ''')
