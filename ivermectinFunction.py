import pandas as pd
import streamlit as st

def find_ivermectin_related(collection, search_term):
    ivermectin_docs = []
    match collection.name:
        case "ClinicalTrials_ObsStudies" | "ClinicalTrials_RandTrials":
            myquery = {"$or": [{"interventions": {"$regex": search_term, "$options": "i"}},{"title": {"$regex": search_term, "$options": "i"}},{"abstract": {"$regex": search_term, "$options": "i"}}]}
        case "Publications_RandTrials":
            myquery = {"$or": [{"concepts": {"$regex": search_term, "$options": "i"}},{"meshTerms": {"$regex": search_term, "$options": "i"}},{"title": search_term}]}
        case _:
            myquery = {}
    mydoc = collection.find(myquery)
    for x in mydoc:
        ivermectin_docs.append(x)
    all_docs = pd.DataFrame(ivermectin_docs)
    return all_docs