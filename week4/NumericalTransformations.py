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

# 3. Using Sklearn to do scaling for me
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler 

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

scaler = StandardScaler()

ages_reshaped = np.array(ages).reshape(-1,1)
ages_scaled = scaler.fit_transform(ages_reshaped)

print(np.mean(ages_scaled))
print(np.std(ages_scaled))

# 4. Min-Max 
import pandas as pd
import numpy as np

coffee = pd.read_csv('starbucks_customers.csv')

spent = coffee['spent']

max_spent = np.max(spent)
min_spent = np.min(spent)
spent_range = max_spent - min_spent
print(spent_range)

spent_normalized = (spent - min_spent) / spent_range

print(spent_normalized)

# 4. Using Sklearn to do MinMax for me
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

coffee = pd.read_csv('starbucks_customers.csv')
spent = coffee['spent']

spent_reshaped = np.array(spent).reshape(-1, 1)

mmscaler = MinMaxScaler()

reshaped_scaled = mmscaler.fit_transform(spent_reshaped)

print(np.min(reshaped_scaled))
print(np.max(reshaped_scaled))
