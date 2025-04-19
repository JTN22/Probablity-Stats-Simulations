# Perform a one-sample t-test.

# Instructions:
# 1. Test if the mean of the dataset [2.1, 2.5, 2.8, 3.0, 3.2] differs significantly from μ_0 = 3.
# 2. Use a significance level of α = 0.05.
# Libraries: scipy.stats

from scipy.stats import ttest_1samp

data = [2.1, 2.5, 2.8, 3.0, 3.2]
mu_0 = 3

# Perform t-test 
t_stat, p_val = ttest_1samp(data, mu_0)
print(f'T-statistic: {t_stat}, P-value: {p_val}')

if p_val < 0.05:
    print('Reject the null hypothesis')
else:
    print('Fail to reject the null hypothesis')
