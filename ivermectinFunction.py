import pandas as pd
import re

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