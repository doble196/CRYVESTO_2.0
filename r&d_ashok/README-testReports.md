# Project 2 - Project Plan

---

## ML MODEL TEST/TRAIN REPORTS
---

## CHANGED THE WAY WE GET SIGNAL TO SIMPLE > 0 implying by, <0 sell

## WSJ DATA ONLY 
### Short Window = 10, Long Window =100
### LOGISTIC REGRESSION BTC-USD
                precision    recall  f1-score   support

        -1.0       0.43      0.37      0.40        89
         1.0       0.54      0.60      0.57       111

    accuracy                           0.50       200
    macro avg      0.49      0.49      0.49       200
    weighted avg   0.49      0.50      0.49       200


### SVC Model BTC-USD
           precision    recall  f1-score   support

        -1.0       0.47      0.29      0.36        89
         1.0       0.57      0.74      0.64       111

    accuracy                           0.54       200
    macro avg      0.52      0.52      0.50       200
    weighted avg   0.52      0.54      0.52       200

### Short Window = 10, Long Window =100

### LOGISTIC REGRESSION ETH-USD
             precision    recall  f1-score   support

        -1.0       0.43      0.54      0.48        96
         1.0       0.45      0.35      0.39       104

    accuracy                           0.44       200
    macro avg      0.44      0.44      0.44       200
    weighted avg   0.44      0.44      0.43       200

### SVC Model ETH-USD

              precision    recall  f1-score   support

        -1.0       0.44      0.59      0.51        96
         1.0       0.45      0.31      0.37       104

    accuracy                           0.45       200
    macro avg      0.45      0.45      0.44       200
    weighted avg   0.45      0.45      0.43       200


### Short Window = 6, Long Window =100
### LOGISTIC REGRESSION BTC-USD

              precision    recall  f1-score   support

        -1.0       0.49      0.53      0.51        91
         1.0       0.58      0.54      0.56       109

    accuracy                           0.54       200
    macro avg      0.53      0.53      0.53       200
    weighted avg   0.54      0.54      0.54       200

### SVC Model BTC-USD

              precision    recall  f1-score   support

        -1.0       0.50      0.49      0.50        91
         1.0       0.58      0.59      0.58       109

    accuracy                           0.55       200
    macro avg      0.54      0.54      0.54       200
    weighted avg   0.54      0.55      0.54       200


### LOGISTIC REGRESSION ETH-USD
              precision    recall  f1-score   support

        -1.0       0.39      0.41      0.40        88
         1.0       0.52      0.50      0.51       112

    accuracy                           0.46       200
    macro avg      0.45      0.45      0.45       200
    weighted avg   0.46      0.46      0.46       200

### SVC Model ETH-USD
              precision    recall  f1-score   support

        -1.0       0.40      0.38      0.39        88
         1.0       0.53      0.56      0.55       112

    accuracy                           0.48       200
    macro avg      0.47      0.47      0.47       200
    weighted avg   0.48      0.48      0.48       200

### Short Window = 6, Long Window =80
### LOGISTIC REGRESSION BTC-USD


              precision    recall  f1-score   support

        -1.0       0.49      0.44      0.46        96
         1.0       0.53      0.59      0.56       104

    accuracy                           0.52       200
    macro avg      0.51      0.51      0.51       200
    weighted avg   0.51      0.52      0.51       200


### SVC Model BTC-USD

              precision    recall  f1-score   support

        -1.0       0.52      0.40      0.45        96
         1.0       0.54      0.66      0.60       104

    accuracy                           0.54       200
    macro avg      0.53      0.53      0.52       200
    weighted avg   0.53      0.54      0.53       200
    
### LOGISTIC REGRESSION ETH-USD

              precision    recall  f1-score   support

        -1.0       0.45      0.52      0.49        94
         1.0       0.51      0.44      0.47       106

    accuracy                           0.48       200
    macro avg      0.48      0.48      0.48       200
    weighted avg   0.48      0.48      0.48       200

### SVC Model ETH-USD

              precision    recall  f1-score   support

        -1.0       0.46      0.54      0.50        94
         1.0       0.51      0.42      0.46       106

    accuracy                           0.48       200
    macro avg      0.48      0.48      0.48       200
    weighted avg   0.49      0.48      0.48       200




### SEEING IMPROVEMENTS IN THE ACCURACY SCORES AS YOU TUNE THE WINDOWS FOR SMOOTHING OUT



---

## BELOW REPORTS ARE WITH OLDER SIGNAL CREATION LOGIC

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
    
#### ONLY WSJ SENTIMENT 

#### ETH - LogisticRegression with Resampling
              precision    recall  f1-score   support

          -1       0.57      0.02      0.04       209
           0       0.14      0.59      0.22        37
           1       0.09      0.28      0.14        40

    accuracy                           0.13       286
    macro avg      0.27      0.30      0.13       286
    weighted avg   0.45      0.13      0.08       286


#### ETH - SVC Model with Resampling

              precision    recall  f1-score   support

          -1       0.00      0.00      0.00       209
           0       0.14      0.59      0.22        37
           1       0.10      0.33      0.16        40

    accuracy                           0.12       286
    macro avg      0.08      0.31      0.13       286
    weighted avg   0.03      0.12      0.05       286

### ONLY TWITTER SENTIMENT

#### ETH - LogisticRegression with Resampling

              precision    recall  f1-score   support

          -1       0.69      0.24      0.36       174
           0       0.18      0.34      0.24        41
           1       0.20      0.63      0.30        35

    accuracy                           0.31       250
    macro avg      0.36      0.40      0.30       250
    weighted avg   0.54      0.31      0.33       250

#### ETH - SVC Model with Resampling

              precision    recall  f1-score   support

          -1       0.62      0.20      0.30       174
           0       0.17      0.34      0.23        41
           1       0.18      0.60      0.28        35

    accuracy                           0.28       250
    macro avg      0.33      0.38      0.27       250
    weighted avg   0.48      0.28      0.28       250

#### BTC - LogisticRegression with Resampling

              precision    recall  f1-score   support

          -1       0.90      0.21      0.34       207
           0       0.10      0.40      0.16        25
           1       0.08      0.44      0.13        18

    accuracy                           0.25       250
    macro avg      0.36      0.35      0.21       250
    weighted avg   0.76      0.25      0.31       250

#### BTC - SVC Model with Resampling

              precision    recall  f1-score   support

          -1       0.87      0.23      0.37       207
           0       0.11      0.32      0.17        25
           1       0.06      0.39      0.10        18

    accuracy                           0.25       250
    macro avg      0.35      0.31      0.21       250
    weighted avg   0.74      0.25      0.33       250



### ONLY REDDIT SENTIMENT

#### ETH - LogisticRegression with Resampling
             precision    recall  f1-score   support

          -1       0.72      0.19      0.30       177
           0       0.14      0.31      0.20        36
           1       0.14      0.49      0.22        37

    accuracy                           0.25       250
    macro avg      0.34      0.33      0.24       250
    weighted avg   0.55      0.25      0.28       250

#### ETH - SVC Model with Resampling

             precision    recall  f1-score   support

          -1       0.71      0.17      0.27       177
           0       0.18      0.36      0.24        36
           1       0.15      0.54      0.23        37

    accuracy                           0.25       250
    macro avg      0.35      0.36      0.25       250
    weighted avg   0.55      0.25      0.26       250

#### BTC - LogisticRegression with Resampling
              precision    recall  f1-score   support

          -1       0.80      0.22      0.35       195
           0       0.17      0.41      0.24        37
           1       0.06      0.33      0.09        18

    accuracy                           0.26       250
    macro avg      0.34      0.32      0.23       250
    weighted avg   0.65      0.26      0.31       250



#### BTC - SVC Model with Resampling

              precision    recall  f1-score   support

          -1       0.75      0.22      0.33       195
           0       0.18      0.41      0.25        37
           1       0.04      0.22      0.06        18

    accuracy                           0.24       250
    macro avg      0.32      0.28      0.22       250
    weighted avg   0.61      0.24      0.30       250




### Neural Network Training and Test

The neural netwok testing with various neural networks also didn't coem up with any dependable results. See the csv files attached
[BTC-twitter]('twitter_btc.pdf')
