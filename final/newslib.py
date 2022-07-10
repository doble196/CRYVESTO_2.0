import pandas as pd
import requests 
from textblob import TextBlob
from pathlib import Path

import nltk
#nltk.download('vader_lexicon') # one time only
from nltk.sentiment.vader import SentimentIntensityAnalyzer

 
#Get current Headlines for US.. You can get any country by specifying the country code
def getCurrentHeadlines_TextBlob():
     
    # news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      #"source": "bbc-news",
      "country":'us',
      "sortBy": "top",
      "apiKey": "408bc0e41ad1474581aadc918b65e44e"
    }
    main_url = " https://newsapi.org/v2/top-headlines"
 
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_news_page = res.json()
 
    # getting all articles in a string article . actually a DICT
    article = open_news_page["articles"]
        
    # empty list which will
    # contain all trending news
    results = []
    pola=[]
    subj=[]
    

    for ar in article:
        results.append(ar["title"])
        pol, sub = TextBlob(ar['title']).sentiment
        pola.append(pol)
        subj.append(sub)
    
    pol_subj_df = pd.DataFrame({})
    pol_subj_df['pola']= pola
    pol_subj_df['subj']= subj
    '''
    for i in range(len(results)):
         
        # printing all trending news
        print(i + 1, results[i])'''
     
    return pol_subj_df, results

def get_headlines_from_newsapi():
    
    # news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      #"source": "bbc-news",
      "country":'us',
      "sortBy": "top",
      "apiKey": "408bc0e41ad1474581aadc918b65e44e"
    }
    main_url = " https://newsapi.org/v2/top-headlines"
 
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_news_page = res.json()
 
    # getting all articles in a string article . actually a DICT
    article = open_news_page["articles"]
    
    df = pd.DataFrame(article)
    
    vader = SentimentIntensityAnalyzer() # or whatever you want to call it


    

    df['scores'] = df['title'].apply(lambda headline: vader.polarity_scores(headline))
    df['scores'] = df['scores'].apply(lambda x : x['compound'])


    #df ['sentiment'] = df['scores'].apply(lambda x: 'pos' if x > 0 else 'neg' if x < 0 else 'neutral')

    return df['scores'].mean()
     