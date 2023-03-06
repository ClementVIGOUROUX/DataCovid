# import module
import pandas
import streamlit as st


def sidebar():
    with st.sidebar:
        st.title("Mettez votre fichier excel")
        file = st.file_uploader("")
        if (file is not None) :
               if (file.name[-4:] == 'xlsx') :
                    excel = pandas.read_excel(file, sheet_name="1 - ClinicalTrials_ObsStudies")
                    excelJson = excel.to_json(orient="index")
                    st.json(excelJson)

               else:
                    st.error("veuillez rentrer un fichier excel")

st.balloons()
st.snow()
# Title
st.title("C'est une dinguerie ce qu'on peut faire!!!")

sidebar()

st.latex(r'''
   cl-x+mx*n^t= clement
    ''')


st.text("Ici c'est un dataframe")
fichier = pandas.read_excel('exel.xlsx', sheet_name='3 - Publications_ObsStudies')
st.dataframe(fichier)

st.text("et la un tableau")
#st.table(fichier)
