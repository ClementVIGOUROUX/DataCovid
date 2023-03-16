import connexionDB as cdb

def alterCircleToCommas():
    db = cdb.connexionDB()
    pbt = db.Publications_RandTrials
    result = pbt.update_many(
        {},
        [
            {
                "$set": {
                    "concepts": {
                        "$split": [
                            {"$replaceAll": {"input": "$concepts", "find": "•", "replacement": ","}},
                            ", "
                        ]
                    }
                }
            }
        ]
    )
    return(result)