import pymongo
import pandas
import connexionDB
def find_All(col):
    list = []
    for x in col.find():
        list.append(x)
    all = pandas.DataFrame(list)
    return all

#permet de recuperer les differents types de phases dans une collection
def find_Different_Type_Phase(col):
    list = []
    for x in col.distinct('phase'):
        list.append(x)
    return list

#permet de recuperer les phase avec un filtre
def find_Phase_Filtre(col,param):
    list = []
    myquery = {'phase': {'$in': param}}
    mydoc = col.find(myquery)
    for x in mydoc:
        list.append(x)
    all = pandas.DataFrame(list)
    return all



#utilise les 2 fonction d'au dessus pour tout faire
def find_All_Phase(col,list):
    condition = len(list)
    if (condition == 0):
        fichier = find_All(col)
    else:
        fichier = find_Phase_Filtre(col,list)
    return fichier



def count_all_Phase(col,list):
    dict = {}
    db = connexionDB.connexionDB()["sae"]
    mycol = db[col]
    for i in range(len(list)):
        dict[list[i]] = mycol.count_documents({'phase':list[i]})
    return dict