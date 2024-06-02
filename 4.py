# 4) You have been provided with a dataset containing information about the heights of
# students in a college. Perform univariate analysis on this dataset using Python and
# calculate the mean, median, mode, and standard deviation of the heights. Also, create a
# histogram to visualize the distribution of heights. Write a Python program to implement
# this analysis.
# heights = [165, 170, 168, 172, 175, 169, 180, 160, 165, 172, 168, 176, 170, 173, 165]

import numpy as np
import matplotlib.pyplot as plt

heights = [165, 170, 168, 172, 175, 169, 180, 160, 165, 172, 168, 176, 170, 173, 165]

mean_height = np.mean(heights)
print(mean_height)

median_height = np.median(heights)
print(median_height)

mode_height = np.argmax(np.bincount(heights))
print(mode_height)

std_height = np.std(heights)
print(std_height)

plt.hist(heights, bins=5)
plt.xlabel("height")
plt.ylabel("Freq")
plt.title("Distribution of heights ")
plt.show()
