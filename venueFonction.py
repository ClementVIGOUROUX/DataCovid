import pandas
import pymongo
import datetime



def find_All(col):
    list = []
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
    for x in mycol.find():
        list.append(x)
    all = pandas.DataFrame(list)
    return all

def getAllYear(col):
    year = []
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
    pipeline = [
        {
            "$project":{
                "year":{
                    "$year":"$datePublished"
                }
            }
        }
    ]
    for x in mycol.aggregate(pipeline):
        year.append(x)
    dataframe = pandas.DataFrame(year)
    dataframe = dataframe.drop_duplicates(['year'])
    dataframe = dataframe.drop(['_id'], axis=1)
    return dataframe



def nb_publisher_venueT1(col , date):
    data = []
    start_date = datetime.datetime(date,1,1)
    end_date = datetime.datetime(date,3,31)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
    pipeline = [
        {
            "$match": {
                "datePublished": {"$gte": start_date, "$lte": end_date}
            }
        }, {
            "$unwind": "$venue"
        }, {
            "$group": {
                "_id": "$venue",
                "count": {"$sum": 1}
            }
        }, {
            "$sort": {"count": -1},
        }, {
            "$limit": 5
        }
    ]
    dataframe = mycol.aggregate(pipeline)
    for doc in dataframe:
        data.append(doc)
    return data


def nb_publisher_venueT2(col , date):
    data = []
    start_date = datetime.datetime(date,4,1)
    end_date = datetime.datetime(date,6,30)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
    pipeline = [
        {
            "$match": {
                "datePublished": {"$gte": start_date, "$lte": end_date}
            }
        }, {
            "$unwind": "$venue"
        }, {
            "$group": {
                "_id": "$venue",
                "count": {"$sum": 1}
            }
        }, {
            "$sort": {"count": -1},
        }, {
            "$limit": 5
        }
    ]
    dataframe = mycol.aggregate(pipeline)
    for doc in dataframe:
        data.append(doc)
    return data

def nb_publisher_venueT3(col , date):
    data = []
    start_date = datetime.datetime(date,7,1)
    end_date = datetime.datetime(date,9,30)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
    pipeline = [
        {
            "$match": {
                "datePublished": {"$gte": start_date, "$lte": end_date}
            }
        }, {
            "$unwind": "$venue"
        }, {
            "$group": {
                "_id": "$venue",
                "count": {"$sum": 1}
            }
        }, {
            "$sort": {"count": -1},
        }, {
            "$limit": 5
        }
    ]
    dataframe = mycol.aggregate(pipeline)
    for doc in dataframe:
        data.append(doc)
    return data


def nb_publisher_venueT4(col , date):
    data = []
    start_date = datetime.datetime(date,10,1)
    end_date = datetime.datetime(date,12,31)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sae"]
    mycol = mydb[col]
    pipeline = [
        {
            "$match": {
                "datePublished": {"$gte": start_date, "$lte": end_date}
            }
        }, {
            "$unwind": "$venue"
        }, {
            "$group": {
                "_id": "$venue",
                "count": {"$sum": 1}
            }
        }, {
            "$sort": {"count": -1},
        }, {
            "$limit": 5
        }
    ]
    dataframe = mycol.aggregate(pipeline)
    for doc in dataframe:
        data.append(doc)
    return data