# Project 2 - Cryvesto 2.0 - A Machine Learning to Trade Cryptos Utilizing Social Media Sentiments
Build a Crypto stock trading App that learns to trade keeping in mind the sentiments derived out of Social Media and News feed.

---
## Hypothesis
Social Media and News sentiments are a significant factor in trading securities, especially Cryptocurrencies.

___

## User Story
A retail investor is so innundated with world news, business news, political events that he is unable to keep track of how these might impact trading or investments. 

Team Cryvesto has embarked upon building a Machine Learning(ML) Sentiment Trade Bot(STB) that utilizes market sentiment from news and social media sources that responds to ‘Bullish’ or ‘Bearish’ signals. These signals trigger an entry or exit point to trade targeted securities or assets.  We believe that our hypothesis highlights the importance of ‘fear’ and ‘greed’ that influences market forces, which could be some of the leading indicators for trade points.

Team Cryvesto will utilize sentiments from news data (from sources like **twitter, reddit, The Wall Street Journal, and NewsAPI**) and historical trading data to build a STB utilizing ML techniques that can predict whether to buy/sell/hold a Cryptocurrency.  

First, the hypothesis that these sentiments are significant factors as trade signals will be established after testing the hypothesis against several ML models, followed by building a STB using the selected ML model.

---

## Acceptance Criteria  

The Cryvesto project must meet the following criteria:

* Establish the validity of the Hypothesis using sentiment feeds from Twitter and Reddit for Bitcoin and Ethereum Cryptocurrencies and testing with the following ML Models:
    - Logistic Regression
    - SVC
    - AdaBoost
    - Random Forest  
* Establish the validity of the Hypothesis using general news setiment from Wall Street Journal and testing with the following ML Models:
    - Logistic Regression
    - SVC
    - AdaBoost
    - Random Forest   
* Determine the ML model that performs the best with over atleast 50% accuracy and recall rates for prediciting the buy/sell signals  
* Using the selected model, build the Cryvesto 2.0 app utilizing **Streamlit** that:
    - displays the sentiment of the day in a Speedometer like format
    - Prompts the user to select from Bitcoin/ Ethereum for trading
    - Perform a paper trade using Alpaca Trade API   

---

## Testing the Hypothesis

### Testing using crypto related sentiments from leading social media sites
* Developed the `mainline_twitter` Jupyter Notebook  
    - drawing sentiments from twitter feed related to
        - Bitcoin
        - Ethereum
    - obtained historical Ticker data from Yahoo Finance
    - tested on the follwoing models
       - Logistic Regression
       - SVC
       - AdaBoost
       - Random Forest
    - accumulated `Classification reports` in a results DataFrame and subsequently in a `csv` file for comparison purposes
    - saved `Actual Vs Strategy Returns` plots in respective PNG files for comparison purposes  

* Developed the `mainline_reddit` Jupyter Notebook  
    - drawing sentiments from reddit feed related to
        - Bitcoin
        - Ethereum
    - obtained historical Ticker data from Yahoo Finance
    - tested on the follwoing models
       - Logistic Regression
       - SVC
       - AdaBoost
       - Random Forest
    - accumulated `Classification reports` in a results DataFrame and subsequently in a `csv` file for comparison purposes
    - saved `Actual Vs Strategy Returns` plots in respective PNG files for comparison purposes  
                

### Testing using headlines from the leading business newspaper- Wall Street Journal
* Developed the `mainline_wsj` Jupyter Notebook  
    - drawing sentiments from historical `Wall Street Journal` news Headlines 
    - obtained historical Ticker data from Yahoo Finance
    - invented  our own proprietary signal strategy called **Simple Moving Average of Sentiments** akin to generally known SMAs which utilize daily returns. In our **SMA of Sentiments** we utilize the sentiment values averaged over a short period of time (SMA-Short), and over a longer period of time (SMA-Long). We used SMA short and SMA Long as the Feature set for our ML models.  We tested the models with and without this strategy and very interestingly the results with the SMA strategy were much better. 
    - tested on the follwoing models
       - Logistic Regression
       - SVC
       - AdaBoost
       - Random Forest
    - accumulated `Classification reports` in a results DataFrame and subsequently in a `csv` file for comparison purposes
    - saved `Actual Vs Strategy Returns` plots in respective PNG files for comparison purposes
    - tested with current top 20 headlines extracted from NewsAPI API

## Hypothesis Test Results

The test showed promising results favoring `AdaBoost` model with about 60% accuracy in predicting buy/sell indicators when tested with social media sentiment feeds. See [twitter classification reports](twitter_classification_reports.pdf) and [reddit classification reports](reddit_classification_reports.pdf) here.

We got similar results with over 50% accuracy with the news headlines from The Wall Street Journal. [Click here for WSJ classification report](classification_reports_wsj.pdf). We believe that with fine tuning of SMA windows we might be able to get better results indicating that even the leading business news headlines have similar impact on trading. This is promising!


## Cryvesto 2.0 Trading App
The App is built using **Streamlit**.



---

## Technologies
The application is developed using:  
* Language: Python 3.7,   
* Packages/Libraries: Pandas; Streamlit, ClusterCentroids, StandardScaler, LogisticRegression, AdaBoostClassifier, RandomForestClassifier 
* Development Environment: VS Code and Terminal, Anaconda 2.1.1 with conda 4.11.0, Jupyterlab 3.2.9
* OS: Mac OS 12.1

---
## Installation Guide
Following are the instructions to install the application from its Github respository.  

### Clone the application code from Github as follows:
copy the URL link of the application from its Github repository      
open the Terminal window and clone as follows:  

   1. %cd to_your_preferred_directory_where_you want_to_store_this_application  
    
   2. %git clone URL_link_that_was_copied_in_step_1_above   
    
   3. %ls     
        CRYVESTO_2.0    
        
   4. %cd CRYVESTO_2.0    

At this point you will have the the entire application files in the current directory as follows:

* alpaca_trade_lib.py       (Alpaca trade lib)
* classification_reports_wsj.pdf
* classification_reports.csv
* load_data.py              (load api library)
* mainline_reddit.ipynb     (reddit feed notebook)
* mainline_twitter.ipynb    (twitter feed notebook)
* mainline_wsj.ipynb        (wsj data notebook)
* ml_lib.py                 (ml library)
* my_api.env          
* newslib.py                (newsapi lib)
* Pipfile
* README.md
* reddit_classification_reports.csv  
* reddit_classification_reports.pdf
* results with reddit data only
* results with twitter data only
* results wsj data only
* trade_api.py             (alpaca order api)
* trade.ipynb
* twitter_classification_reports.csv
* twitter_classification_reports.pdf
* twitter_lib.py            (social media lib)
* wsj_headlines.csv         (wsj headlines hitorical data)
* wsj_lib.py                (wsj lib)
* xactcryptos.py
    
---

## Usage
The following details the instructions on how to run the application.  

### Setup the environment and Run the application 

Setup the environment using conda as follows:

    5. %conda create dev -python=3.7 anaconda  
    
    6. %conda activate dev  
    
    7. %jupyter lab  

### Run the Notebooks
THIS ASSUMES FAMILIARITY WITH JUPYTER LAB. If not, then [click here for information on Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/).  

After step 7 above, this will take you to the jupyter lab window, where you can open the application notebook **mainline_twitter.ipynb, or mainline_reddit.ipynb, or mainline_wsj.ipynb** and run the notebook to test the hypothesis with respective data source.  

### Run the Cryvest 2.0 App


---

---

## Contributors
Ashok Pandey - ashok.pragati@gmail.com, www.linkedin.com/in/ashok-pandey-a7201237  
Dane Hayes - nydane1@gmail.com  
Scott Marler - scottjmarler@gmail.com  
Rensley Ramos - ranly196@gmail.com  
Anna Joltaya 

---

## License
The source code is the property of the developer. The users can copy and use the code freely but the developer is not responsible for any liability arising out of the code and its derivatives.

---

