import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer

#load the dataset
dataset = pd.read_csv('insurance.csv') 
#choose first 7 columns as features
features = dataset.iloc[:,0:6] 
#choose the final column for prediction
labels = dataset.iloc[:,-1] 

#one-hot encoding for categorical variables
features = pd.get_dummies(features) 
#split the data into training and test data
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42) 
 
#normalize the numeric columns using ColumnTransformer
ct = ColumnTransformer([('normalize', Normalizer(), ['age', 'bmi', 'children'])], remainder='passthrough')
#fit the normalizer to the training data and convert from numpy arrays to pandas frame
features_train_norm = ct.fit_transform(features_train) 
#applied the trained normalizer on the test data and convert from numpy arrays to pandas frame
features_test_norm = ct.transform(features_test) 

#ColumnTransformer returns numpy arrays. Convert the features to dataframes
features_train_norm = pd.DataFrame(features_train_norm, columns = features_train.columns)
features_test_norm = pd.DataFrame(features_test_norm, columns = features_test.columns)

# -----> your code here below
my_ct = ColumnTransformer([('scale', StandardScaler(), ['age', 'bmi', 'children'])], remainder='passthrough')
#fit the scaler to the training data and convert from numpy arrays to pandas frame
features_train_scale = my_ct.fit_transform(features_train) 
#applied the trained scaler on the test data and convert from numpy arrays to pandas frame
features_test_scale = my_ct.transform(features_test) 

#ColumnTransformer returns numpy arrays. Convert the features to dataframes
features_train_scale = pd.DataFrame(features_train_scale, columns = features_train.columns)
features_test_scale = pd.DataFrame(features_test_scale, columns = features_test.columns)

#print the summary statistics
print(features_train_scale.describe())
print(features_test_scale.describe())
