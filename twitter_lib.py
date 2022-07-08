import pandas as pd
import requests
from pathlib import Path
import json
import datetime

import load_data as ld
import os

def get_crypto_sentiment_from_augmento(source, coin, num_of_periods, start, end, bin_size):

    #argument for load_data_from_augmento(coin, num_of_periods, start, end, bin_size='24H')

    #coin = 'bitcoin'
    #num_of_periods = 1000 # 1000 days

    #start="2018-04-01T00:00:00Z"
    #end ="2022-04-30T00:00:00Z"
    #default bin size of 24H, but we will provide ...just..
    #bin_size='24H'

    #get topic list
    r = requests.request("GET", "http://api-dev.augmento.ai/v0.1/topics")
    topics_json = r.json()
    #print('Topics are ', json.dumps(topics_json, indent=4, skipkeys = True, allow_nan = True))
    topic_list = list(topics_json.values())
    #source = 'twitter'

    data=ld.load_data_from_augmento(source, coin, num_of_periods, start, end, bin_size)
    df = pd.DataFrame(data)
    counts_df = pd.DataFrame(df['counts'].tolist(), columns=topic_list)
    counts_df['Date'] = pd.to_datetime(df['datetime']).dt.date
    counts_df = counts_df.groupby(by='Date').mean()
    
    df_sentiments = counts_df[['FOMO', 'Uncertain','Hopeful','Bearish', 'Pessimistic/Doubtful', 'Sad', 'Fearful/Concerned', 'Angry', 'Mistrustful', 'Panicking', 'Annoyed/Frustrated', 'Bullish', 'Optimistic', 'Happy', 'Euphoric/Excited']] 

    #bearish=df_sentiments[[ 'Bearish', 'Pessimistic/Doubtful', 'Sad', 'Fearful/Concerned', 'Angry', 'Mistrustful', 'Panicking', 'Annoyed/Frustrated']]
   # bullish=df_sentiments[[ 'Hopeful','Bullish', 'Optimistic', 'Happy', 'Euphoric/Excited']]

    #bearish['Bear_sum'] = bearish.sum(axis=1)
    #bullish['Bull_sum']=bullish.sum(axis=1)

    #return bearish, bullish
# return counts_df
    return df_sentiments
 #   return df_sentiments, bullish, bearish
    





