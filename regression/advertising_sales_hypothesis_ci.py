# Scenario: A company studies the relationship between advertising expenditure (X) and sales (Y).

# Data:
# Advertising ($): [100, 200, 300, 400, 500, 600, 700]
# Sales ($): [10, 20, 25, 35, 45, 40, 60]

# Instructions:
# (a) Perform a linear regression and report the coefficients Beta0 and Beta1.
# (b) Test the hypothesis that Beta1 = 0.5 at alpha = 0.05.
# (c) Predict sales when advertising is $800 and compute a 95% confidence interval for the prediction.

# Libraries: statsmodels, scipy.stats

import numpy as np 
import statsmodels.api as sm 
from scipy.stats import t 

# Load data
X = np.array([100, 200, 300, 400, 500, 600, 700])
y = np.array([10, 20, 25, 35, 45, 40, 60])

# Linear regression
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
beta0, beta1 = model.params
beta0, beta1

# Hypothesis test 
se_beta1 = model.bse[1]
t_stat = (beta1 - 0.5)/se_beta1
p_val = 2*(1 - t.cdf(abs(t_stat), df=model.df_resid))
p_val

# Prediction
X_new = np.array([1, 800])
prediction = model.get_prediction(X_new).summary_frame()
prediction

# Summary
model.summary()
