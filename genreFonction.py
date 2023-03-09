import pymongo
import pandas
import connexionDB as cdb

#SELECT * d'une collection (parametre)
def find_All(collection):
    result = []
    for x in collection.find():
        result.append(x)
    all = pandas.DataFrame(result)
    return all

#Retourner une liste des genres disponibles dans la collection
def find_Different_Type_Genre(collection):
    result = []
    for x in collection.distinct('gender'):
        result.append(x)
    return result

#Permet de recuperer les phase avec un filtre
def find_Genre_Filtre(collection,param):
    list = []
    myquery = {'gender': {'$in': param}}
    mydoc = collection.find(myquery)
    for x in mydoc:
        list.append(x)
    all = pandas.DataFrame(list)
    return all

#Utilise les 2 fonction d'au dessus pour tout faire
def find_All_Genre(collection,list):
    condition = len(list)
    if (condition == 0):
        fichier = find_All(collection)
    else:
        fichier = find_Genre_Filtre(collection,list)
    return fichier


#Main
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

#print(find_Different_Type_Genre(cts))
#print(find_All(pbt))
#print(find_Genre_Filtre(cts, ["Female"]))
#print(find_All_Genre(cts, ["Male"]))
