# Project_2 Streamlit Application
#### Issues Im having. Session state is storing the values in the keys.  However, when I buy or sell it subtracts or adds from the original crypto holdings amount.  Try to buy 5 crypto, then sell the same 5 crypto and view the results.  You will see what Im troubleshooting.  Anyways we can add visuals for your data, an interactive dataframe that Lucas Manning shared.  

from turtle import onclick
import streamlit as st
import time
import yfinance as yf
#import AshokData

import pandas as pd
import os
#from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# our private library alpaca_trade_lib.py which does the trading using alpaca. 

import alpaca_trade_lib as ta

def trade_crypto(coin, amount, buy_sell):
# comment these after uncommenting loadenv 
    alpaca_secret_key='QrWTvuqjdWDgx7Klqe5iWIR8K5iESy6DFugfV4Xy'
    alpaca_api_key='PKSYV8TUR5L9XAGR5AHC'

## THE KEYS HAVE TO BE RETRIEVED via LOAD_DOTENV. 
# Uncomment the load_dotenv line and the key setting lines below 
# after commenting the key lines above

#    load_dotenv('my_api.env')
# Set the variables for the Alpaca API and secret keys
#    alpaca_api_key = os.getenv('ALPACA_API_KEY')
#    alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')

#get the alpaca tradeapi object
    api = ta.get_alpaca_tradeapi_object(alpaca_api_key, alpaca_secret_key)

# buy coin(s)

    if coin == 'BTC': crypto='BTCUSD'
    if coin == 'ETH': crypto='ETHUSD'

    number_of_shares = amount
    buy_or_sell = buy_sell.lower()
    st.write('NUM OF SHARES '+ str(number_of_shares))
    st.write('BUY_SELL '+buy_sell)

    st.write("CRYPTO is "+ crypto)

#do a trade
    try:
        order_result = ta.submit_crypto_order(api, crypto, buy_or_sell, number_of_shares)
    except Exception as exception:
       st.write (exception)
 
  #if exception.__str__() == 'position does not exist':
   # pos_qty = 0

#see what trade price we got
#print (order_result.client_order_id)
    price = ta.get_my_order_filled_price (api, order_result.client_order_id)
 #  print (f"Purchase price for {number_of_shares} share(s) was USD {price} per share")
    
# Weird but this is how we are returning the value of this function. Thru state variable..
    st.session_state.order_filled_price = price  

    return





st.sidebar.header("Options")
st.sidebar.write("[README](https://github.com/doble196/CRYVESTO_2.0/blob/ashok/r%26d_ashok/README.md)")
st.title("Cryvesto 2.0 Trading App")


email = st.text_input("Please enter your email to access the Cryvesto trading app")


if email == "admin":
    if email == 'admin':
      with st.form("trade_form", clear_on_submit=True):

        btc = yf.Ticker("BTC-USD")
        st.cache(func=btc)
        eth = yf.Ticker("ETH-USD")
        st.cache(func=eth)
        btc_price = btc.info["regularMarketPrice"]
        st.cache(func=btc_price)
        eth_price = eth.info["regularMarketPrice"]
        st.cache(func=eth_price)

        # initial holding
        btc_holdings = 50
        eth_holdings = 1000
        cash_available = 500000

        # retrieve the holdings from last trade
        if 'btc_holdings' in st.session_state: 
            btc_holdings = st.session_state.btc_holdings 
        if 'eth_holdings' in st.session_state:
            eth_holdings = st.session_state.eth_holdings 
        if 'cash_available' in st.session_state:
            cash_available = st.session_state.cash_available
        
        eth_holdings_value = eth_holdings * eth_price
        btc_holdings_value = btc_holdings * btc_price

        account_balance = btc_holdings_value + eth_holdings_value + cash_available

        st.write("The market price of BTC is: ",btc_price)
        st.write("The market price of ETH is: ",eth_price) 
        st.write(f"ETH Holdings: {eth_holdings}  Value: USD {eth_holdings_value:,.2f}") 
        st.write(f"BTC Holdings: {btc_holdings}  Value: USD {btc_holdings_value:,.2f}") 
        st.write("Cash available for trading:", cash_available)

        st.write("Portfolio Total:", account_balance)

        cryptos = st.radio("What crypto do you want to trade today?", ("BTC", "ETH"))
        if cryptos == "BTC":
            market_price = btc_price
        if cryptos == "ETH":
            market_price = eth_price  

        #### Ashok Add import your function here.  We can add visuals. 

        buy_sell = st.radio('Please make a selection for todays trading.',('Buy','Sell'))              
        st.write("How much",cryptos," do you want to trade ?")
        amount = st.number_input("Amount",.0)
        st.write('NUM OF SHARES INPUT '+ str(amount))

        # Check if you have sufficient AMOUNT REQUIRED if WANT TO BUY
        # Check if you have ENOUGH shares, if you want to sell 
        # CHECK BOTH BEFORE PROCEEEDING TO SAVE STATE
        total = amount * market_price            
    
        if (buy_sell == 'Buy') and (total > cash_available):
            st.warning(f"You don't have enough cash available. Current Cash Balance: USD {cash_available}!")

        elif (buy_sell == 'Sell') and (cryptos == 'BTC') and (amount > btc_holdings):
            st.warning(f"You don't have enough Cryptos available to sell. Current BTC Balance: {btc_holdings}!")

        elif (buy_sell == 'Sell') and (cryptos == 'ETH') and (amount > eth_holdings):
            st.warning(f"You don't have enough Cryptos available to sell. Current ETH Balance: {eth_holdings}!")

        elif amount :                   
            if buy_sell == "Buy":                
                if cryptos == "BTC":
                    btc_holdings = btc_holdings + amount
                    st.session_state.btc_holdings = btc_holdings # save the amount to be retrieved for next session
                    cash_available = cash_available - total
                    st.session_state.cash_available = cash_available            
                
                else:
                    eth_holdings = eth_holdings + amount
                    st.session_state.eth_holdings = eth_holdings # save the amount to be retrieved for next session
                    cash_available = cash_available - total
                    st.session_state.cash_available = cash_available
                

            if buy_sell == "Sell":
            
                if cryptos == "BTC":
                    btc_holdings = btc_holdings - amount
                    st.session_state.btc_holdings = btc_holdings # save the amount to be retrieved for next session

                    cash_available = cash_available + total
                    st.session_state.cash_available = cash_available                
                else:
                    eth_holdings = eth_holdings - amount
                    st.session_state.eth_holdings = eth_holdings # save the amount to be retrieved for next session

                    cash_available = cash_available + total
                    st.session_state.cash_available = cash_available
        
            st.write("Your trade in the amount of",total, "has been processed.")                        
            st.session_state.btc_holdings = btc_holdings
            st.session_state.eth_holdings = eth_holdings  

        submitted = st.form_submit_button("Submit")
        if submitted:
            trade_crypto (cryptos, amount, buy_sell)
            order_filled_price = float(st.session_state.order_filled_price )
            if cryptos == 'BTC' : btc_price = order_filled_price
            if cryptos == 'ETH' : eth_price = order_filled_price
            
            eth_holdings_value = eth_holdings * eth_price
            btc_holdings_value = btc_holdings * btc_price
            account_balance = btc_holdings_value + eth_holdings_value + cash_available

            st.write("AFTER THE TRADE:")

            st.write(f"ETH Holdings: {eth_holdings}  Value: USD {eth_holdings_value:,.2f}") 
            st.write(f"BTC Holdings: {btc_holdings}  Value: USD {btc_holdings_value:,.2f}") 
            st.write("Cash available for trading:", cash_available)


            st.write("Portfolio Total:", account_balance)

    
else: 
    st.error("Please enter a valid email")
    st.stop()
    
   
    
    

    


