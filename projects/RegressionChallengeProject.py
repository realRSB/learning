import app
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import InputLayer, Dense
from tensorflow.keras.optimizers import Adam

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

# Load data
dataset = pd.read_csv('admissions_data.csv')

# Dataframes
labels = dataset.iloc[:, -1]
features = dataset.iloc[:, 0:-1]  # Select all the rows (:), and access columns from 0 to the last column

# Train and test set
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20, random_state=23)

# Standardize
ct = ColumnTransformer([('standardize', StandardScaler(), features_train.columns)], remainder='passthrough')

features_train_scaled = ct.fit_transform(features_train)
features_test_scaled = ct.transform(features_test)

# Build model
my_model = Sequential()

# Input layer
input = InputLayer(input_shape=(features.shape[1],))
my_model.add(input)

# Hidden layer
my_model.add(Dense(16, activation='relu'))

# Output layer
my_model.add(Dense(1))

# Optimizer and compiling model
opt = Adam(learning_rate=0.01)
my_model.compile(loss='mse', metrics='mae', optimizer=opt)

# Early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, mode='min', verbose=1)

# Evaluate the model
history = my_model.fit(
    features_train_scaled, 
    labels_train, 
    epochs=50, 
    batch_size=1, 
    validation_split=0.2, 
    callbacks=[early_stopping], 
    verbose=1
)

res_mse, res_mae = my_model.evaluate(features_test_scaled, labels_test, verbose=0)

# Final loss = RSME, final metric = MAE
print(res_mse, res_mae)

# Predict
predicted_values = my_model.predict(features_test_scaled)

# Calculate R-squared
r_squared = r2_score(labels_test, predicted_values)
print(f"R-squared: {r_squared}")

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(history.history['mae'])
ax1.plot(history.history['val_mae'])
ax1.set_title('model mae')
ax1.set_ylabel('MAE')
ax1.set_xlabel('epoch')
ax1.legend(['train', 'validation'], loc='upper left')

  # Plot loss and val_loss over each epoch
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(history.history['loss'])
ax2.plot(history.history['val_loss'])
ax2.set_title('model loss')
ax2.set_ylabel('loss')
ax2.set_xlabel('epoch')
ax2.legend(['train', 'validation'], loc='upper left')

# used to keep plots from overlapping each other  
fig.tight_layout()
fig.savefig('static/images/my_plots.png')
