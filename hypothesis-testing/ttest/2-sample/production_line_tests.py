# Scenario: A machine produces items with weights that are normally distributed. Two production lines are tested with the following data:

# Line 1: [50.1, 50.2, 49.9, 50.3, 50.0, 50.1, 50.2, 50.4, 49.8, 50.0]
# Line 2: [50.0, 49.9, 50.1, 49.8, 49.9, 50.0, 49.7, 50.2, 50.1, 50.3]

# Instructions:
# (a) Test whether the means of the two lines are equal (two-sample t-test, equal variances).
# (b) Test whether the variances are equal (F-test).
# (c) If variances differ, perform Welch's t-test.

# Libraries: scipy.stats

from scipy.stats import ttest_ind, f_oneway

# Load Data
line1 = [50.1, 50.2, 49.9, 50.3, 50.0, 50.1, 50.2, 50.4, 49.8, 50.0]
line2 = [50.0, 49.9, 50.1, 49.8, 49.9, 50.0, 49.7, 50.2, 50.1, 50.3]

# Two-sample t-test (equal variances)
t_stat, p_value = ttest_ind(line1, line2, equal_var=True)
t_stat, p_value

# F-test for variances
f_stat, f_p_value = f_oneway(line1, line2)
f_stat, f_p_value

# Welch's t-test
t_stat_welch, p_value_welch = ttest_ind(line1, line2, equal_var=False)
t_stat_welch, p_value_welch
