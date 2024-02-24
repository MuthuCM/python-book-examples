# Example 16.4

# Import the libraries
import mglearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

X, y = mglearn.datasets.make_forge()

classifier = LogisticRegression()
cr = classifier.fit(X,y)

mglearn.plots.plot_2d_separator(cr, X,fill = False, eps = 0.5)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.title("Logistic Regression Classifier")
plt.xlabel("Salary")
plt.ylabel("Vehicle Type")
plt.show()