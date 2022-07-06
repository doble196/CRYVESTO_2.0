# Project_2 Streamlit Application
#### Issues Im having. Session state is storing the values in the keys.  However, when I buy or sell it subtracts or adds from the original crypto holdings amount.  Try to buy 5 crypto, then sell the same 5 crypto and view the results.  You will see what Im troubleshooting.  Anyways we can add visuals for your data, an interactive dataframe that Lucas Manning shared.  

import streamlit as st
import time
import yfinance as yf
#import AshokData


st.sidebar.header("Options")
st.sidebar.write("[README](https://github.com/doble196/CRYVESTO_2.0/blob/ashok/r%26d_ashok/README.md)")
st.title("Cryvesto 2.0 Trading App")


email = st.text_input("Please enter your email to access the Cryvesto trading app")


if email == "admin":
    if email == 'admin':
    #with st.form("trade_form", clear_on_submit=True):

        btc = yf.Ticker("BTC-USD")
        st.cache(func=btc)
        eth = yf.Ticker("ETH-USD")
        st.cache(func=eth)
        btc_price = btc.info["regularMarketPrice"]
        st.cache(func=btc_price)
        eth_price = eth.info["regularMarketPrice"]
        st.cache(func=eth_price)
        btc_holdings = 50
        eth_holdings = 1000
        eth_holdings_value = eth_holdings * eth_price
        btc_holdings_value = btc_holdings * btc_price
        account_balance = btc_holdings_value + eth_holdings_value
        st.write("The market price of BTC is: ",btc_price)
        st.write("The market price of ETH is: ",eth_price) 
        st.write("Funds available for trading:", account_balance)
    
        cryptos = st.radio("What crypto do you want to trade today?", ("BTC", "ETH"))
        
        #### Ashok Add import your function here.  We can add visuals. 

        buy_sell = st.radio('Please make a selection for todays trading.',('Buy','Sell'))  
    
        if 'cryptos' not in st.session_state:
            st.session_state.cryptos = cryptos
        
        if 'account_balance' not in st.session_state:
            st.session_state.account_balance = account_balance    
    
        if 'btc_holdings' not in st.session_state:
            st.session_state.btc_holdings = btc_holdings
        
        if 'eth_holdings' not in st.session_state:
            st.session_state.eth_holdings = eth_holdings
        
        if 'btc_holdings_value' not in st.session_state:
            st.session_state.btc_holdings_value = btc_holdings_value
        
        if 'eth_holdings_value' not in st.session_state:
            st.session_state.eth_holdings_value = eth_holdings_value

        if 'btc_price' not in st.session_state:
            st.session_state.btc_price = btc_price
            
        if 'eth_price' not in st.session_state:
            st.session_state.eth_price = eth_price
             
        if 'buy_sell' not in st.session_state:
            st.session_state.buy_sell = buy_sell
            
        
            
        if cryptos:
        
            if cryptos == "BTC":
                market_price = btc_price
                st.session_state.cryptos = cryptos
                
            if cryptos == "ETH":
                market_price = eth_price  
                st.session_state.cryptos = cryptos
    
        if buy_sell:
            
            st.write("How much",cryptos," do you want to trade ?")
            st.session_state.buy_sell = buy_sell
            amount = st.number_input("Amount",.0)
            total = amount * market_price
            st.session_state.amount = amount
            
    
        if 'total' not in st.session_state:
            st.session_state.total = total
        if 'amount' not in st.session_state:
            st.session_state.amount = amount
    
        if amount:
                    
            if buy_sell == "Buy":
                account_balance = account_balance - total
                
                if account_balance <= 0:
                    st.error("Transaction cannot be completed. Negative Account Balance")
                    account_balance
                elif cryptos == "BTC":
                    btc_holdings = btc_holdings + amount
                    st.session_state.btc_holdings = btc_holdings
                    
            
                else:
                    eth_holdings = eth_holdings + amount
                    st.session_state.eth_holdings = eth_holdings
                    
            
            if buy_sell == "Sell":
                account_balance = account_balance + total
                
                
                if cryptos == "BTC":
                    if btc_holdings < amount:
                        st.error("Transaction cannot be completed.")
                        st.stop()
                    else: 
                        btc_holdings = btc_holdings - amount
                        btc_holdings_value = btc_holdings * btc_price
                             
                        
                if cryptos == "ETH":
                    if eth_holdings < amount:
                        st.error("Transaction cannot be completed.")
                        st.stop()
                    else:
                        eth_holdings = eth_holdings - amount
                        eth_holdings_value = eth_holdings * eth_price
                        
                        
        submitted = st.form_submit_button("Submit")
        if submitted:                
            st.write("Your trade in the amount of",total, "has been processed.")                        
            st.session_state.buy_sell = buy_sell
            st.session_state.total = total
            st.session_state.account_balance = account_balance
            st.session_state.btc_holdings_value = btc_holdings_value
            st.session_state.eth_holdings_value = eth_holdings_value
            st.session_state.btc_holdings = btc_holdings * amount
            st.session_state.eth_holdings = eth_holdings * amount
            st.session_state.amount = amount    
            st.session_state.btc_price = btc_price
            st.session_state.eth_price = eth_price 
            
    st.write("Your account balance is:", account_balance)
    st.write("You own",btc_holdings,"Bitcoin")
    st.write("You own",eth_holdings,"Ethereum")
    
    #st.write(st.session_state)    
        
    
else: 
    st.error("Please enter a valid email")
    st.stop()
    
   
    
    

    


