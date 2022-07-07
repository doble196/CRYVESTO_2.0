# Project 2 - Project Plan

---

## Phase 1 - Discovery & Prototyping

### Get Data
* Research the various sources and find the data
* Prep the data with the following output
     - columns of data 
         * date
         * headline news or 
         * data with various categories - like from Augmento

### Process  the Data
* Process the data for sentiment
     - sentiment analysis

### 
         

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

### TWITTER 

#### BTC - LogisticRegression with Resampling
              precision    recall  f1-score   support

          -1       0.79      0.31      0.45       183
           0       0.22      0.33      0.27        45
           1       0.05      0.38      0.09        13

    accuracy                           0.32       241 
    macro avg      0.35      0.34      0.27       241
    weighted avg   0.65      0.32      0.39       241

#### BTC - SVC Model with Resampling

             precision    recall  f1-score   support

          -1       0.75      0.26      0.38       183
           0       0.16      0.24      0.19        45
           1       0.05      0.38      0.08        13

    accuracy                           0.26       241
    macro avg      0.32      0.30      0.22       241
    weighted avg   0.60      0.26      0.33       241

#### ETH - LogisticRegression with Resampling

              precision    recall  f1-score   support

          -1       0.78      0.22      0.35       171
           0       0.19      0.40      0.26        42
           1       0.11      0.39      0.17        28

    accuracy                           0.27       241
    macro avg      0.36      0.34      0.26       241
    weighted avg   0.60      0.27      0.31       241




#### ETH - SVC Model with Resampling

              precision    recall  f1-score   support

          -1       0.79      0.26      0.39       171
           0       0.22      0.40      0.28        42
           1       0.12      0.46      0.19        28

    accuracy                           0.31       241
    macro avg      0.38      0.38      0.29       241
    weighted avg   0.61      0.31      0.35       241


### REDDIT

#### BTC - LogisticRegression with Resampling

              precision    recall  f1-score   support

          -1       0.86      0.25      0.39       189
           0       0.24      0.52      0.32        31
           1       0.10      0.57      0.17        21

    accuracy                           0.32       241
    macro avg      0.40      0.45      0.30       241
    weighted avg   0.71      0.32      0.36       241



#### BTC - SVC Model with Resampling

              precision    recall  f1-score   support

          -1       0.91      0.28      0.43       189
           0       0.27      0.39      0.32        31
           1       0.11      0.71      0.19        21

    accuracy                           0.33       241
    macro avg      0.43      0.46      0.31       241
    weighted avg   0.76      0.33      0.39       241


#### ETH - LogisticRegression with Resampling

              precision    recall  f1-score   support

          -1       0.62      0.18      0.28       168
           0       0.23      0.49      0.31        43
           1       0.08      0.27      0.12        30

    accuracy                           0.24       241
    macro avg      0.31      0.31      0.24       241
    weighted avg   0.49      0.24      0.26       241


#### ETH - SVC Model with Resampling

              precision    recall  f1-score   support

          -1       0.68      0.19      0.30       168
           0       0.21      0.35      0.26        43
           1       0.10      0.40      0.16        30

    accuracy                           0.24       241
    macro avg      0.33      0.31      0.24       241
    weighted avg   0.52      0.24      0.27       241


### Neural Network Training and Test

The neural netwok testing with various neural networks also didn't coem up with any dependable results. See the csv files attached