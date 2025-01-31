import codecademylib3
import pandas as pd

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
