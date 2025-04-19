# Scenario: A machine produces items with two different settings. The weights of items produced under these settings are assumed to follow normal distributions.

# Data:
# Setting 1: [52.1, 50.9, 51.4, 52.5, 50.3, 51.7, 50.8, 51.9, 52.3, 50.6]
# Setting 2: [51.2, 50.5, 51.0, 50.7, 51.3, 50.9, 51.6, 50.4, 51.1, 51.0]

# Instructions:
# (a) Test whether the means of the two settings are equal, assuming equal variances.
# (b) Test the same hypothesis, assuming unequal variances.
# (c) Compute and interpret the p-value and critical value for both tests.

# Libraries: scipy.stats

import numpy as np 
from scipy.stats import ttest_ind

# Load data 
setting1 = [52.1, 50.9, 51.4, 52.5, 50.3, 51.7, 50.8, 51.9, 52.3, 50.6]
setting2 = [51.2, 50.5, 51.0, 50.7, 51.3, 50.9, 51.6, 50.4, 51.1, 51.0]

# Equal variances
t_stat_equal, p_val_equal = ttest_ind(setting1, setting2, equal_var=True)
t_stat_equal, p_val_equal

# Unequal variances 
t_stat_unequal, p_val_unequal = ttest_ind(setting1, setting2, equal_var=False)
t_stat_unequal, p_val_unequal
