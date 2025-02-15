import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense
from tensorflow.keras.optimizers import Adam


# Data Loading
dataset = pd.read_csv('life_expectancy.csv')

# pd.DataFrame.head(dataset)
# pd.DataFrame.describe(dataset)

dataset = dataset.drop(['Country'], axis = 1)
labels = dataset.iloc[:, -1]
features = dataset.iloc[:, 0:-1] #select all the rows (:), and access columns from 0 to the last column

# Preprocessing
features = pd.get_dummies(features)

# Split data into training and test
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state=23)

# Standardize
numerical_features = features.select_dtypes(include=['float64', 'int64'])
numerical_columns = numerical_features.columns

ct = ColumnTransformer([('only numeric', StandardScaler(), numerical_columns)], remainder='passthrough')

features_train_scaled = ct.fit_transform(features_train)
features_test_scaled = ct.transform(features_test)

# Building the model
my_model = Sequential()

# Input layer
input = InputLayer(input_shape = (features.shape[1], ))
my_model.add(input)

# Output layer
my_model.add(Dense(64, activation='relu'))
my_model.add(Dense(1))

# Model summary
# print(my_model.summary())

# Optomizer and compiling model
opt = Adam(learning_rate=0.01)

my_model.compile(loss='mse', metrics='mae', optimizer=opt)

# Evaluvate the model
my_model.fit(features_train_scaled, labels_train, epochs=50, batch_size=1, verbose=1)

res_mse, res_mae = my_model.evaluate(features_test_scaled, labels_test, verbose=0)

# Final loss = RSME, final metric = MAE
print(res_mse, res_mae)
