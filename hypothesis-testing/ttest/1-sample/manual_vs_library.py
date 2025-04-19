# Scenario: A sample of size 25 has a mean of 50 and a standard deviation of 5. Test H0: mu = 48.

# Instructions:
# 1. Construct the formula for the t-statistic.
# 2. Compute the t-statistic step by step.
# 3. Compare the result with a library-based t-test.
# Libraries: scipy.stats

from scipy.stats import t

# Parameters
sample_mean = 50
sample_std = 5
n = 25
mu = 48

# T-statistic
t_statistic = (sample_mean - mu) / (sample_std / np.sqrt(n))

# P-value
p_value = 2 * (1 - t.cdf(abs(t_statistic), df=n-1))

print(f"T-statistic: {t_statistic}, P-value: {p_value}")
