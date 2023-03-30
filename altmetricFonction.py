from datetime import date
import pandas
import connexionDB as cdb


def find_All(collection):
    list = []
    for x in collection.find():
        list.append(x)
    all = pandas.DataFrame(list)
    return all


# permet de recuperer les differents types de phases dans une collection
def find_Different_Type_Phase(col):
    list = []
    for x in col.distinct('phase'):
        list.append(x)
    return list


def sortByAltmetric(collection, date):
    #myquery = {'dateInserted' : }
    current_month = date.month
    current_year = date.year

    data = []
    db = cdb.connexionDB()

    #pipeline = [{'$sort': {'altmetric' : 1, 'timesCited' : 1}}]

    dataframe = collection.find({}).sort("altmetric", -1)

    for doc in dataframe:
        data.append(doc)

    all = pandas.DataFrame(data)

    all['datePublished'] = pandas.to_datetime(all['datePublished'])
    #month = all['datePublished'].dt.month


    new_all = []
    for index in all.index:
        month = all['datePublished'][index].month
        year = all['datePublished'][index].year
        if current_month == month and current_year == year:
            new_all.append(all.iloc[index])

    return new_all

    """
    db.publis.aggregate([
    {$undb.publis.aggregate([
    {$unwind : '$authors'},
    {$group : { _id : '$authors', nbPublis : {$count : {} }}},
    {$sort : {'nbPublis' : 1}}
]);wind : '$authors'},
    {$group : { _id : '$authors', nbPublis : {$count : {} }}},
    {$sort : {'nbPublis' : 1}}
]);

    """

# permet de recuperer les phase avec un filtre
def find_Phase_Filtre(col, param):
    list = []
    myquery = {'phase': {'$in': param}}
    mydoc = col.find(myquery)
    for x in mydoc:
        list.append(x)
    all = pandas.DataFrame(list)
    return all


# utilise les 2 fonction d'au dessus pour tout faire
def find_All_Phase(col, list):
    condition = len(list)
    if (condition == 0):
        fichier = find_All(col)
    else:
        fichier = find_Phase_Filtre(col, list)
    return fichier


def count_all_Phase(col, list):
    dict = {}
    for i in range(len(list)):
        dict[list[i]] = col.count_documents({'phase': list[i]})
    return dict
