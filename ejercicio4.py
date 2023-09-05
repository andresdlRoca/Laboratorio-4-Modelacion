import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Function for discrete distribution (Poisson)
def poisson_sample(n, lamb):
    return np.random.poisson(lamb, n)

# Function for continuous distribution (Exponential)
def exponential_sample(n, lamb):
    return np.random.exponential(1/lamb, n)

def central_limit_theorem(sample_func, n_values, N_values, mu, sigma, title):
    for N in N_values:
        plt.figure(figsize=(15, 10))
        plt.suptitle(f'{title} for N = {N}')
        
        for i, n in enumerate(n_values):
            means = []
            for _ in range(N):
                sample = sample_func(n, mu)  
                sn = np.mean(sample)
                centered_sn = (sn - mu) / (sigma / np.sqrt(n))
                means.append(centered_sn)
            
            x = np.linspace(-4, 4, 100)

            # Plot histogram
            plt.subplot(2, len(n_values), i+1)
            plt.hist(means, bins=50, density=True)
            plt.plot(x, norm.pdf(x, 0, 1), 'r', lw=2)
            plt.title(f'n = {n}')

            # Plot CDF
            plt.subplot(2, len(n_values), len(n_values) + i + 1)
            plt.hist(means, bins=50, density=True, cumulative=True, alpha=0.6)
            plt.plot(x, norm.cdf(x, 0, 1), 'r', lw=2)

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()

# Discrete case: Poisson distribution with lambda = 10
lamb_poisson = 10
mu_poisson = lamb_poisson  # mean
sigma_poisson = np.sqrt(lamb_poisson)  # standard deviation
n_values = [20, 40, 60, 80, 100]
N_values = [50, 100, 1000, 10000]

central_limit_theorem(poisson_sample, n_values, N_values, mu_poisson, sigma_poisson, 'Poisson Distribution')

# Continuous case: Exponential distribution with lambda = 2
lamb_exp = 2
mu_exp = 1 / lamb_exp  # mean
sigma_exp = 1 / lamb_exp  # standard deviation

central_limit_theorem(exponential_sample, n_values, N_values, mu_exp, sigma_exp, 'Exponential Distribution')
