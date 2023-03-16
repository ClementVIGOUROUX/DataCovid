import pandas
import connexionDB
import json

def verif(file):
    return file.name[-4:] == 'xlsx'

def fichier_toJson(file):
    dict={}
    pages =["1 - ClinicalTrials_ObsStudies","2 - ClinicalTrials_RandTrials","3 - Publications_ObsStudies","4 - Publications_RandTrials"]
    for i in range(len(pages)):
        fileE = pandas.read_excel(file, sheet_name=pages[i])
        fileJ = fileE.to_json(orient='records')
        dict[pages[i]] = fileJ
    return dict

def inserer(dict):
    db = connexionDB.connexionDB()
    collections = [
        ("ClinicalTrials_ObsStudies", db.ClinicalTrials_ObsStudies),
        ("ClinicalTrials_RandTrials", db.ClinicalTrials_RandTrials),
        ("Publications_ObsStudies", db.Publications_ObsStudies),
        ("Publications_RandTrials", db.Publications_RandTrials)
    ]

    for page, collection in collections:
        if collection.count_documents({}) == 0:
            data = json.loads(dict[page])
            collection.insert_many(data)
            return
