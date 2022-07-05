# Project_2 Streamlit Application

import streamlit as st
import time
import yfinance as yf


    
st.sidebar.header("Options")
st.sidebar.write("[README](https://github.com/doble196/CRYVESTO_2.0/blob/ashok/r%26d_ashok/README.md)")
st.title("Cryvesto 2.0 Trading App")


email = st.text_input("Please enter your email to access trading app")


btc_price = 19684.984
eth_price = 1101.454



            
                 


if email == "user_1@gmail.com":
    
    btc_holdings = 50
    eth_holdings = 1000
    eth_holdings_value = eth_holdings * eth_price
    btc_holdings_value = btc_holdings * btc_price
    account_balance = btc_holdings_value + eth_holdings_value
    st.write("The market price of BTC is: ",btc_price)
    st.write("The market price of ETH is: ",eth_price) 
    st.write("Funds available for trading:", account_balance)
    
    
    with st.form("cryvesto",clear_on_submit=True): 
        
        cryptos = st.radio("What crypto do you want to trade today?", ("BTC", "ETH"))
        b_s_h = st.radio('Please make a selection for todays trading.',('Buy','Sell','Hold'))  
    
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
             
        if 'b_s_h' not in st.session_state:
            st.session_state.b_s_h = b_s_h
            
        if cryptos:
            st.session_state.cryptos = cryptos
            if cryptos == "BTC":
                market_price = btc_price
                
            if cryptos == "ETH":
                market_price = eth_price  
   
        if b_s_h:
            if b_s_h == "Hold":
                st.write("Holding all positions soldier!")
                st.session_state.b_s_h = b_s_h
                st.stop()
            else:
                st.write("How much",cryptos," do you want to ",b_s_h, "?")
                st.session_state.b_s_h = b_s_h
                amount = st.number_input("Amount",.0)
                total = amount * market_price
    
        if 'total' not in st.session_state:
            st.session_state.total = total
    
        if amount:
                    
            if b_s_h == "Buy":
                account_balance = account_balance - total
                if account_balance <= 0:
                    st.error("Transaction cannot be completed. Negative Account Balance")
                    account_balance
                if cryptos == "BTC":
                    btc_holdings = btc_holdings + amount
                else:
                    eth_holdings = eth_holdings + amount
            
            if b_s_h == "Sell":
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
                        
        st.write("Your trade in the amount of",total, "has been processed.")                 
        
     
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.cryptos = cryptos            
            st.session_state.b_s_h = b_s_h
            st.session_state.total = total
            st.session_state.account_balance = account_balance
            st.session_state.btc_holdings = btc_holdings
            st.session_state.eth_holdings = eth_holdings
            st.session_state.btc_holdings_value = btc_holdings_value
            st.session_state.eth_holdings_value = eth_holdings_value
            st.session_state.btc_price = btc_price
            st.session_state.eth_price = eth_price 
    st.write("Your account balance is:", account_balance)
    st.write("You own",btc_holdings,"Bitcoin")
    st.write("You own",eth_holdings,"Ethereum")
        
        
        
            
            
#likes = []
    #like = st.checkbox("Do you like this app?")
    #if like:
    #    st.write("Thanks!")
        
        
 
    
    
    
else: 
    st.error("Please enter a valid email")
    st.stop()
    
   
    
    

    


