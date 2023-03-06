import pymongo
import pandas

def find_Different_Type_Genre(col):
    list = []
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
    for x in mycol.distinct('gender'):
        list.append(x)
    return list

def find_All(col):
    list = []
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
    for x in mycol.find():
        list.append(x)
    all = pandas.DataFrame(list)
    return all

#permet de recuperer les phase avec un filtre
def find_Genre_Filtre(col,param):
    list = []
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
    myquery = {'gender': {'$in': param}}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        list.append(x)
    all = pandas.DataFrame(list)
    return all

#utilise les 2 fonction d'au dessus pour tout faire
def find_All_Genre(col,list):
    condition = len(list)
    if (condition == 0):
        fichier = find_All(col)
    else:
        fichier = find_Genre_Filtre(col,list)
    return fichier