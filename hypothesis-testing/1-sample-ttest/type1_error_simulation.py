# Scenario: A factory produces items with a mean weight of 100g and standard deviation of 5g. You sample 30 items.

# Instructions:
# 1. Construct the test statistic formula to test if the sample mean is significantly different from 100g.
# 2. Write a Python function to compute the p-value given a sample.
# 3. Simulate 1,000 samples and count how many reject the null hypothesis at alpha=0.05.
# Libraries: numpy, scipy.stats

from scipy.stats import t
import numpy as np

# Construct test statistic formula
def test_statistic(sample, mu_0):
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    n = len(sample)
    t_stat = (sample_mean - mu_0) / (sample_std / np.sqrt(n))
    return t_stat

# Simulate samples
mu_0 = 100
sample_size = 30
alpha = 0.05
rejects = 0

for _ in range(1000):
    sample = np.random.normal(100, 5, sample_size)
    t_stat = test_statistic(sample, mu_0)
    p_value = 2 * (1 - t.cdf(abs(t_stat), df=sample_size - 1))
    if p_value < alpha:
        rejects += 1

print(f"Proportion of rejected null hypotheses: {rejects / 1000}")
