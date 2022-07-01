# Project 2 - Cryvesto, Version 2

Utilize ML techniques to build a Crypto stock trading bot. 

---

## User Story
A retail investor is so innundated with world news, business news, political events that he is unable to keep track of how these might impact trading or investments. To help bring some sanity to this process, we are designing a bot which will utilize news data (from sources like **twitter, reddit, The Wall Street Journal, and NewsAPI**) and historical trading data to build an ML model that can predict whether to buy/sell/hold a security based upon current news.  The model is trained with 'sentiment' analysis and related trading data. Given the current news, the trained model will predict whether an investor should buy a stock or not.  

And, finally (if time permits) execute a paper trade upon user confirmation.

---

## Acceptance Criteria  

The Cryvesto bot will use AWS Lex, Lambda and Sagemaker (maybe) and must meet the following criteria:

* TBD

---

## The Application  

The application uses the following steps to build the robo advisor:


### The Trading Bot
The Amazon Lex Bot will engage the user as follows:
1. wanna trade stock? if no, exit.
2. Prompt for a TICKER symbol, validate
3. Inform the User to 'Hang on.. while I analyze..'.  Under the hood ask the MODEL (a Lambda function) for a recommendation
4. Once back with the recommendation, ask if want to trade
5. if yes, use Alpaca Paper Trading to execute a paper trade (another Lambda Function)
6. if no, go back to step 1.

### MODEL

#### Build the model
* Get the data from various sources (wherever possible)- WSJ, NewsAPI, Augmento, Twitter, Reddit etc.
* get the historical headline news data
* save in a dataframe, `headline_df`
* do a sentiment analysis on each headline, add respective columns in the `headline_df`. If we use TextBlob, these columns would be `polarity` and `subjectivity` . I used `polarity` due to TextBlob. We can use anything, like `Augmento` etc.
* get the pricing data for the `ticker` that the user wanted to trade for the historical dates available
* on the `close` price do a `pct_change` and save it in a `returns` column
* calculate the value of `signal` column to trade based upon the `polarity` and `returns`
    - if `polarity` > .5 and `returns` > 0: then set `signal to 1 (BUY )
    - if `polarity` <=5 and `returns` < 0 : then set signal to -1 (SELL)
    - otherwise set signal to 0 (HOLD)
* create `X` variable with `polarity`, `subjectivity` and `returns` columns
* create `y` variable with `signal`
* scale the data
* resample (if needed) - in WSJ case I needed to
* build a model (LogisticRegression or anything else) 
* test 
* Now the model is ready

#### Make a Prediction
* get current news from `NewsAPI` (top 20 news items)
* get the current TICKER price. do a `pct_change` on it
* do a sentiment analysis on the current news items
* do a `mean` on 'polarity` and 'subjectivity`
* pass on these mean values and TICKER pct_change as `X_test` to the model
* let the model Predict
* pass the prediction to the user via the Bot

### Compare with other models

### Trade using Alpaca Paper Trading

---

## Technologies
The application is developed using:  
* Language: Python 3.7,   
* Packages/Libraries: Pandas; AWS Lex, AWS Lambda, AWS Sagemaker  
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
        Project_2    
        
   4. %cd Project_2     

At this point you will have the the entire application files in the current directory as follows (THIS IS JUST A SAMPLE):

    * ageError                        (Test Result screenshot)  
    * bot w lambda                    (bot video)  
    * bot_without_lambda              (bot video)   
    * correctDialog                   (test result screenshot)  
    * incorrectAmt                    (test result screenshot)  
    * negativeAgeError                (test result screenshot)  
    * README.md                       (this file you are reading)  
    * Starter_Code  
        - Lambda  
            - lambda_function.py      (start code that was modified)
        - Test_Events                 (used for testing the Lambda function)
            - ageError.json  
            - correctDialog.json  
            - incorrectAmountError.json  
            - negativeAgeError.json  
       
---

## Usage
The following details the instructions on how to run the application.  

### Setup the environment and Run the application 

In order to run the Bot you will have to log on to the Amazon AWS Console and go through the process of creating the bot and then running the bot with lambda function as detailed above.

---

## Contributors
Ashok Pandey - ashok.pragati@gmail.com, www.linkedin.com/in/ashok-pandey-a7201237  
Dane Hayes - nydane1@gmail.com  
Scott Marler -scottjmarler@gmail.com  
Rensley Ramos -  
Anna Joltaya

---

## License
The source code is the property of the developer. The users can copy and use the code freely but the developer is not responsible for any liability arising out of the code and its derivatives.

---