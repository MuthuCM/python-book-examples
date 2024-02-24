#Example 16.2
# Classification Example 2 - Logistic Regression

# Import the libraries
import numpy as np
import pandas as pd

# Read data from a CSV file
df = pd.read_csv('VehicleData1.csv')
X = df["salary"].values
y = df["vehicle_type"].values
X = X.reshape(-1, 1)

# Do Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

# Fit Logistic Regression Model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X, y)

# Find Accuracy Score and Confusion Matrix
from sklearn.metrics import accuracy_score, classification_report
y_pred = classifier.predict(X)
print(y_pred)
print()
print(accuracy_score(y, y_pred))
print()
print(classification_report(y, y_pred))
print()
from sklearn import metrics
print("F-Score: ", metrics.f1_score(y, y_pred, average = 'weighted'))
print()

# Do Prediction

X = [75000,92000,31000]
X = np.array(X)
X = X.reshape(-1,1)
X = sc.fit_transform(X)
predictedValues = classifier.predict(X)
print(predictedValues)