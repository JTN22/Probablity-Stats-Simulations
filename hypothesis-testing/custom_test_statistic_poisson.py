# Scenario: The number of defects in a factory follows a Poisson distribution with mean lambda. You collect a sample of size n and wish to test H0: lambda = 5.

# Instructions:
# 1. Derive the formula for the test statistic T = sqrt(n) * (X_bar - 5).
# 2. Construct a formula for the p-value assuming T follows a normal distribution under H0.
# 3. Simulate 100 samples, compute T for each, and calculate the proportion of p-values less than 0.05.
# Libraries: numpy, scipy.stats

import numpy as np
from scipy.stats import norm

# Derive T statistic and p-value
def compute_test_statistic(sample, lambda_):
    n = len(sample)
    X_bar = np.mean(sample)
    T = np.sqrt(n) * (X_bar - lambda_)
    return T

# Simulate samples
lambda_ = 5
n = 30
samples = [np.random.poisson(lambda_, n) for _ in range(100)]
p_values = [2 * (1 - norm.cdf(abs(compute_test_statistic(sample, lambda_)))) for sample in samples]
reject_proportion = np.mean([p < 0.05 for p in p_values])

print(f"Proportion of null hypothesis rejections: {reject_proportion}")
