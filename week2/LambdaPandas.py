import codecademylib3
import pandas as pd

# Lambda split
get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

print(df)

# Using lambda for rows
df = pd.read_csv('employees.csv')

total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)

print(df)

# Load data
orders = pd.read_csv('shoefly.csv')

# Add column to check if vegan
orders['shoe_source'] = orders['shoe_material'].apply(
    lambda x: 'animal' if x == 'leather' else 'vegan'
)

# Add salutation column
orders['salutation'] = orders.apply(
    lambda row: f"Dear Mr. {row['last_name']}" if row['gender'] == 'male' else f"Dear Ms. {row['last_name']}",
    axis=1
)

# Display first few rows
print(orders.head())
