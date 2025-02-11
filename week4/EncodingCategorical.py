# 1. Ordinal Encoding
encoder = OrdinalEncoder(categories=[['Excellent', 'New', 'Like New', 'Good', 'Fair']])

condition_reshaped = cars['condition'].values.reshape(-1,1)

cars['condition_rating'] = encoder.fit_transform(condition_reshaped)

# 2. Label Encoding
encoder = LabelEncoder()

cars['color'] = encoder.fit_transform(cars['color'])
