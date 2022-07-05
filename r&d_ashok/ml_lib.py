# Imports
import pandas as pd
import numpy as np
from pathlib import Path
import hvplot.pandas
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from pandas.tseries.offsets import DateOffset
from sklearn.metrics import classification_report


def create_train_test_dataframes(X, y, training_begin, training_end):

    # Generate the X_train and y_train DataFrames
    X_train = X.loc[training_begin:training_end]
    y_train = y.loc[training_begin:training_end]

    # Generate the X_test and y_test DataFrames
    X_test = X.loc[training_end+DateOffset(hours=1):]
    y_test = y.loc[training_end+DateOffset(hours=1):]
    return X_train, y_train, X_test, y_test

# Scale the features DataFrames
def scale_features_df(X_train, X_test):
    # Create a StandardScaler instance
    scaler = StandardScaler()

    # Apply the scaler model to fit the X-train data
    X_scaler = scaler.fit(X_train)

    # Transform the X_train and X_test DataFrames using the X_scaler
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)

    return X_train_scaled, X_test_scaled

# From SVM, instantiate SVC classifier model instance
def model_fit_predict(model, X_train, y_train, X_test):
 
    # Fit the model to the data using the training data
    model_fitted = model.fit(X_train, y_train)
 
    # Use the testing data to make the model predictions
    pred = model_fitted.predict(X_test) 

    return pred

# Create a new empty predictions DataFrame.
def get_Strategy_and_Actual_returns(index_of_df, svm_pred, signals_test_df):       
    # Create a predictions DataFrame
    predictions_df = pd.DataFrame(index=index_of_df)# YOUR CODE HERE

    # Add the SVM model predictions to the DataFrame
    predictions_df['Predicted'] = svm_pred 

    # Add the actual returns to the DataFrame
    predictions_df['Actual Returns'] = signals_test_df['Actual Returns'] # YOUR CODE HERE

    # Add the strategy returns to the DataFrame
    predictions_df['Strategy Returns'] = predictions_df['Actual Returns'] * predictions_df['Predicted']

    # Plot the actual returns versus the strategy returns
    return (1+predictions_df[['Strategy Returns', 'Actual Returns']]).cumprod()