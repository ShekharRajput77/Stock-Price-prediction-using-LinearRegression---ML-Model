# -*- coding: utf-8 -*-
"""Stock_Prediction_ML_Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16nvFjQylotJbuY5eTrJdPWI7uuRnRzT5
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from google.colab import files

uploaded = files.upload()
file_name = list(uploaded.keys())[0]

df = pd.read_csv(file_name)
print(df.head())

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

df['Volume'] = df['Volume'].str.replace(',', '', regex=True).astype(float)

df['Prev_Close'] = df['Close'].shift(1)

df.dropna(inplace=True)

X = df[['Prev_Close', 'Volume']]
Y = df['Close']

#Splitting the data into Training and testing sets
test_size = 0.2
split_index = int(len(df)*(1 - test_size))

X_train, X_test = X[:split_index], X[split_index:]
Y_train, Y_test = Y[:split_index], Y[split_index:]

#Model input
model = LinearRegression()
model.fit(X_train, Y_train)

#Based on the training of the data, predict the Y = Volume
Y_predict = model.predict(X_test)

mae = mean_absolute_error(Y_test, Y_predict)
mse = mean_squared_error(Y_test, Y_predict)
rmse = np.sqrt(mse)
r2 = r2_score(Y_test, Y_predict)

#Evaluated metrics
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")
print(f"R-Rooted Score: {r2}")


#Plot - Actual vs Prediction Prices
plt.figure(figsize=(12,6))
plt.plot(Y_test.index, Y_test, label = 'Actual Prices', color = 'Blue')
plt.plot(Y_test.index, Y_predict, label = 'Predicted Prices', color = 'Red', linestyle = 'dashed')
plt.xlabel('Date')
plt.ylabel('Stock Closing Price')
plt.title('prediction of stock prices using LinearRegression')
plt.legend()
plt.grid(True)
plt.show()

#Scatter Plot - Actual vs prediction Prices
plt.figure(figsize=(12,6))
plt.scatter(Y_test, Y_predict, color = 'blue', alpha=0.5)
plt.plot([min(Y_test), max(Y_test)], [min(Y_test), max(Y_test)], color = 'Green', linestyle = 'dashed')
plt.xlabel('Actual prices')
plt.ylabel('Predicted Prices')
plt.title('Actual Vs Predicted Prices')
plt.show()