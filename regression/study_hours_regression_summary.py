# Scenario: A dataset contains hours studied (X) and test scores (Y).

# Instructions:
# 1. Fit a simple linear regression model Y = Beta0 + Beta1*X.
# 2. Report the coefficients and R^2 value.
# 3. Predict the score for a student who studies 8 hours.
# Dataset: Hours: [1, 2, 3, 4, 5, 6], Scores: [50, 55, 60, 65, 70, 75]

# Libraries: numpy, statsmodels

import numpy as np
import statsmodels.api as sm

# Dataset
X = np.array([1, 2, 3, 4, 5, 6])
y = np.array([50, 55, 60, 65, 70, 75])

# Fit linear regression
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

# Prediction
x_new = 8
predicted_score = model.predict([1, x_new])[0]
print(f"Predicted score for 8 hours: {predicted_score}")
