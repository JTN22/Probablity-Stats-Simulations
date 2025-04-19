# Task: Compare two employee work times.

# Scenario: Employee A's times are: [8, 9, 7.5, 8.2, 8.8] hours.
# Employee B's times are: [7.2, 8.1, 7.8, 8.5, 7.6] hours.

# Instructions:
# 1. Perform a two-sample t-test to see if the work times differ significantly.
# 2. Use a significance level of α = 0.05.
# Libraries: scipy.stats

from scipy.stats import ttest_ind

# Employee work times
times_A = [8, 9, 7.5, 8.2, 8.8]
times_B = [7.2, 8.1, 7.8, 8.5, 7.6]

# Two-sample t-test
t_stat, p_value = ttest_ind(times_A, times_B)

print(f"T-statistic: {t_stat}, P-value: {p_value}")
if p_value < 0.05:
    print("Reject the null hypothesis: Work times differ significantly.")
else:
    print("Fail to reject the null hypothesis: Work times do not differ significantly.")
