# Scenario: A coin is flipped 100 times, resulting in 55 heads. You test if the coin is fair.

# Instructions:
# 1. State the null and alternative hypotheses.
# 2. Perform a hypothesis test at alpha = 0.05.
# 3. Compute the p-value and interpret the result.
# Libraries: scipy.stats

from scipy.stats import binomtest

# Parameters
n_flips = 100
n_heads = 55
alpha = 0.05

# Perform test
p_value = binomtest(n_heads, n_flips, p=0.5, alternative='two-sided').pvalue
print(f"P-value: {p_value}")
if float(p_value) < alpha:
    print("Reject the null hypothesis: The coin is not fair.")
else:
    print("Fail to reject the null hypothesis: The coin is fair.")
