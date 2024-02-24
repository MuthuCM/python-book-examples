# Example 15.1 - Version 2 ( ML Approach)
# Simple Linear Regression - Example 1
# Import the Libraries
import numpy as np
import matplotlib.pyplot as plt

# Specify Data
X = [1,2,3,4,5,6,7,8,9,10]
Y = [3,5,7,9,11,13,15,17,19,21]
X = np.array(X)
X = X.reshape(-1,1)

# Fit Linear Regression Model
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,Y)
regression_coefficient = lr.coef_[0]
intercept = lr.intercept_

# Display Output
print(f"Regression Coefficient =  {regression_coefficient:5.2f} ")
print(f"Intercept is: { intercept : 5.2f}" )
print()
print(f"Regression Equation is: Y = {regression_coefficient:5.2f} X + { intercept : 5.2f}")
print()

# Do Prediction
predicted_value = lr.predict([[11]])[0]
print(f"Predicted Value is: { predicted_value: 5.2f}")
print()

# Visualize the Regression Line
plt.scatter(X,Y,color = 'red')
plt.plot(X,lr.predict(X), color = 'blue')
plt.show()
