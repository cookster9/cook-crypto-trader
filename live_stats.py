from cbpro_client import cbpro_client
from logger import logger

@cbpro_client
@logger
def get_live_stats(cbpro_client, logger, product = 'BTC-USD'):
    # Paramters are optional
    wsClient = cbpro_client.WebsocketClient(url="wss://ws-feed.pro.coinbase.com", products=product)

    #while() get stats now


    # Do other stuff...
    wsClient.close()
    return wsClient