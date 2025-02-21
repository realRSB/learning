import numpy as np
import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset and remove NaN values.
df = pd.read_csv('./telescope_data.csv', index_col=0)
df.dropna(inplace=True)
print('Task 1:')
print(df.head())

# Extract the class column and separate features.
classes = df['class']
data_matrix = df.drop(columns='class')
print('Task 2:')
print(data_matrix)

# Compute and visualize the correlation matrix.
correlation_matrix = data_matrix.corr()
ax = plt.axes()
sns.heatmap(correlation_matrix, cmap='Greens', ax=ax)
ax.set_title('Task 3:')
plt.show()

# Perform eigendecomposition on the correlation matrix.
eigenvalues, eigenvectors = np.linalg.eig(correlation_matrix)
indices = eigenvalues.argsort()[::-1]  
eigenvalues = eigenvalues[indices]
eigenvectors = eigenvectors[:, indices]
print('Task 4:')
print(f'Eigenvalues length: {eigenvalues.size}, Original Number of Features: {data_matrix.shape[1]}')
print(eigenvalues.shape, eigenvectors.shape)

# Calculate and visualize the variance explained by each eigenvalue.
information_proportions = eigenvalues / eigenvalues.sum()
information_percents = information_proportions * 100
plt.figure()
plt.plot(information_percents, 'ro-', linewidth=2)
plt.title('Task 5: Scree Plot')
plt.xlabel('Principal Axes')
plt.ylabel('Percent of Information Explained')
plt.show()

# Compute and visualize the cumulative variance explained.
cumulative_information_percents = np.cumsum(information_percents)
plt.figure()
plt.plot(cumulative_information_percents, 'ro-', linewidth=2)
plt.hlines(y=95, xmin=0, xmax=15)
plt.vlines(x=3, ymin=0, ymax=100)
plt.title('Task 6: Cumulative Information percentages')
plt.xlabel('Principal Axes')
plt.ylabel('Cumulative Proportion of Variance Explained')
plt.show()
