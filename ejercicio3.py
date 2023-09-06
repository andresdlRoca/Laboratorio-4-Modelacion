import numpy as np
from scipy.special import erf

def inverse_transform_sampling(u):
    valid_range = 2*u/np.sqrt(np.pi) - 1
    valid_range = np.clip(valid_range, 1e-10, 1.0)  # Ensure values are within [1e-10, 1]
    return np.sqrt(-np.log(valid_range))

def integral_estimate(N):
    u_values = np.random.rand(N)
    x_values = inverse_transform_sampling(u_values)
    f_values = x_values * np.exp(-x_values**2)
    estimate = np.mean(f_values)
    return estimate

N = 1000000  # Number of samples
result = integral_estimate(N)
print("Estimated value of the integral:", result)
