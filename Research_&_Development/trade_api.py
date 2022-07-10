import pandas as pd
import os
from dotenv import load_dotenv
import trade_api as tradeapi


# you need to open an account at a brokerage to buy/sell shares
# here assumption is that account is open and we are trading on that account
# i m using my alpaca account to do a paper trade in my account

def submit_crypto_order(crypto, buy_or_sell, number_of_shares):

    #load_dotenv('my_api.env')

    ## HARD CODING FOR NOW..FOR AWS LAMBDA..JUST SO I CAN TEST
    ## HAS TO BE CHANGED TO DO A LOADENV

    alpaca_secret_key='QrWTvuqjdWDgx7Klqe5iWIR8K5iESy6DFugfV4Xy'
    alpaca_api_key='PKSYV8TUR5L9XAGR5AHC'

    # Set the variables for the Alpaca API and secret keys
    #alpaca_api_key = os.getenv('ALPACA_API_KEY')
    #alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')

    # Create the Alpaca tradeapi.REST object
    # YOUR CODE HERE
    api = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        #api_version='v2'
        'https://paper-api.alpaca.markets'
    )


    # Submit a market order to buy 1 share of Apple at market price

    order_result= api.submit_order(
        symbol=crypto,
        qty=number_of_shares,
        side=buy_or_sell,
        type='market',
        time_in_force='gtc'
    )
    return order_result

