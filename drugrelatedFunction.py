import pandas as pd
import re

def find_drug_related(collection, mot):
    drug_docs = []
    search_term = re.compile('drug', re.IGNORECASE)
    myquery = {"interventions": {"$regex": mot, "$options": "i"}}
    mydoc = collection.find(myquery)
    for x in mydoc:
        drug_docs.append(x)
    all_docs = pd.DataFrame(drug_docs)
    return all_docs