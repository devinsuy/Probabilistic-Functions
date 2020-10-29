from scipy.stats import uniform as uni
from collections import OrderedDict
from matplotlib import pyplot as plt
import numpy as np
import random 

# Non uniform PDF and CDF using psuedo-randomization 
def psuedo_rand(a=1, b=10, n=1000000):
    # Initialization
    occurrences = OrderedDict()
    rand_vals = [None] * n
    ptr = 0
    for x in range(a, b+1): occurrences[x] = 0
    
    # Randomly generate n values [a,b] and map the number
    # to the amount of times it was generated
    for _ in range(n):
        rand_vals[ptr] = random.randint(a, b)
        ptr += 1
    for x in rand_vals: occurrences[x] += 1

    # Map each number to the percentage that it occurs,
    # the probability of each number in our sample
    pdf_pcts = {}
    for x, occurr in occurrences.items():
        pdf_pcts[x] = round(occurr/n, 4)

    # Calculate CDF values from our probabilities by
    # mapping the value to a running sum
    cdf_pcts = {}
    p_sum = 0
    for x, pct in pdf_pcts.items():
        p_sum += pct
        cdf_pcts[x] = round(p_sum, 4)

    # Output results
    print("Results\n-------")
    print("Using psuedo-randomization")
    print("Random values between [" + str(a) + ", " + str(b) + "]")
    print("Number of values selected:", n)
    print("PDF f(x):", pdf_pcts)
    print("CDF F(x):", cdf_pcts)

    # Plot PDF and CDF horizontally
    plt.subplot(1,2,1)
    plt.title("PDF (Psuedo-random) For [" + str(a) + ", " + str(b) + "] Over n=" + str(n) + " Trials")
    plt.plot(pdf_pcts.keys(), pdf_pcts.values(), 'r-')
    plt.xlabel("Interval Values")
    plt.ylabel("f(x)")

    plt.subplot(1,2,2)
    plt.title("CDF (Psuedo-random) For [" + str(a) + ", " + str(b) + "] Over n=" + str(n) + " Trials")
    plt.plot(cdf_pcts.keys(), cdf_pcts.values(), 'b-')
    plt.xlabel("Interval Values")
    plt.ylabel("F(x)")
    plt.show()

# psuedo_rand()


'''
A random variable that is uniformly distributed over the interval (a, b) follows the probability density
function (pdf) given by: 
    𝑓(𝑥; 𝑎, 𝑏) = 1/(𝑏−𝑎); 
    𝑎 < 𝑥 < 𝑏 

The cumulative distribution function (cdf) for a uniform random variable is:
    𝐹(𝑥) = {
                0           : 𝑥 ≤ 𝑎
                (𝑥−a)/(𝑏−𝑎) : 𝑎 < 𝑥 < 𝑏
                1           : 𝑥 ≥ 𝑏
            }
Python implementation for (a, b) = (1, 10)
'''
def uniform(a=1, b=10):
    # PDF map values to uniform distribution f(x)
    pdf_val = round(1/(b-a), 4)
    pdf_pcts = {}
    for x in range(a-1, b+2): 
        if x > a and x < b: pdf_pcts[x] = pdf_val
        else: pdf_pcts[x] = 0

    # CDF map values to uniform distrubtion F(x)
    cdf_pcts = {}
    for x in range(a-1, b+2):
        if x > a and x < b:
            cdf_pcts[x] = round((x-a)/(b-a), 4)
        elif x <= a:
            cdf_pcts[x] = 0
        elif x >= b:
            cdf_pcts[x] = 1

    # Output results
    print("Results\n-------")
    print("Uniform Implementation")
    print("Values on interval [" + str(a) + ", " + str(b) + "]")
    print("PDF f(x):", pdf_pcts)
    print("CDF F(x):", cdf_pcts)

    # Plot PDF and CDF horizontally
    plt.subplot(1,2,1)
    plt.title("Uniform Probability Density Function For [" + str(a) + ", " + str(b) + "]")
    plt.plot(pdf_pcts.keys(), pdf_pcts.values(), 'r-')
    plt.xlabel("Interval Values")
    plt.ylabel("f(x)")

    plt.subplot(1,2,2)
    plt.title("Cumulative Distribution Function For [" + str(a) + ", " + str(b) + "]")
    plt.plot(cdf_pcts.keys(), cdf_pcts.values(), 'b-')
    plt.xlabel("Interval Values")
    plt.ylabel("F(x)")
    plt.show()

uniform()
