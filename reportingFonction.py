import pymongo
import pandas
import connexionDB as cdb


def count_Collection(col):
    total = col.count_documents({})
    return total


def nb_par_Mois(col):
    data =[]
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
    dataframe = col.aggregate(pipeline)
    for doc in dataframe:
        data.append(doc)
    return data


def nb_publisher_registry(col):
    data = []
    db = cdb.connexionDB()
    mycol = db[col]
    pipeline = [{'$group': {'_id': '$registry', 'nb': {'$sum': 1}}}, {'$sort': {'nb': -1}}]
    dataframe = mycol.aggregate(pipeline)
    for doc in dataframe:
        data.append(doc)
    return data


def nb_publisher_venue(col):
    data = []
    db = cdb.connexionDB()
    mycol = db[col]
    pipeline = [{'$group': {'_id': '$venue', 'nb': {'$sum': 1}}}, {'$sort': {'nb': -1}}]
    dataframe = mycol.aggregate(pipeline)
    for doc in dataframe:
        data.append(doc)
    return data

#Main
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

print(count_Collection(cts))












