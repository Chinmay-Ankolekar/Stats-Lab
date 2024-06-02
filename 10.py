# 10) Consider Australian Drug Sales dataset and develop a Python/R code to perform Time
# Series Analysis and visualize using plots.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('AusAntidiabeticDrug.csv')

date = df['ds']
sales = df['y']

datetime = pd.to_datetime(date)

# sns.set(style="whitegrid", color_codes=True)

# plt.figure(figsize=(16, 6))
plt.plot(datetime, sales)
plt.xlabel("Time")
plt.ylabel("$ Millions")
plt.title("Antidiabetic Drug Sales Over Time")
plt.show()
