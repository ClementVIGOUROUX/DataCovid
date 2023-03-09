import pandas
import pymongo


def verif(file):
    if (file.name[-4:] == 'xlsx'):
        return True
    else:
        return False


def fichier_toJson(file):
    dict={}
    pages =["1 - ClinicalTrials_ObsStudies","2 - ClinicalTrials_RandTrials","3 - Publications_ObsStudies","4 - Publications_RandTrials"]
    for i in range(len(pages)):
        fileE = pandas.read_excel(file, sheet_name=pages[i])
        fileJ = fileE.to_json(orient='records')
        dict[pages[i]] = fileJ
    return dict

""""
col = ["ClinicalTrials_ObsStudies", "ClinicalTrials_RandTrials", "Publications_ObsStudies","Publications_RandTrials"]
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    for i in range(len(col)):
        mycol = mydb[col[i]]
        print(col[i])
        mycol.insert_many(dict[col[i]])"""



def inserer (dict):
    col = ["ClinicalTrials_ObsStudies", "ClinicalTrials_RandTrials", "Publications_ObsStudies","Publications_RandTrials"]
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col[0]]
    print(col[0])
    mycol.insert_many(dict["ClinicalTrials_ObsStudies"])
