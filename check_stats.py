from cbpro_client import cbpro_client
from logger import logger
import json
import sys
import string

@cbpro_client
@logger
def check_stats(cbpro_client, logger, product = 'BTC-USD'):
    """ Check stats of a pair

    Params: 
        - product (pair): string default BTC-USD
    Return: 
        - price response
    
    {
        "open": "6745.61000000", 
        "high": "7292.11000000", 
        "low": "6650.00000000", 
        "volume": "26185.51325269", 
        "last": "6813.19000000", 
        "volume_30day": "1019451.11188405"
    }


    """
    logger.info("Getting price")
    btc_stats = cbpro_client.get_product_24hr_stats(product)
    logger.info("Last Price: {}".format(btc_stats.get("last")))

    resp = btc_stats

    if 'message' in resp.keys():
        logger.warning("message in keys?")
    else:
        logger.info("Stats Response: {}".format(resp))
    
    return resp
