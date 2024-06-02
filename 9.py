# 9) Develop a Python/R code to build a simple Linear Regression model to predict sales units
# based on the advertising budget spent on TV. Display the statistical summary of the
# model.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

sales = np.array([2, 4, 6, 9, 12, 34, 45])
tv_budgets = np.array([1, 2, 4, 7, 9, 11, 15])

x = tv_budgets.reshape(-1, 1)
y = sales

model = LinearRegression()
model.fit(x, y)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

y_pred = model.predict(x)

plt.scatter(x, y, color='b', label="Actual Sales")
plt.plot(x, y_pred, color='r', label="Linear Regression")
plt.xlabel("TV Budget")
plt.ylabel("Sales")
plt.legend()
plt.show()
