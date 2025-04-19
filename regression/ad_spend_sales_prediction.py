# Task: Fit and interpret a multiple regression model.

# Scenario: A company tracks their sales (y) based on ad spending on TV (x1) and social media (x2).

# Instructions:
# 1. Use the provided data to fit the regression model y = β_0 + β_1x_1 + β_2x_2.
# 2. Report the coefficients, p-values, and R^2 value.
# 3. Predict sales when TV spending = 1000 and social media spending = 500.
# Libraries: pandas, statsmodels

import pandas as pd
import statsmodels.api as sm

# Sample data
data = pd.DataFrame({
    'x1': [200, 300, 400, 500, 600],
    'x2': [50, 60, 70, 80, 90],
    'y': [20, 25, 30, 35, 40]
})

# Regression model
X = data[['x1', 'x2']]
X = sm.add_constant(X)
y = data['y']

model = sm.OLS(y, X).fit()
print(model.summary())

# Predict sales
predicted_sales = model.predict([1, 1000, 500])
print(f"Predicted Sales: {predicted_sales[0]}")
