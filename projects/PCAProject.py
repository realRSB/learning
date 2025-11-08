import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
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

# Standardize the dataset by subtracting the mean and dividing by the standard deviation.
mean = data_matrix.mean(axis=0)
sttd = data_matrix.std(axis=0)
data_matrix_standardized = (data_matrix - mean) / sttd

# Perform PCA on the standardized dataset.
pca = PCA()
principal_components = pca.fit_transform(data_matrix_standardized)
print(f'Number of features in the data matrix: {principal_components.shape[1]}')
print(f'Number of features in the principal components: {data_matrix.shape[1]}')

# Compute the eigenvalues from the singular values and extract the eigenvectors.
singular_values = pca.singular_values_
eigenvalues = singular_values ** 2
eigenvectors = pca.components_.T

# Extract the variance ratios, which represent the proportion of variance explained by each principal component.
principal_axes_variance_ratios = pca.explained_variance_ratio_
principal_axes_variance_percents = principal_axes_variance_ratios * 100

# Perform PCA again but limit the components to 2.
pca = PCA(n_components=2)
principal_components = pca.fit_transform(data_matrix_standardized)
print(f'Number of Principal Components Features: {principal_components.shape[1]}')
print(f'Number of Original Data Features: {data_matrix_standardized.shape[1]}')

# Visualize the principal components in a scatter plot with class labels as hue.
principal_components_data = pd.DataFrame({
    'PC1': principal_components[:, 0],
    'PC2': principal_components[:, 1],
    'class': classes,
})
sns.lmplot(x='PC1', y='PC2', data=principal_components_data, hue='class', fit_reg=False)
plt.show()

# Convert class labels to categorical numerical values for classification.
y = classes.astype('category').cat.codes

# Train a LinearSVC model using the two principal components.
pca_1 = PCA(n_components=2)
X = pca_1.fit_transform(data_matrix_standardized)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
svc_1 = LinearSVC(random_state=0, tol=1e-5)
svc_1.fit(X_train, y_train)
score_1 = svc_1.score(X_test, y_test)
print(f'Score for model with 2 PCA features: {score_1}')

# Train a LinearSVC model using the first two features from the original dataset.
first_two_original_features = [0, 1]
X_original = data_matrix_standardized.iloc[:, first_two_original_features]
X_train, X_test, y_train, y_test = train_test_split(X_original, y, test_size=0.33, random_state=42)
svc_2 = LinearSVC(random_state=0)
svc_2.fit(X_train, y_train)
score_2 = svc_2.score(X_test, y_test)
print(f'Score for model with 2 original features: {score_2}')
