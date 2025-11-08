# Import required libraries
import codecademylib3
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Load the dataset from UCI repository
# The dataset contains information about flags, with various features such as colors, shapes, etc.
cols = ['name', 'landmass', 'zone', 'area', 'population', 'language', 'religion', 'bars', 'stripes', 'colours',
        'red', 'green', 'blue', 'gold', 'white', 'black', 'orange', 'mainhue', 'circles', 'crosses', 'saltires',
        'quarters', 'sunstars', 'crescent', 'triangle', 'icon', 'animate', 'text', 'topleft', 'botright']
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data", names=cols)

# Specify variable names (features) to be used as predictors for classification
var = ['red', 'green', 'blue', 'gold', 'white', 'black', 'orange', 'mainhue', 'bars', 'stripes', 'circles', 'crosses', 
       'saltires', 'quarters', 'sunstars', 'triangle', 'animate']

# Print the number of countries in each landmass (continent) category
print(df.landmass.value_counts())

# Filter the dataset for countries in Europe (landmass = 3) and Oceania (landmass = 6)
df_36 = df[df["landmass"].isin([3, 6])]

# Print the average values of the predictors for Europe and Oceania
print(df_36.groupby('landmass')[var].mean().T)

# Create labels for classification based on landmass (Europe vs Oceania)
labels = df_36["landmass"]

# Print the data types for the predictor variables
print(df[var].dtypes)

# Create dummy variables for categorical predictors (converts categorical variables to binary format)
data = pd.get_dummies(df_36[var])

# Split data into a training set (60%) and a test set (40%)
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state=1, test_size=.4)

# Fit decision tree models for max_depth values between 1 and 20, and record accuracy for each depth
depths = range(1, 21)
acc_depth = []
for i in depths:
    dt = DecisionTreeClassifier(random_state=10, max_depth=i)
    dt.fit(train_data, train_labels)
    acc_depth.append(dt.score(test_data, test_labels))

# Plot accuracy vs. tree depth to visualize how model performance changes with depth
plt.plot(depths, acc_depth)
plt.xlabel('max_depth')
plt.ylabel('accuracy')
plt.show()

# Find the maximum accuracy and the corresponding depth where this occurs
max_acc = np.max(acc_depth)
best_depth = depths[np.argmax(acc_depth)]
print(f'Highest accuracy {round(max_acc, 3) * 100}% at depth {best_depth}')

# Refit the decision tree model with the best depth, and plot the decision tree
plt.figure(figsize=(14, 8))
dt = DecisionTreeClassifier(random_state=1, max_depth=best_depth)
dt.fit(train_data, train_labels)
tree.plot_tree(dt, feature_names=train_data.columns,  
               class_names=['Europe', 'Oceania'], filled=True)
plt.show()

# Prune the decision tree using different values of ccp_alpha (complexity parameter)
acc_pruned = []
ccp = np.logspace(-3, 0, num=20)
for i in ccp:
    dt_prune = DecisionTreeClassifier(random_state=1, max_depth=best_depth, ccp_alpha=i)
    dt_prune.fit(train_data, train_labels)
    acc_pruned.append(dt_prune.score(test_data, test_labels))

# Plot accuracy vs. ccp_alpha to visualize how pruning affects model performance
plt.plot(ccp, acc_pruned)
plt.xscale('log')  # Use a logarithmic scale for the x-axis
plt.xlabel('ccp_alpha')
plt.ylabel('accuracy')
plt.show()

# Find the maximum accuracy and the corresponding ccp_alpha value for pruning
max_acc_pruned = np.max(acc_pruned)
best_ccp = ccp[np.argmax(acc_pruned)]
print(f'Highest accuracy {round(max_acc_pruned, 3) * 100}% at ccp_alpha {round(best_ccp, 4)}')

# Fit a final decision tree model with the best max_depth and ccp_alpha values
dt_final = DecisionTreeClassifier(random_state=1, max_depth=best_depth, ccp_alpha=best_ccp)
dt_final.fit(train_data, train_labels)

# Plot the final pruned decision tree
plt.figure(figsize=(14, 8))
tree.plot_tree(dt_final, feature_names=train_data.columns,  
               class_names=['Europe', 'Oceania'], filled=True)
plt.show()
