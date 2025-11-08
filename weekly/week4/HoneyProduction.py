import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

prod_by_year = df.groupby('year').totalprod.mean().reset_index()

X = prod_by_year['year']
X = X.values.reshape(-1, 1)
y = prod_by_year['totalprod']

X_future = np.array(range(2013, 2051))
X_future = X_future.reshape(-1, 1)

regr = linear_model.LinearRegression()
regr.fit(X, y)
print(regr.coef_[0])

y_predict = regr.predict(X)
future_predict = regr.predict(X_future)

plt.scatter(X, y, color='blue')  # Scatter plot of actual data
plt.plot(X, y_predict, color='orange')  # Line plot of predictions
plt.plot(X_future, future_predict, color='red')  # Line plot of future predictions
plt.show()
