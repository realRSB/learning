import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
from sklearn.metrics import classification_report
import numpy as np

# Load data
data = pd.read_csv('heart_failure.csv')

# Print columns and their types
print(data.info())

# Check class distribution
print('Classes and number of values in the dataset:', data['death_event'].value_counts())

# Features and labels
y = data.iloc[:, -1]  # Assuming the last column is the target 'death_event'
x = data.iloc[:, 0:-1]

# One-hot encoding for categorical variables if any
x = pd.get_dummies(x)

# Split data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=23)

# Select numeric columns for scaling
numeric_cols = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 
                'platelets', 'serum_creatinine', 'serum_sodium', 'time']

# Scale numeric features using StandardScaler
ct = ColumnTransformer(
    transformers=[
        ('numeric', StandardScaler(), numeric_cols)
    ],
    remainder='passthrough'  # Keep other features unchanged
)

X_train = ct.fit_transform(X_train)
X_test = ct.transform(X_test)

# Encode labels for classification
le = LabelEncoder()
Y_train = le.fit_transform(Y_train.astype(str))
Y_test = le.transform(Y_test.astype(str))

# Convert labels to categorical (one-hot encoding for binary classification)
Y_train = tf.keras.utils.to_categorical(Y_train, num_classes=2, dtype='int64')
Y_test = tf.keras.utils.to_categorical(Y_test, num_classes=2, dtype='int64')

# Design neural network model
model = Sequential()

# Input layer
model.add(InputLayer(input_shape=(X_train.shape[1],)))

# Hidden layer
model.add(Dense(12, activation='relu'))

# Output layer (2 neurons for binary classification)
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(
    loss='categorical_crossentropy',  # Suitable for one-hot encoding
    optimizer='adam',
    metrics=['accuracy']
)

# Train the model
model.fit(X_train, Y_train, epochs=50, batch_size=16, verbose=1)

# Evaluate the model
loss, acc = model.evaluate(X_test, Y_test, verbose=0)
print("Loss:", loss, "Accuracy:", acc)

# Predict on test data
y_estimate = model.predict(X_test, verbose=0)
y_estimate = np.argmax(y_estimate, axis=1)  # Convert one-hot to label
y_true = np.argmax(Y_test, axis=1)

# Print classification report
print(classification_report(y_true, y_estimate))
