# import module
import pandas
import streamlit as st
import insererFonction as iF


# Title 1
st.title("C'est une dinguerie ce qu'on peut faire!!!")

with st.sidebar:
    st.title("Mettez votre fichier excel")
    file = st.file_uploader("")
    if (file is not None):
        if iF.verif(file):
            dict= iF.fichier_toJson(file)
            st.write(dict)
            iF.inserer(dict)
        else:
            st.error("Pas bon fichier")

st.latex(r'''
   cl-x+mx*n^t= clement
    ''')


st.text("Ici c'est un dataframe")
fichier = pandas.read_excel('exel.xlsx', sheet_name='3 - Publications_ObsStudies')
st.dataframe(fichier)

st.text("et la un tableau")
#st.table(fichier)
