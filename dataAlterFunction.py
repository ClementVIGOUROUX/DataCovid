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

def alterDateCTS():
    db = cdb.connexionDB()
    collection = db.ClinicalTrials_ObsStudies
    collection.update_many(
        {},
        [
            {
                "$set": {
                    "dateInserted": {
                        "$toDate": "$dateInserted"}
                }
            },
            {
                "$set": {
                    "date": {
                        "$toDate": "$date"}
                }
            }
        ]
    )

def alterDateCTT():
    db = cdb.connexionDB()
    collection = db.ClinicalTrials_RandTrials
    collection.update_many(
        {
            "$expr": {
                "$eq": [{"$strLenCP": "$dateInserted"}, 10]
            }
        },
        [
            {
                "$set": {
                    "dateInserted": {
                        "$toDate": "$dateInserted"
                    }
                }
            }
        ]
    )

    collection.update_many(
        {
            "$expr": {
                "$eq": [{"$strLenCP": "$date"}, 10]
            }
        },
        [
            {
                "$set": {
                    "date": {
                        "$toDate": "$date"
                    }
                }
            }
        ]
    )

def alterDatePBS():
    db = cdb.connexionDB()
    collection = db.Publications_ObsStudies
    collection.update_many(
      {},
      [
        {
          "$set": {
            "dateInserted": {
             "$toDate": "$dateInserted"}
            }
          },
          {
          "$set": {
            "datePublished": {
             "$toDate": "$datePublished"}
            }
          }
      ]
    )

def alterDatePBT():
    db = cdb.connexionDB()
    collection = db.Publications_RandTrials
    collection.update_many(
        {},
        [
            {
    "$set": {
        "dateInserted": {
    "$toDate": "$dateInserted"}
    }
    },
    {
    "$set": {
        "datePublished": {
    "$toDate": "$datePublished"}
    }
    }
    ]
    )

alterDatePBS()
