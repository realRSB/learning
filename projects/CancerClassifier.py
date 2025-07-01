import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the data
breast_cancer_data = load_breast_cancer()

# Split the data into training and validation sets
training_data, validation_data, training_labels, validation_labels = train_test_split(
    breast_cancer_data.data, breast_cancer_data.target, test_size=0.2, random_state=100
)

# Initialize variables
k_list = range(1, 101)
accuracies = []
cross_val_accuracies = []

# Perform KNN classification for each k
for k in k_list:
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(training_data, training_labels)
    score = classifier.score(validation_data, validation_labels)
    accuracies.append(score)
    
    # Cross-validation for more robust accuracy
    cross_val_score_mean = cross_val_score(classifier, training_data, training_labels, cv=5).mean()
    cross_val_accuracies.append(cross_val_score_mean)

# Plot the results
plt.figure(figsize=(14, 8))
sns.set(style="whitegrid")

plt.plot(k_list, accuracies, label='Validation Accuracy', color='blue', linestyle='-', marker='o')
plt.plot(k_list, cross_val_accuracies, label='Cross-Validation Accuracy', color='green', linestyle='--', marker='x')

plt.title("Breast Cancer Classifier Accuracy with K-Nearest Neighbors", fontsize=16)
plt.xlabel("Number of Neighbors (k)", fontsize=12)
plt.ylabel("Accuracy", fontsize=12)
plt.legend()
plt.xticks(np.arange(0, 101, step=5))
plt.grid(True)
plt.show()

# Find the best k
best_k = k_list[np.argmax(accuracies)]
best_accuracy = max(accuracies)
print(f"Best k: {best_k} with Validation Accuracy: {best_accuracy:.4f}")

best_cross_val_k = k_list[np.argmax(cross_val_accuracies)]
best_cross_val_accuracy = max(cross_val_accuracies)
print(f"Best k with Cross-Validation: {best_cross_val_k} with Accuracy: {best_cross_val_accuracy:.4f}")
