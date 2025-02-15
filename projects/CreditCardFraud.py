import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the data
transactions = pd.read_csv('transactions_modified.csv')

# How many fraudulent transactions?
total_fraud_modified = transactions['isFraud'].sum()
print(f"Fraudulent Transactions in Modified Dataset: {total_fraud_modified}")

# Summary statistics on amount column
print(transactions['amount'].describe())

# Create isPayment field
transactions['isPayment'] = transactions['type'].isin(['PAYMENT', 'DEBIT']).astype(int)

# Create isMovement field
transactions['isMovement'] = transactions['type'].isin(['CASH_OUT', 'TRANSFER']).astype(int)

# Create accountDiff field
transactions['accountDiff'] = (transactions['oldbalanceOrg'] - transactions['oldbalanceDest']).abs()

# Create features and label variables
label = transactions['isFraud']
features = transactions[['amount', 'isPayment', 'isMovement', 'accountDiff']]

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(features, label, train_size=0.7, test_size=0.3, random_state=6)

# Normalize the features variables
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Fit the model to the training data
model = LogisticRegression()
model.fit(x_train, y_train)

# Score the model on the training data
train_score = model.score(x_train, y_train).round(5)
print(f'Train Score: {train_score}')

# Score the model on the test data
test_score = model.score(x_test, y_test).round(5)
print(f'Test Score: {test_score}')

# New transaction data
transaction1 = np.array([123456.78, 0.0, 1.0, 54670.1])
transaction2 = np.array([98765.43, 1.0, 0.0, 8524.75])
transaction3 = np.array([543678.31, 1.0, 0.0, 510025.5])
your_transaction = np.array([6472.54, 1.0, 0.0, 55901.23])

# Combine new transactions into a single array
sample_transactions = np.stack((transaction1, transaction2, transaction3, your_transaction))

# Normalize the new transactions
sample_transactions = scaler.transform(sample_transactions)

# Predict fraud on the new transactions
predictions = model.predict(sample_transactions)
print(f'Model Prediction Score: {predictions}')

# Show probabilities on the new transactions
model_proba = model.predict_proba(sample_transactions)
print(f'Model Prediction Probabilities: {model_proba}')

# Load the complete dataset
complete_transactions = pd.read_csv('transactions.csv')

# Count fraudulent transactions in the complete dataset
total_fraud_complete = complete_transactions['isFraud'].sum()
total_transactions_complete = len(complete_transactions)
fraud_percentage_complete = (total_fraud_complete / total_transactions_complete) * 100

print(f"Fraudulent Transactions in Complete Dataset: {total_fraud_complete}")
print(f"Percentage of Fraudulent Transactions in Complete Dataset: {fraud_percentage_complete:.2f}%")

# Calculate percentage of fraudulent transactions in the modified dataset
total_transactions_modified = len(transactions)
fraud_percentage_modified = (total_fraud_modified / total_transactions_modified) * 100

print(f"Percentage of Fraudulent Transactions in Modified Dataset: {fraud_percentage_modified:.2f}%")

# Set the style of the visualization
sns.set(style="whitegrid")

# Create a figure and axis
plt.figure(figsize=(14, 8))

# Plot a violin plot to show the distribution of transaction amounts
sns.violinplot(x='isFraud', y='amount', data=transactions, palette='muted', split=True)

# Overlay a swarm plot to show individual data points
sns.swarmplot(x='isFraud', y='amount', data=transactions, color='k', alpha=0.5)

# Add titles and labels
plt.title('Distribution of Transaction Amounts by Fraud Status', fontsize=16)
plt.xlabel('Fraud Status (0 = Non-Fraudulent, 1 = Fraudulent)', fontsize=12)
plt.ylabel('Transaction Amount', fontsize=12)

# Show the plot
plt.show()
