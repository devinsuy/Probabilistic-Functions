from math import sqrt
from collections import OrderedDict
from matplotlib import pyplot as plt
import numpy as np
import random
import statistics


# Calculate and return the confidence interval given the 
# mean, s_dev, sample size, and desired confidence %
def get_confidence(mu, sigma, n, confidence):
    confidence_vals = {.9 : 1.645, .95: 1.96, .9545: 2, .96: 2.05, .98: 2.33, .99 : 2.58, .9973: 3}
    return [
        mu + ((confidence_vals[confidence] * sigma) / sqrt(n)), 
        mu - ((confidence_vals[confidence] * sigma) / sqrt(n))
    ]
    
# Assuming exact population parameters are given, randomly generate population
# of size N and sample values from n = [1:MAX_SAMPLE], calculate population
# means and plot along 95% and 99% confidence intervals
def sample_size_confidence(mu=100, sigma=12, N=1000000, MAX_SAMPLE=200):
    pop = list(np.random.normal(mu, sigma, N))

    # Sample values and map sample size -> to sample_mean, and 
    # sample size -> to [interval_95, interval_99] for values n = [1 : 200]
    sample_data = OrderedDict()
    sample_interval_95 = OrderedDict()
    sample_interval_99 = OrderedDict()

    for n in range(1, MAX_SAMPLE+1):
        sample_interval_95[n] = get_confidence(mu, sigma, n, 0.95)
        sample_interval_99[n] = get_confidence(mu, sigma, n, 0.99)
        sample_data[n] = statistics.mean(random.sample(pop, n))
    
    # Generate plots, along 95 percent confidence interval, then 99
    plt.scatter(sample_data.keys(), sample_data.values(), marker="x")
    plt.plot(sample_interval_95.keys(), sample_interval_95.values(), 'r', linestyle='dashed')
    plt.ylabel("X_Bar")
    plt.xlabel("Sample Size")
    plt.title("Sample Means and 95% Confidence Intervals (mu=" + str(mu) + ", sigma=" + str(sigma) + ", N=" + str(N) + ")")
    plt.show()
    plt.close()

    plt.scatter(sample_data.keys(), sample_data.values(), marker="x")
    plt.plot(sample_interval_99.keys(), sample_interval_99.values(), 'g', linestyle='dashed', )
    plt.ylabel("X_Bar")
    plt.xlabel("Sample Size")
    plt.title("Sample Means and 99% Confidence Intervals (mu=" + str(mu) + ", sigma=" + str(sigma) + ", N=" + str(N) + ")")
    plt.show()

sample_size_confidence()


