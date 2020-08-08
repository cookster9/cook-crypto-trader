from cbpro_client import cbpro_client
from logger import logger
import json
import sys
import string
from datetime import datetime, timedelta
from pymongo import MongoClient

@cbpro_client
@logger
def get_history(cbpro_client, logger, product = 'BTC-USD'):
    """ Makes deposit into USD Wallet

    Params: 
        - product (pair): string default BTC-USD
    Return: 
        - history over timeframe
        [
        [ time, low, high, open, close, volume ],
        [ 1415398768, 0.32, 4.2, 0.35, 4.2, 12.3 ],
        ...
        ]
    """
    startTime = (datetime.now() - timedelta(minutes=600)).isoformat()
    endTime = datetime.now().isoformat()
    btc_history = cbpro_client.get_product_historic_rates(product, granularity = 300, start = startTime, end = endTime)
    mongo_client = MongoClient('mongodb://localhost:27017/')
    # specify the database and collection
    db = mongo_client.db
    BTC_collection = db.crypto
    addHistoryToMongo(btc_history,BTC_collection)    

    return btc_history

def addHistoryToMongo(history,BTC_collection):   
    index = 0
    for line in history:
        json = {"time":line[0],"low":line[1],"high":line[2],"open":line[3],"close":line[4],"volume":line[5]}
        BTC_collection.insert_one(json)
        index+=1
    return