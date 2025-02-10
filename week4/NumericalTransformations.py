# 1. Centering Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import codecademylib3_seaborn 

coffee = pd.read_csv('starbucks_customers.csv')

ages = coffee.age

min_age = min(ages)
print(min_age)

max_age = max(ages)
print(max_age)

print(max_age - min_age)

mean_age = np.mean(ages)
print(mean_age)

centered_ages = ages - mean_age
print(centered_ages)

plt.hist(centered_ages)
plt.show()

# 2. Standardizing Data
import pandas as pd
import numpy as np

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

mean_age = np.mean(ages)
std_dev_age = np.std(ages)

ages_standardized = (ages - mean_age) / std_dev_age

print(np.mean(ages_standardized))
print(np.std(ages_standardized))
