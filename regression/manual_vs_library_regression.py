# Scenario: A dataset contains X = [1, 2, 3, 4] and Y = [2, 4, 6, 8].

# Instructions:
# 1. Derive the formulas for the regression coefficients Beta0 and Beta1.
# 2. Compute Beta0 and Beta1 step by step.
# 3. Verify the coefficients using a library.

# Libraries: numpy, statsmodels

import numpy as np
import statsmodels.api as sm

# Data
X = np.array([1, 2, 3, 4])
Y = np.array([2, 4, 6, 8])

# Formula for coefficients
n = len(X)
x_mean = np.mean(X)
y_mean = np.mean(Y)
beta1 = sum((X - x_mean) * (Y - y_mean)) / sum((X - x_mean)**2)
beta0 = y_mean - beta1 * x_mean

# Using statsmodels
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()

print(f"Beta0 (Manual): {beta0}, Beta1 (Manual): {beta1}")
print(model.summary())
