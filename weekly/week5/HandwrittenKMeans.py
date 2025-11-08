import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# Import + Visualization
digits = datasets.load_digits()
# print(digits.DESCR)
# print(digits.data)
# print(digits.target)

# Figure size (width, height)

fig = plt.figure(figsize=(6, 6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
# For each of the 64 images
for i in range(64):
    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    ax.text(0, 7, str(digits.target[i]))
plt.show()

# Model
model = KMeans(n_clusters=10, random_state=42)
model.fit(digits.data)

# Visualizing after K-Means
fig = plt.figure(figsize=(8, 3))

fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

for i in range(10):
  ax = fig.add_subplot(2, 5, 1 + i)
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
plt.show()

new_samples = np.array(([
[0.00,1.42,4.04,4.57,4.57,4.42,1.06,0.00,0.00,2.97,6.86,6.53,6.17,7.46,5.96,0.00,0.00,0.00,0.00,5.67,7.22,7.62,5.30,0.00,0.00,0.00,0.00,3.09,5.21,7.61,3.66,0.00,0.00,0.00,0.00,0.00,2.41,7.62,2.94,0.00,0.00,0.00,3.63,6.53,7.24,6.40,0.28,0.00,0.00,0.00,2.05,5.33,4.69,0.92,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.52,4.57,2.18,0.00,0.00,0.00,0.00,0.00,6.40,7.62,7.29,2.10,0.00,0.00,0.00,1.22,7.62,4.09,6.70,5.94,0.00,0.00,0.00,1.27,7.62,4.99,7.01,5.59,0.00,0.00,0.00,0.00,4.96,7.54,6.89,1.57,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.02,7.39,7.54,5.92,2.36,0.00,0.00,0.00,2.90,7.62,4.70,6.84,6.60,0.00,0.00,0.00,1.89,7.62,6.24,6.91,5.69,0.00,0.00,0.00,0.00,2.87,5.71,6.02,1.88,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.99,1.52,0.07,0.00,0.00,0.00,0.00,3.78,7.62,7.62,6.68,1.05,0.00,0.00,0.30,7.46,5.83,2.92,7.21,4.92,0.00,0.00,0.00,5.95,7.62,6.08,7.21,5.10,0.00,0.00,0.00,0.43,3.55,5.32,5.25,1.14,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
]))

new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')

print(new_labels)
