# Example 15.5
# Multiple Regression  - Predicting house price using Boston Data Set
# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read data from a CSV file
df = pd.read_csv('boston.csv')
# X = df.drop('MV', axis =1).values
# Y = df.MV.values
X = df.iloc[: , 1:7].values
Y = df.iloc[: , 0].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fit Multiple Linear Regression Model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
print(f"Regression Coefficients are: {regressor.coef_}")
print()

# Calculate Accuracy
from sklearn.metrics import r2_score
print(f"Accuracy Score is: {r2_score(Y_test, regressor.predict(X_test))}")
print()

# Do Prediction
dictionary1 = { 'INDUS' : [2.32,7.06,7.07],
                'NOX' : [53.9,47.0,46.9],
               'RM': [6.675,6.521,7.280],
               'TAX' : [290,240,242],
               'PT' : [15,17.9,17.8],
               'LSTAT' : [5,9,4]
              }
df1 = pd.DataFrame (dictionary1)
X1 = df1.iloc[:, :].values
X1 = sc.fit_transform(X1)
predictedValues = regressor.predict(X1)
print(predictedValues)