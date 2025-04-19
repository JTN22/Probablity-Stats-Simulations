# Scenario: A factory studies the relationship between hours of training (X) and productivity (Y).

# Data:
# Hours of Training: [1, 2, 3, 4, 5, 6, 7]
# Productivity: [10, 12, 15, 18, 22, 25, 28]

# Instructions:
# (a) Perform linear regression to fit the data and report the coefficients.
# (b) Test if the slope is equal to 3 at alpha = 0.05.
# (c) Predict productivity for 8 hours of training, including a 95% confidence interval.

# Libraries: statsmodels, matplotlib

import statsmodels.api as sm
import numpy as np
from scipy.stats import t

# Load Data
X = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([10, 12, 15, 18, 22, 25, 28])

# Linear regression
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
beta0, beta1 = model.params
beta0, beta1 

# Test slope
se_beta1 = model.bse[1]
t_stat = (beta1 - 3) / se_beta1
p_value = 2 * (1 - t.cdf(abs(t_stat), df=model.df_resid))
t_stat, p_value

# Prediction
X_new = np.array([[1, 8]])
prediction = model.get_prediction(X_new).summary_frame()
prediction

# Summary
model.summary()
