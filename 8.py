# 8) Analyze a dataset containing information about the sales revenue and advertising
# expenditure of a company over a period of time. Calculate the Karl Pearson correlation
# coefficient between sales revenue and advertising expenditure using Python. Interpret the
# correlation coefficient and discuss the strength and direction of the relationship between
# advertising and sales.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('sales_dataset.csv')

sales = df['Sales']
advertising = df['Advertising']

correlation_coeff, p_val = stats.pearsonr(sales, advertising)

if correlation_coeff > 0:
    corr_direction = "Positive"
elif correlation_coeff < 0: 
    corr_direction = "Negative"
else :
    corr_direction = "no"

corr_strength = abs(correlation_coeff)

print(correlation_coeff)
print(corr_strength)
print(corr_direction)

plt.scatter(advertising, sales)
plt.xlabel("Advertising")
plt.ylabel('sales')
plt.show()
