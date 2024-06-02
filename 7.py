# 7) Consider the scores of ten students in SMIP and DBMS and Compute the Spearman rank
# correlation and Interpret the results using Python/R

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

x = [70, 46, 54, 34, 20, 86, 18, 12, 56, 64]
y = [60, 66, 90, 46, 16, 48, 74, 8, 32, 54]

df = pd.DataFrame({'SMIP': x, 'DBMS': y})

corr = df.corr(method='spearman')
print(corr)

sns.heatmap(corr, annot=True)
plt.title('Heatmap of Spearman Correlation')
plt.show()

corr_coef, pval = stats.spearmanr(x, y)
print("Spearman correlation coefficient:", corr_coef)
print("p-value:", pval)

plt.hist([x, y], label=['SMIP', 'DBMS'], bins=5)
plt.title('Histogram of Scores')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.legend()
plt.show()
