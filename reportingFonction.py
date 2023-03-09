import pymongo
import pandas



def count_Collection(col):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
    total = mycol.count_documents({})
    return total


def nb_par_Mois(col):
    data =[]
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
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





