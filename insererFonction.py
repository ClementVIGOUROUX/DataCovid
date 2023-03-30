import pandas
import connexionDB as cdb
import json
import dataAlterFunction as daf

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
    db = cdb.connexionDB()
    collections = [
        ("1 - ClinicalTrials_ObsStudies", db.ClinicalTrials_ObsStudies),
        ("2 - ClinicalTrials_RandTrials", db.ClinicalTrials_RandTrials),
        ("3 - Publications_ObsStudies", db.Publications_ObsStudies),
        ("4 - Publications_RandTrials", db.Publications_RandTrials)
    ]

    for page, collection in collections:
        data = json.loads(dict[page])
        collection.insert_many(data)

    daf.alterDatePBS()
    daf.alterDatePBT()
    daf.alterDateCTS()