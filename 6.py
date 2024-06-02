# 6) Perform univariate analysis on a dataset containing information about the performance
# of students in a school. The dataset includes variables such as student ID, test scores in
# different subjects, attendance, and socio-economic background. Use Python to analyze the
# distribution of test scores in each subject separately. Calculate the mean, median, and
# standard deviation for each subject and visualize the distribution using box plots.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("student_performance.csv")

subjects = ['math score', 'reading score'] 

for subject in subjects:
    subject_scores = data[subject]

    mean_score = np.mean(subject_scores)
    median_score = np.median(subject_scores)
    std_score = np.std(subject_scores)

#     plt.figure(figsize=(10, 6))
    plt.boxplot(subject_scores)
    plt.xlabel(subject.capitalize())
    plt.ylabel("Score")
    plt.title("Distribution of " + subject.capitalize())
    plt.show()

    print(subject.capitalize() + ":")
    print("Mean:", mean_score)
    print("Median:", median_score)
    print("Standard Deviation:", std_score)
    print()
