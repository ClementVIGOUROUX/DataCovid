import pymongo

#Connexion à la base de données MongoDB Atlas (Paris)
def connexionDB():
    password = "$iutinfo"
    client = pymongo.MongoClient(f"mongodb+srv://admin:{password}@iut.wauv1kb.mongodb.net/test?retryWrites=true&w=majority")
    db = client['sae']
    return db