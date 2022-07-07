#import pandas as pd
import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi


# you need to open an account at a brokerage to buy/sell shares
# here assumption is that account is open and we are trading on that account
# i m using my alpaca account to do a paper trade in my account

# comment these after uncommenting loadenv 
    #alpaca_secret_key='QrWTvuqjdWDgx7Klqe5iWIR8K5iESy6DFugfV4Xy'
    #alpaca_api_key='PKSYV8TUR5L9XAGR5AHC'

    ## THE KEYS HAVE TO BE RETRIEVED via LOAD_DOTENV. 
    # Uncomment the load_dotenv line and the key setting lines below 
    # after commenting the key lines above

    #load_dotenv('my_api.env')
    # Set the variables for the Alpaca API and secret keys
    #alpaca_api_key = os.getenv('ALPACA_API_KEY')
    #alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')


def get_alpaca_tradeapi_object(alpaca_api_key='PKSYV8TUR5L9XAGR5AHC', alpaca_secret_key='QrWTvuqjdWDgx7Klqe5iWIR8K5iESy6DFugfV4Xy'):

    ## Made default - my keys, you canprovide yours.

    # Create the Alpaca tradeapi.REST object
    # YOUR CODE HERE
    return tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        #api_version='v2'
        'https://paper-api.alpaca.markets'
    )


def submit_crypto_order(api, crypto, buy_or_sell, number_of_shares):

    # Submit a market order to buy/sell  sharees of crypto at market price

    order_result= api.submit_order(
        symbol=crypto,
        qty=number_of_shares,
        side=buy_or_sell,
        type='market',
        time_in_force='gtc' #good to cancel
    )
    return order_result


def get_list_of_closed_orders(api, crypto, limit=100):
    # Get the last 100 of our closed orders
    closed_orders = api.list_orders(
    status='closed',
    limit=limit,
    nested=True  # show nested multi-leg orders
    )

    # Get only the closed orders for a particular stock
    closed_crypto_orders = [o for o in closed_orders if o.symbol == crypto]
    return closed_crypto_orders

def get_my_order_filled_price (api, client_order_id):
    my_order = api.get_order_by_client_order_id(client_order_id)
    return my_order.filled_avg_price


