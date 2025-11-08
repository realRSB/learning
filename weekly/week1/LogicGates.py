import codecademylib3_seaborn
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

# Define the data and labels for the AND gate
data = [[0, 0], [0, 1], [1, 0], [1, 1]]
labels = [0, 0, 0, 1]

# Plot the data points
plt.scatter([point[0] for point in data], [point[1] for point in data], c=labels)

# Create and train the Perceptron
classifier = Perceptron(max_iter=40, random_state=22)
classifier.fit(data, labels)

# Create a grid of points for visualization
x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)
point_grid = list(product(x_values, y_values))

# Calculate distances from the decision boundary
distances = classifier.decision_function(point_grid)
abs_distances = [abs(value) for value in distances]

# Reshape distances for heatmap
distances_matrix = np.reshape(abs_distances, (100, 100))

# Plot the heatmap
heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)
plt.colorbar(heatmap)

# Show the plot
plt.show()
