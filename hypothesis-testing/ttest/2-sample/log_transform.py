# Scenario: A researcher measures the height (X) of plants under two conditions and applies a transformation Y = log(X).

# Data:
# Condition A: [10, 12, 14, 15, 16, 18, 19]
# Condition B: [9, 11, 13, 14, 15, 17, 18]

# Instructions:
# (a) Test if the means of the transformed heights are equal at alpha = 0.01.
# (b) Verify normality of the transformed data.
# (c) Compute the 95% confidence interval for the mean of Condition A.

# Libraries: scipy.stats, numpy

import numpy as np
from scipy.stats import ttest_ind, shapiro

# Load Data
condition_a = [10, 12, 14, 15, 16, 18, 19]
condition_b = [9, 11, 13, 14, 15, 17, 18]
log_a = np.log(condition_a)
log_b = np.log(condition_b)

# T-test
t_stat, p_value = ttest_ind(log_a, log_b)
t_stat, p_value

# Normality test
shapiro_a = shapiro(log_a)
shapiro_b = shapiro(log_b)

shapiro_a, shapiro_b

# Confidence interval
mean_a, std_a = np.mean(log_a), np.std(log_a, ddof=1)
n_a = len(log_a)
ci_lower = mean_a - 1.96 * std_a / np.sqrt(n_a)
ci_upper = mean_a + 1.96 * std_a / np.sqrt(n_a)

ci_lower, ci_upper
