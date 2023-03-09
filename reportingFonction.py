import pymongo
import pandas
import connexionDB


def count_Collection(col):
    db = connexionDB.connexionDB()["sae"]
    mycol = mydb[col]
    total = mycol.count_documents({})
    return total


def nb_par_Mois(col):
    data =[]
    db = connexionDB.connexionDB()["sae"]
    mycol = db[col]
    pipeline = [
    {"$project":{
        "month":{"$month":{"$dateFromString": {"dateString": "$date","format": "%m/%d/%Y"}}},
        "year": {"$year": {"$dateFromString": {"dateString": "$date","format": "%m/%d/%Y"}}}
    }},
    {
        "$group":{
            "_id":{"annee":"$year","mois":"$month"},
            "count":{"$sum":1}
    }}]
    dataframe = mycol.aggregate(pipeline)
    for doc in dataframe:
        data.append(doc)
    return data

data = nb_par_Mois("ClinicalTrials_ObsStudies")



print(data)





