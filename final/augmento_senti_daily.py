import pandas as pd
import requests
from pathlib import Path
import json
import datetime
import numpy as np
import os
from datetime import datetime, date, timedelta

import matplotlib.pyplot as plt
# Import ClusterCentroids from imblearn
from imblearn.under_sampling import ClusterCentroids
from sklearn.metrics import confusion_matrix,classification_report


#ashok private libraries
import load_data as ld
import twitter_lib as tl
import wsj_lib as wsj
import ml_lib as ml



    

def daily_augmento_senti():
  
    
    
    # get the sentiment for the day
    prefix='btc'  # used for creating file name
    coin_ticker='BTC-USD'
    source = 'twitter'      # for augmento
    coin = 'bitcoin'       # used in Augmento 
    num_of_periods = 100   # 100 days  usedin Augmento
    bin_size='24H'          #default bin size for Augmento

    # used by Augmento and Yahoo Finance Apis
    start= '2022-06-06T00:00:00Z'
    end = '2022-06-07T00:00:00Z'

    # Get sentiment from twitter/ reddit data obtained from augmento site 
    sentiment_df_1 = tl.get_crypto_sentiment_from_augmento(source, coin, num_of_periods, start, end, bin_size)

    # get the sum of the sentiment data for the day
    sentiment_df_1['Senti_Sum'] = sentiment_df_1.sum(axis=1)

    #seperate bullish & Bearish sentiments into 2 df
    bearish=sentiment_df_1[[ 'Bearish', 'Pessimistic/Doubtful', 'Sad', 'Fearful/Concerned', 'Angry', 'Mistrustful', 'Panicking', 'Annoyed/Frustrated']]
    bullish=sentiment_df_1[[ 'Hopeful','Bullish', 'Optimistic', 'Happy', 'Euphoric/Excited']]


    #sum each sentiment df
    bearish['Bear_sum'] = bearish.sum(axis=1)
    bullish['Bull_sum']=bullish.sum(axis=1)

    #add the summations back to the general sentiment_df
    sentiment_df_1['Bear_sum'] = bearish['Bear_sum']
    sentiment_df_1['Bull_sum'] = bullish['Bull_sum']

    #sentiment_of_the_day = sum of all bullish -  sum of all bearish
    sentiment_df_1['Day_Sent'] = sentiment_df_1['Bull_sum'] - sentiment_df_1['Bear_sum']


    #load yahoo crypto data
    # get the coin price for the day
    df_coin= ld.load_from_yahoo([coin_ticker], start,end)

    #join the sentiment & crypto price of the day
    joined_df = sentiment_df_1.join(df_coin[coin_ticker]['close'])
    
    #joined_df['daily_ret']=joined_df['close'].pct_change()

    #create signals
    #joined_df['signal'] = 0.0
    #joined_df.loc[(joined_df['daily_ret'] >= 0), 'signal'] = 1
    #joined_df.loc[(joined_df['daily_ret'] < 0), 'signal'] = -1

    #calculate the pct_change of the sentiment for today

    sentiment_per = joined_df['Day_Sent'] / joined_df['Senti_Sum']
    
    senti_per = sentiment_per.iloc[0]


    return senti_per