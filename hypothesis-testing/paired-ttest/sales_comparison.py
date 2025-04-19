# Task: Compare sales performance before and after a promotional campaign.

# Scenario: Sales data includes 'Pre_Campaign_Sales' and 'Post_Campaign_Sales'.

# Instructions:
# 1. Perform a paired t-test to determine if the campaign significantly increased sales.
# 2. Calculate and report the 95% confidence interval for the mean difference in sales.
# Libraries: scipy.stats, numpy

from scipy.stats import ttest_rel, t
import numpy as np

# Sales data
pre_sales = np.array([100, 120, 130, 140, 150])
post_sales = np.array([110, 130, 135, 145, 160])

# Paired t-test
t_stat, p_value = ttest_rel(post_sales, pre_sales)

# Confidence interval
mean_diff = np.mean(post_sales - pre_sales)
std_diff = np.std(post_sales - pre_sales, ddof=1)
n = len(post_sales)
confidence_interval = t.interval(0.95, n-1, loc=mean_diff, scale=std_diff/np.sqrt(n))

print(f"T-statistic: {t_stat}, P-value: {p_value}")
print(f"95% Confidence Interval: {confidence_interval}")
