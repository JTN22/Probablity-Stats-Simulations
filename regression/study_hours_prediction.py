# Scenario: The number of hours studied (X) impacts test scores (Y).

# Instructions:
# 1. Fit a linear regression model Y = Beta0 + Beta1*X.
# 2. Use the provided dataset to estimate Beta0 and Beta1.
# 3. Predict the score for a student who studies 8 hours.
# Dataset: Hours: [1, 2, 3, 4, 5, 6], Scores: [50, 55, 60, 65, 70, 75]

# Libraries: numpy, statsmodels

import numpy as np
import statsmodels.api as sm

# Dataset
X = np.array([1, 2, 3, 4, 5, 6])
y = np.array([50, 55, 60, 65, 70, 75])

# Fit linear regression
X = sm.add_constant(X)  # Add intercept
model = sm.OLS(y, X).fit()

# Coefficients
beta0, beta1 = model.params

# Predict score for 8 hours of study
x0 = 8
predicted_score = beta0 + beta1 * x0

print(model.summary())
print(f"Predicted score for 8 hours: {predicted_score}")
