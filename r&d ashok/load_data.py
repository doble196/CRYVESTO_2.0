import pandas as pd

import pandas_datareader as pdr
import datetime as dt
import yfinance as yf
import os
import alpaca_trade_api as tradeapi


def load_from_yahoo(tickers, start, end) :

    #start = dt.datetime(2016, 1, 1) -example dates
    #end = dt.datetime(2022, 5, 2)
    #DATA FORMATTING FOR MC Simulation was giving problem, so instead of fetching data in one scoop,
    #did a for loop and constructed the concatanated dataframe as required by MCS
    df=[]
    for tkr in tickers:
        df.append(pdr.get_data_yahoo(tkr, start, end))
    
    portfolio_organized_df = pd.concat(df, axis=1, keys=tickers)
    portfolio_organized_df.rename(columns={'High':'high','Low':'low','Open':'open','Close':'close', 'Volume':'volume', 'Adj Close':'adj close'}, inplace=True)
    
    return portfolio_organized_df

#   
#   For ALPACA 
#   start_date = pd.Timestamp('2021-04-13', tz='America/New_York').isoformat()
#   end_date = pd.Timestamp('2022-04-13', tz='America/New_York').isoformat()

def load_from_alpaca(tickers, start_date, end_date):

# Set the variables for the Alpaca API and secret keys
    alpaca_api_key = os.getenv('ALPACA_API_KEY')
    alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')
    
    # Create the Alpaca tradeapi.REST object
    # YOUR CODE HERE
    
    alpaca_rest_obj = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version='v2'
    )
    
# Set timeframe to 1Day
    timeframe='1Day'
    max

# Format current date as ISO format
# Set both the start and end date at the date of your prior weekday 
# This will give you the closing price of the previous trading day
# Alternatively you can use a start and end date of 2020-08-07

# in GET_BARS Set number of rows to 1000 to retrieve the maximum amount of rows=> limit = max_rows
#setting the rows to 1000 was resulting in the the dataframe with a lot of NaNs. And, running the simulation gave the 30 years returns dataframe with all 1s!!
#I played with this number and with numbers below 1500 or so it was doing this. so I put the number at 3000 just so I could run properly.
    max_rows=10000

#    start_date = pd.Timestamp('2021-04-13', tz='America/New_York').isoformat()
#    end_date = pd.Timestamp('2022-04-13', tz='America/New_York').isoformat()

    portfolio_df = alpaca_rest_obj.get_bars(
        tickers,
        timeframe,
        start=start_date,
        end=end_date,
        limit=max_rows
    ).df

# Reorganize the DataFrame
# Separate ticker data
    df=[]
    for tkr in tickers:
            df.append(portfolio_df[portfolio_df['symbol']==tkr].drop('symbol', axis=1))
    
# Concatenate the ticker DataFrames

    portfolio_organized_df = pd.concat(df, axis=1, keys=tickers)
    portfolio_organized_df.index = portfolio_organized_df.index.date

    

# Review the first 5 rows of the Alpaca DataFrame
# YOUR CODE HERE
    portfolio_organized_df.tail()
    return portfolio_organized_df
