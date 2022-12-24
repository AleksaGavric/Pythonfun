import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv(
    "https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv"
)

prod_per_year = df.groupby("totalprod")

X = df["year"]
X = X.values.reshape(-1, 1)

y = df["totalprod"]

plt.scatter(y, X)
# plt.show()

regr = linear_model.LinearRegression()
regr.fit(X, y)

# print(regr.coef_, regr.intercept_)

y_predict = regr.predict(X)

plt.scatter(y_predict, X)
# plt.show()

X_future = np.array(range(2013, 2051))
X_future = X_future.reshape(-1, 1)

# print(X_future)

future_predict = regr.predict(X_future)

plt.scatter(future_predict, X_future)
plt.show()
