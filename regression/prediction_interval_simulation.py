# Scenario: You have a simple linear regression model Y = Beta0 + Beta1*X + epsilon, where epsilon ~ N(0, sigma^2).

# Instructions:
# 1. Construct the formula for a 95% prediction interval at a given X=x0.
# 2. Given Beta0=2, Beta1=0.5, sigma=1, and x0=10, compute the prediction interval.
# 3. Simulate 100 predictions at x0=10 and verify the coverage of the interval.
# Libraries: numpy, scipy.stats

from scipy.stats import t
import numpy as np

# Prediction interval formula
def prediction_interval(beta0, beta1, sigma, x0, n):
    X = np.array([1, x0])
    variance = sigma**2 * (1 + 1 / n + (x0 - np.mean(X))**2 / np.sum((X - np.mean(X))**2))
    t_crit = t.ppf(0.975, df=n-2)
    interval = t_crit * np.sqrt(variance)
    return beta0 + beta1 * x0 - interval, beta0 + beta1 * x0 + interval

# Example values
beta0, beta1, sigma, x0, n = 2, 0.5, 1, 10, 100
interval = prediction_interval(beta0, beta1, sigma, x0, n)

print(f"Prediction interval: {interval}")
