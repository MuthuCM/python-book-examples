#Example 16.3
# Classification example 3 - Logistic Regression
# Import the libraries
import numpy as np
import pandas as pd

# Read data from a CSV file
dataset = pd.read_csv('Health_Data.csv')

# Define independent variables & dependent variable
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# Do Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

# Fit Logistic Regression Classification Model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X, y)

# Calculate Accuracy
from sklearn import metrics
y_pred = classifier.predict(X)
print("F-Score: " , metrics.f1_score(y, y_pred, average = 'weighted'))
print()

# Do Prediction
testInput = { 'Height' : [174,189,185], 'Weight' : [96,87,110] }
testData = pd.DataFrame (testInput)
X = testData.iloc[:, :].values
X = sc.fit_transform(X)
predictedValue = classifier.predict(X)
print(predictedValue)
