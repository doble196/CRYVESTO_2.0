import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import yfinance as yf
import hvplot.pandas
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
#%matplotlib inline
import panel as pn
import questionary
import os

from dotenv import load_dotenv
#from MCForecastTools import MCSimulation

def sanitize_date(date):
    return pd.to_datetime(date).dt.date

# Get Data from a source. The sources can be any api's that return pandas Dataframes. Using Yahoo as source for phase 1 
# But provision is there for other api's. The Arguments for the get_data function are:
# - ticker : the symbol or symbols
# - start : start date
# - end : end date
# - source: 'Yahoo'/'y/'Y' for now, can be any other, but code need be added for them
# pct_change: True (Default) - if you want cleaned data with NaNs removed and pct_change() format. 
#           : False - if want raw data.
# 

def get_data(ticker, start, end, source='Yahoo', pct_change=True):
    if source=="" or source=='Yahoo' or source == 'y' or source == 'Y':
        if pct_change==False:
            return pdr.get_data_yahoo(ticker, start, end)
        else:
            return pdr.get_data_yahoo(ticker, start, end).dropna().pct_change() # had to do dropna first bec of poor data
    else:
        print(f"The data source {source} is not yet implemented")
        return None

# To Analyze and Plot the returns 
# Arguments-
# - title : the title of the plot
# - daily_ret: dataframe to plot
# - xcol : title of x-axis
# - plot_type: H/h/d/D - for Historical/daily returns
#           : C/c/Cumulative for cumulative Returns 
# used rolling window 0f 60
#
#def analyze_and_plot(title, daily_ret, xcol, ycol, plot_type):
def analyze_and_plot(title, daily_ret, xcol, plot_type):

    #PLOT TYPE - Historical or Dailiy Returns
    if plot_type=='H' or plot_type=='h' or plot_type == 'D' or plot_type == 'd':
        x= daily_ret.rolling(window=60).mean().hvplot(
            title = title,
            xlabel = xcol, 
            width = 700
            )
        return x
    elif plot_type=='C' or plot_type=='c' or plot_type == 'Cumulative':
        cumulative_returns = (1 + daily_ret).cumprod() -1
        x= cumulative_returns.rolling(window=60).mean().hvplot(
            title = title,
            xlabel = xcol, # lambda x: if xcol!=None: x=xcol,
            width = 700
        )
        return x
    
#Get Beta factor for a Ticker. The arguments are:
# df1: the ticker dataframe close column 
# df2: the mkt(or any other) dataframe 'close' column
#Example -get_beta(df['Close']['BTC-USD'], df['Close']['ETH-USD'])

def get_beta(df1, df2):
    return df1.cov(df2) / df2.var()
          # df - daily return data frame for the security..we pass the Close column or Adj Close as param, 

    
# Get Sharpe Ratio for a Ticker symbol. The argument is:
# df - the ticker dataframe 'close' or 'Adj close' column
# e.g. get_sharpe(dailyret['Adj Close'])

def get_sharpe(df):
    year_trading_days = 252
    average_annual_return = df.mean()* year_trading_days
    std_dev = df.std()
    annualized_std = std_dev * np.sqrt(year_trading_days)
    sharpe_ratio = average_annual_return / annualized_std
    return sharpe_ratio
    
#Do the Risk Return Analysis: Here the function does the Sharpe Ratios for the crypto tickers selected and for
# each selected crypto it does beta calculations against the Funds selected.
#Arguments:
# - tickers_crypto: crypto tickers selected
# - etfs: ETF tickers selected
# - etf_list: list of funds
# - start: start date for historical data
# - end: end date for historical data

def do_risk_return_analysis(tickers_crypto, etfs, etf_list, start, end):
    print(f'Now, doing the Risk-Return Analysis on {tickers_crypto}  CRYptos..!\n ')
    
    #start = dt.datetime(2017, 1, 1)
    #end = dt.datetime(2022, 1, 1)
    
    for ticker in tickers_crypto:
        df1= get_data(ticker, start, end)

    #etfs=['SPY', 'IYW', 'QQQ', 'RYT', 'IETC', 'IWM', 'BND','ARKK','RPV']
        x=get_sharpe(df1['Close'])
        print('______________________________________________________________________________________')

        print (f"\nThe Risk Adjusted Return for {ticker} is ...{x}")
    
        print(f'The Returns of {ticker} against {etfs}, i.e. Betas against various ETFs, are...\n')
        j=0
        for i in etfs:

            df2=get_data(i, start, end)
            b=get_beta(df1['Close'],df2['Close'])
            print (f'{i}\t{etf_list[i]}\t{b:.2f}')
            j+=1
        
        print('______________________________________________________________________________________')

        resp=questionary.text("Press ENTER when ready to proceed further..").ask()
    #cp=analyze_and_plot('Cumulative Returns', df1, xcol='Date', plot_type='c')
    # hvplot.show(cp)
    #Removed the code to do the plotting as hvplot couldn't return control back to the porgram

