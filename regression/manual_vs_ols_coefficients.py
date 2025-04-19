# Scenario: The sales of a product (Y) depend on advertising expenditure in TV (X1) and Social Media (X2).

# Instructions:
# 1. Derive the least squares estimators for the regression coefficients (Beta0, Beta1, Beta2).
# 2. Write Python code to fit a regression model and calculate these coefficients using a dataset.
# Libraries: numpy, statsmodels

import numpy as np
import statsmodels.api as sm

# Derive coefficients manually
X = np.array([[1, 100, 50], [1, 200, 80], [1, 300, 60]])  # Adding intercept term
y = np.array([20, 30, 25])

# Coefficients (Beta) = (X'X)^-1 X'y
beta = np.linalg.inv(X.T @ X) @ X.T @ y
print(f"Coefficients: {beta}")

# Verify using statsmodels
model = sm.OLS(y, X).fit()
print(model.summary())
