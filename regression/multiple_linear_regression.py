# Instructions:

# Load a CSV file with columns x1, x2, and y into a Pandas DataFrame.
# Fit a regression model: y = β_0 + β_1x_1 + β_2x_2.
# Output the coefficients β_0, β_1, β_2 and the model's R^2 score.
# Libraries: pandas, statsmodels or sklearn

import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load data
df = pd.read_csv('data.csv')
X = df[['x1', 'x2']]
y = df['y']

# Linear regression 
model = LinearRegression()
model.fit(X, y)

# Coefficients
beta0 = model.intercept_
beta1, beta2 = model.coef_

# R^2 score 
r2 = r2_score(y, model.predict(X))

print(f'Intercept: {beta0}, Coefficients: {beta1}, {beta2}, R^2: {r2}')
