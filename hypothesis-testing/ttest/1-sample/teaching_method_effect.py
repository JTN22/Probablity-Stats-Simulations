# Scenario: A researcher believes that a new teaching method improves test scores. The class average before the method was 70.

# Instructions:
# 1. Construct the formula for the test statistic when testing H0: mu = 70.
# 2. Simulate a dataset of 30 test scores after the method with mean=75 and std=10.
# 3. Perform the hypothesis test and interpret the p-value.
# Libraries: numpy, scipy.stats

import numpy as np
from scipy.stats import ttest_1samp

# Test statistic formula: t = (mean - mu) / (std / sqrt(n))
data = np.random.normal(75, 10, 30)
mu = 70

# Perform t-test
t_stat, p_value = ttest_1samp(data, mu)

print(f"T-statistic: {t_stat}, P-value: {p_value}")
if p_value < 0.05:
    print("Reject the null hypothesis: The teaching method improves scores.")
else:
    print("Fail to reject the null hypothesis.")
