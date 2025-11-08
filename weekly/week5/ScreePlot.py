import numpy as np
import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt

eigenvalues = pd.read_csv('eigenvalues.csv')['eigenvalues'].values

# 1. Find the proportion of information for each eigenvector, which is equal to the eigenvalues divided by the sum of all eigenvalues
info_prop = eigenvalues / eigenvalues.sum()

## Plot the principal axes vs the information proportions for each principal axis

plt.plot(np.arange(1,len(info_prop)+1),info_prop, 'bo-', linewidth=2)
plt.title('Scree Plot')
plt.xlabel('Principal Axes')
plt.xticks(np.arange(1,len(info_prop)+1))
plt.ylabel('Proportion of Information Explained')
plt.show()
plt.clf()

# 2. Find the cumulative sum of the proportions
cum_info_prop = np.cumsum(info_prop)

## Plot the cumulative proportions array

plt.plot(np.arange(1,len(info_prop)+1), cum_info_prop, 'bo-', linewidth=2)
plt.hlines(y=.95, xmin=1, xmax=15)
plt.vlines(x=4, ymin=0, ymax=1)
plt.title('Cumulative Information Proportions')
plt.xlabel('Principal Axes')
plt.xticks(np.arange(1,len(info_prop)+1))
plt.ylabel('Cumulative Proportion of Information Explained')
plt.show()
