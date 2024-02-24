#Example 16.1
# Simple Classification using Logistic Regression
# Import the Libraries
import numpy as np

# Specify Data
salary = [45000,40000,35000,30000,42000,37000,43000,38000,41000,44000,90000,80000,70000,60000,95000,85000,75000,65000,84000,92000]
vehicle_type = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
salary = np.array(salary)
salary = salary.reshape(-1,1)

# Transform the Data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
salary = sc.fit_transform(salary)

# Fit Logistic Regression Model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(salary, vehicle_type)

# Predict the Results
predicted_values = classifier.predict(salary)
print(predicted_values)
print()

# Calculate Accuracy
from sklearn import metrics
predicted_values = classifier.predict(salary)
print("F-Score: ", metrics.f1_score(vehicle_type, predicted_values, average = 'weighted'))
