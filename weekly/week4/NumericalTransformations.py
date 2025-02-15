# 1. Centering Data
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
coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

mean_age = np.mean(ages)
std_dev_age = np.std(ages)

ages_standardized = (ages - mean_age) / std_dev_age

print(np.mean(ages_standardized))
print(np.std(ages_standardized))

# 3. Using Sklearn to do scaling for me
coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

scaler = StandardScaler()

ages_reshaped = np.array(ages).reshape(-1,1)
ages_scaled = scaler.fit_transform(ages_reshaped)

print(np.mean(ages_scaled))
print(np.std(ages_scaled))

# 4. Min-Max 
coffee = pd.read_csv('starbucks_customers.csv')

spent = coffee['spent']

max_spent = np.max(spent)
min_spent = np.min(spent)
spent_range = max_spent - min_spent
print(spent_range)

spent_normalized = (spent - min_spent) / spent_range

print(spent_normalized)

# 4. Using Sklearn to do MinMax for me
coffee = pd.read_csv('starbucks_customers.csv')
spent = coffee['spent']

spent_reshaped = np.array(spent).reshape(-1, 1)

mmscaler = MinMaxScaler()

reshaped_scaled = mmscaler.fit_transform(spent_reshaped)

print(np.min(reshaped_scaled))
print(np.max(reshaped_scaled))

# 5. Binning our data
coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

print(np.min(ages))
print(np.max(ages))

age_bins = [12, 20, 30, 40, 71]

coffee['binned_ages'] = pd.cut(ages, age_bins, right = False)
print(coffee['binned_ages'].head(10))

coffee['binned_ages'].value_counts().plot(kind='bar')
plt.show()
