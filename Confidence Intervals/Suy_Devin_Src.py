from math import sqrt
from collections import OrderedDict, defaultdict
from matplotlib import pyplot as plt
import numpy as np
import random
import statistics

# Using normal distr, calculate and return the confidence interval 
# given the mean, s_dev, sample size, and desired confidence %
def get_confidence_z(mu, sigma, n, confidence):
    confidence_vals = {.9 : 1.645, .95: 1.96, .9545: 2, .96: 2.05, .98: 2.33, .99 : 2.58, .9973: 3}
    z_score = confidence_vals[confidence]

    return [
        mu - ((z_score * sigma) / sqrt(n)),
        mu + ((z_score * sigma) / sqrt(n)) 
    ]

# Using t distr, calculate and return the confidence interval 
# given the mean, s_dev, sample size, and desired confidence %
def get_confidence_t(mu, sigma, n, confidence):
    # Values from t table using v=n-1 dof
    studT_95 = {5 : 2.78, 40: 2.02, 120 : 1.98}
    studT_99 = {5 : 4.6, 40: 2.71, 120: 2.62}

    if confidence == .95 and n in [5,40,120]: 
        t_score = studT_95[n]
    elif confidence == .99 and n in [5,40,120]:
        t_score = studT_99[n]
    else: return -1

    return [
        mu - ((t_score * sigma) / sqrt(n)),
        mu + ((t_score * sigma) / sqrt(n)) 
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
        sample_interval_95[n] = get_confidence_z(mu, sigma, n, 0.95)
        sample_interval_99[n] = get_confidence_z(mu, sigma, n, 0.99)
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


def normal_studT(mu=100, sigma=12, N=1000000, num_trials=10000, n_vals=[5,40,120]):
    pop = list(np.random.normal(mu, sigma, N))

    # Map the sample size n to the amount of successful trials
    z_success_95 = OrderedDict([(5, 0), (40,0), (120,0)])
    z_success_99 = OrderedDict([(5, 0), (40,0), (120,0)])
    t_success_95 = OrderedDict([(5, 0), (40,0), (120,0)])
    t_success_99 = OrderedDict([(5, 0), (40,0), (120,0)])

    # Conduct trials, logging the amount of "successes"
    for _ in range(num_trials):
        for n in n_vals:
            # Sample data and calculate parameters
            sample = random.sample(pop, n)
            sample_mean = statistics.mean(sample)
            sample_sdev = statistics.stdev(sample)
            
            # Calculate intervals [low, high]
            z_95 = get_confidence_z(sample_mean, sample_sdev, n, confidence=.95)
            z_99 = get_confidence_z(sample_mean, sample_sdev, n, confidence=.99)
            t_95 = get_confidence_t(sample_mean, sample_sdev, n, confidence=.95)
            t_99 = get_confidence_t(sample_mean, sample_sdev, n, confidence=.99)

            # Check if trial was success (whether or not the mu falls 
            # within intervals), increment count if so
            if (z_95[0] <= mu) and (mu <= z_95[1]): z_success_95[n] += 1
            if (z_99[0] <= mu) and (mu <= z_99[1]): z_success_99[n] += 1
            if (t_95[0] <= mu) and (mu <= t_95[1]): t_success_95[n] += 1
            if (t_99[0] <= mu) and (mu <= t_99[1]): t_success_99[n] += 1

    # Output results of simulation
    print("RESULTS\n-------\n")
    print("Normal distribution, 95% confidence:")
    for n, success_count in z_success_95.items():
        print("   n=" + str(n) + ": Success rate " + str(round(success_count/10000, 3)))
    print("\nNormal distribution, 99% confidence:")
    for n, success_count in z_success_99.items():
        print("   n=" + str(n) + ": Success rate " + str(round(success_count/10000, 3)))
    print("\nT distribution, 95% confidence:")
    for n, success_count in t_success_95.items():
        print("   n=" + str(n) + ": Success rate " + str(round(success_count/10000, 3)))
    print("\nT distribution, 99% confidence:")
    for n, success_count in t_success_99.items():
        print("   n=" + str(n) + ": Success rate " + str(round(success_count/10000, 3)))

normal_studT()