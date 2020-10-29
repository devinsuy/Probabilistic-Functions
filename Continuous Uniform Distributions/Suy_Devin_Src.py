from scipy.stats import uniform as uni
from collections import OrderedDict
from matplotlib import pyplot as plt
import numpy as np
import random 

def psuedo_rand(a=1, b=10, n=1000000):
    # Initialization
    occurrences = OrderedDict()
    rand_vals = [None] * n
    ptr = 0
    for num in range(a, b+1): occurrences[num] = 0
    
    # Randomly generate n values [a,b] and map the number
    # to the amount of times it was generated
    for _ in range(n):
        rand_vals[ptr] = random.randint(a, b)
        ptr += 1
    for num in rand_vals: occurrences[num] += 1

    # Map each number to the percentage that it occurs,
    # the probability of each number in our sample
    pdf_pcts = {}
    for num, occurr in occurrences.items():
        pdf_pcts[num] = round(occurr/n, 4)

    # Calculate CDF values from our probabilities by
    # mapping the value to a running sum
    cdf_pcts = {}
    p_sum = 0
    for num, pct in pdf_pcts.items():
        p_sum += pct
        cdf_pcts[num] = round(p_sum, 4)

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

psuedo_rand()