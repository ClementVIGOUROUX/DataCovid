import connexionDB as cdb
import pandas as pd
import re

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
    pipeline = [{'$group': {'_id': '$registry', 'nb': {'$sum': 1}}}, {'$sort': {'nb': -1}}]
    dataframe = col.aggregate(pipeline)
    for doc in dataframe:
        data.append(doc)
    return data


def nb_publisher_venue(col):
    data = []
    pipeline = [{'$group': {'_id': '$venue', 'nb': {'$sum': 1}}}, {'$sort': {'nb': -1}}]
    dataframe = col.aggregate(pipeline)
    for doc in dataframe:
        data.append(doc)
    return data

def find_ivermectin_related(collection):
    ivermectin_docs = []
    search_term = re.compile('ivermectin', re.IGNORECASE)
    match collection.name:
        case "ClinicalTrials_ObsStudies" | "ClinicalTrials_RandTrials":
            myquery = {"$or": [{"interventions": search_term},{"title": search_term},{"abstract": search_term}]}
        case "Publications_RandTrials":
            myquery = {"$or": [{"concepts": search_term},{"meshTerms": search_term},{"title": search_term}]}
        case _:
            myquery = {}
    mydoc = collection.find(myquery)
    for x in mydoc:
        ivermectin_docs.append(x)
    all_docs = pd.DataFrame(ivermectin_docs)
    return all_docs

#Main
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials
pbs = db.Publications_ObsStudies
pbt = db.Publications_RandTrials

print(find_ivermectin_related(pbt))
#print(pbt.name)