# Example 15.3
# Simple Linear Regression - Example 3
# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read Data from a CSV File
df = pd.read_csv('Salary_Data.csv')
X = df.iloc[:, 0].values
Y = df.iloc[:, 1].values
X = X.reshape(-1, 1)

# Fit Simple Linear Regression Model
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X, Y)
regression_coefficient = lr.coef_[0]
intercept = lr.intercept_

# Display Output
print(f"Regression Coefficient =  {regression_coefficient:5.2f} ")
print(f"Intercept is: { intercept : 5.2f}" )
print()
print(f"Regression Equation is: Y = {regression_coefficient:5.2f} X + { intercept : 5.2f}")
print()

# Calculate R2 Score
Y_pred = lr.predict(X)
from sklearn.metrics import r2_score
print(f"Accuracy is: {r2_score(Y, Y_pred):5.2f}")
print()

# Visualize the Regression Line
plt.scatter(X,Y,color = 'red')
plt.plot(X,lr.predict(X), color = 'blue')
plt.show()