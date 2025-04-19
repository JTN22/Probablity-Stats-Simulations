# Scenario: Analyze the following dataset of hours studied (X) and test scores (Y):
# X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Y = [50, 55, 60, 65, 70, 75, 80, 82, 84, 85]

# Instructions:
# (a) Perform a linear regression and report R².
# (b) Plot residuals to assess model fit.
# (c) Compute the confidence interval for the predicted score at X = 7.

# Libraries: statsmodels, matplotlib

import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

# Load Data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([50, 55, 60, 65, 70, 75, 80, 82, 84, 85])

# Linear regression
X_with_const = sm.add_constant(X)
model = sm.OLS(y, X_with_const).fit()
model.summary()

# Residual plot
residuals = model.resid
plt.scatter(X, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residual Plot')
plt.show()

# Confidence interval for prediction at X=7
X_new = np.array([[1, 7]])
prediction = model.get_prediction(X_new).summary_frame()
prediction
