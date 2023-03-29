import connexionDB as cdb
import json

#Connexion à la base de données mongoDB Atlas
db = cdb.connexionDB()

#Acces aux collections
cts = db.ClinicalTrials_ObsStudies
ctt = db.ClinicalTrials_RandTrials

# Récupération de toutes les données de la collection
data = cts.find()

# Itération sur chaque document
for document in data:
    if 'interventions' in document:
        # Récupération de la chaîne de caractères représentant une liste d'interventions
        interventions_str = document['interventions']

        # Verifier si interventions_str est une liste
        if isinstance(interventions_str, list):
            continue
        else:
            # Afficher les interventions qui ne sont pas une liste
            print(f"Interventions value is not a list: {interventions_str}")

            # Remplacement des guillemets simples par des guillemets doubles
            interventions_str = interventions_str.replace("'", "\"")

            # Remplacement des mots "None" par des valeurs vides
            interventions_str = interventions_str.replace("None", "\"None\"")

            # Conversion de la chaîne en une liste de dictionnaires
            try:
                interventions_list = json.loads(interventions_str)
            except json.JSONDecodeError as e:
                print(f"Impossible de convertir la chaîne en liste de dictionnaires pour le document: {e}")
                continue

            # Mise à jour du document avec la liste d'interventions
            cts.update_one({'_id': document['_id']}, {'$set': {'interventions': interventions_list}})