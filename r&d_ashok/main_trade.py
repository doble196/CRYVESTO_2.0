import pandas as pd
import os
from dotenv import load_dotenv
import trade_api as ta



# comment these after uncommenting loadenv 
#alpaca_secret_key='QrWTvuqjdWDgx7Klqe5iWIR8K5iESy6DFugfV4Xy'
#alpaca_api_key='PKSYV8TUR5L9XAGR5AHC'

## THE KEYS HAVE TO BE RETRIEVED via LOAD_DOTENV. 
# Uncomment the load_dotenv line and the key setting lines below 
# after commenting the key lines above

load_dotenv('my_api.env')
# Set the variables for the Alpaca API and secret keys
alpaca_api_key = os.getenv('ALPACA_API_KEY')
alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')

#get the alpaca tradeapi object
api = ta.get_alpaca_tradeapi_object(alpaca_api_key, alpaca_secret_key)

crypto = 'BTCUSD'
number_of_shares = 1
buy_or_sell = 'buy'

#do a trade
order_result = ta.submit_crypto_order(api, crypto, buy_or_sell, number_of_shares)

