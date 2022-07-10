import pandas as pd
from pathlib import Path

import nltk
#nltk.download('vader_lexicon') # one time only
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiments_from_wsj():
    vader = SentimentIntensityAnalyzer() # or whatever you want to call it


    df = pd.read_csv('wsj_headlines.csv')
    df = df.drop(columns=['Unnamed: 0'])

    df['scores'] = df['Headline'].apply(lambda headline: vader.polarity_scores(headline))
    df['scores'] = df['scores'].apply(lambda x : x['compound'])

    df = df.groupby(by='Date').mean()

    df ['sentiment'] = df['scores'].apply(lambda x: 'pos' if x > 0 else 'neg' if x < 0 else 'neutral')

    return df