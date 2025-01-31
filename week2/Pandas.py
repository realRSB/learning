import codecademylib3
import pandas as pd

#Part 1: reading the csv
orders = pd.read_csv('shoefly.csv')

#Part 2: inspecting the first five lines of data
print(orders.head(5))

#Part 3: selecting the column 'email'
emails = orders.email

#Part 4: the Frances Palmer incident
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

#Part 5: Comfy feet means more time on the street
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]

# Cool lambda functionality
df = pd.read_csv('employees.csv')

# Add columns here
get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

print(df)
