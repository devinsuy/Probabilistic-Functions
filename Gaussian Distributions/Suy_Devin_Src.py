from scipy import stats
from math import erf, floor, ceil, sqrt, pi, e
from matplotlib import pyplot as plt
from collections import OrderedDict
import numpy as np

'''
----------------------------
Normal Gaussian Distribution
----------------------------
'''
# Implementation of probability density function f(x) 
def pdf(x, mu=0, var=1):
    exponent = (-1 * pow((x-mu), 2)) / (2 * var)
    return (1 / sqrt(2*pi*var)) * pow(e, exponent)

# Implementation of cumulative distribution function F(x)
def cdf(x, mu=0, var=1):
    return 0.5 + (0.5 * erf((x-mu) / sqrt(2*var)))

# Verify values obtained against scipy.stats.normal module
def show_verification():
    print("PDF Implementation\n------------------")
    print("Probability Density Function @ x=1, mu=0, variance=1")
    print("   Using self implementation :", pdf(1))
    print("   Using scipy.stats.norm.pdf:", stats.norm.pdf(1))

    print("\nCDF Implementation\n------------------")
    print("Cumulative Distribution Function @ x=1, mu=0, variance=1")
    print("   Using self implementation :", cdf(1))
    print("   Using scipy.stats.norm.cdf:", stats.norm.cdf(1))

# show_verification()


# Given a range [start_val, end_val] returns a data dictionary
# mapping input -> pdf/cdf output vals for each val in the range 
def get_plot(start_val, end_val, use_pdf=True, mu=0, var=1):
    output = {}
    # Map using probability density function
    if use_pdf:
        for val in range(start_val, end_val+1): output[val] = pdf(val, mu, var)
        
    # Map values using cumulative distribution function
    else:
        for val in range(start_val, end_val+1): output[val] = cdf(val, mu, var)

    return output 

# Generate pdf/cdf plots for the specified (mu, variance) pairs
def generate_all_plots(start_val=-6, end_val=6):
    # Maps argument ID to mu, variance arguments
    mu_var = {
        0 : [0,1], 1 : [0, 0.1], 2 : [0, 0.01], 3 : [-3, 1], 4 : [-3, 0.1], 5 : [-3, 0.01]
    }
    # Maps mu_var argument ID to the corresponding plot values
    plot_vals_pdf = OrderedDict()
    plot_vals_cdf = OrderedDict()
    x_vals = [i for i in range(start_val, end_val+1)]

    # Generate plots for each of our mu, variance settings
    for i in range(len(mu_var)):
        params = mu_var[i]
        plot_vals_pdf[i] = get_plot(start_val, end_val, use_pdf=True, mu=params[0], var=params[1])
        plot_vals_cdf[i] = get_plot(start_val, end_val, use_pdf=False, mu=params[0], var=params[1])

    # Plot PDF results for each parameter
    for i in range(len(mu_var)):
        mu, var = mu_var[i]
        plt.plot(x_vals, plot_vals_pdf[i].values(), label=("mu=" + str(mu) + ", var=" + str(var)))
    plt.title("Probability Density Function Over [" + str(start_val) + ", " + str(end_val) + "]")
    plt.xlabel("Interval Values")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()

    # Plot CDF results for each parameter
    for i in range(len(mu_var)):
        mu, var = mu_var[i]
        plt.plot(x_vals, plot_vals_cdf[i].values(), label=("mu=" + str(mu) + ", var=" + str(var)))
    plt.title("Cumulative Distribution Function Over [" + str(start_val) + ", " + str(end_val) + "]")
    plt.xlabel("Interval Values")
    plt.ylabel("F(x)")
    plt.legend()
    plt.show()

# generate_all_plots()



'''
---------------------
Central Limit Theorem
---------------------
'''

# Returns the mean of uniform distribution over [a,b]
def uniform_mean(a, b):
    return round(0.5*(a+b), 3)

# Return the standard deviation over the uniform distr
def uniform_sdev(a, b):
    return round(sqrt((1/12) * pow(b-a, 2)), 3)

# Display the mean and sdev of a single book (cm) over [a,b]
def single_book(a=1, b=3):
    print("For A Single Book Over [" + str(a) + "," + str(b) + "]" 
    + "\n----------------------------")
    print("   Mean:", uniform_mean(a,b), "cm")
    print("   Sdev:", uniform_sdev(a,b), "cm")

# single_book()


# For a stack of n books, return the mean thickness
def stack_mean(n, a, b):
    return round(n * uniform_mean(a,b), 3) 

# For a stack of n books, return the standard deviation thickness
def stack_sdev(n, a, b):
    return round(uniform_sdev(a,b) * sqrt(n), 3)

# Display the mean and sdev of a stack of books
def book_stack(n_vals=[1,5,15], a=1, b=3):
    print("Mean And Sdev Of Book Stack" + 
    "\n---------------------------")
    for n in n_vals:
        print("   Stack @ n=" + str(n) + " books:")
        print("      Sn Mean:", stack_mean(n, a, b), "cm")
        print("      Sn Sdev:", stack_sdev(n, a, b), "cm")

# book_stack()


# Perform N samples of size n to generate probability 
# histogram and plot of normal PDF f(x)
def run_simu_util(n, a=1, b=3, N=100000):
    mean = stack_mean(n, a, b)
    s_dev = stack_sdev(n, a, b)

    # Randomly sample n values from [a,b]
    s_vals = []
    for _ in range(N): s_vals.append(np.sum(np.random.uniform(a, b, n)))

    # Generate histogram bars
    hist, b_edges = np.histogram(a=s_vals, bins=np.linspace(n*a, n*b, 31), density=True)
    bar = (b_edges[:-1]+b_edges[1:]) / 2
    w = bar[1]-bar[0] 

    return [mean, s_dev, hist, b_edges, bar, w]

# Run the simulation for each n value
def run_book_simu(n_vals=[1,5,15], a=1, b=3, N=100000):
    plt_data = []
    for n in n_vals:
        mean, s_dev, hist, b_edges, bar, w = run_simu_util(n, a, b, N)

        # Plot results
        plt.bar(x=bar, height=hist, width=w, edgecolor='w')
        pdf_vals = [pdf(x, mu=mean, var=pow(s_dev,2)) for x in bar]
        plt.plot(bar, pdf_vals, 'r')
        plt.xlabel("Height of Book Stack (cm) for Size n=" + str(n) + " Books")
        plt.ylabel("Probability Density Function")
        plt.title("Book Stack Height PDF and Normal Distribution Over N=" + str(N) 
        + " Samples In [" + str(a) + "," + str(b) + "]")
        plt.show()

# run_book_simu()


'''
-------------------------------------------------------
Distribution of the sum of exponential random variables
-------------------------------------------------------
- A battery lasts an average of 𝛽 = 45 𝑑𝑎𝑦𝑠
- Batteries are purchased in a carton of 24
'''

# Generate the n values with the given beta in an exponential
# distribution, representing our "batteries" comprising a "carton"
def generate_carton(beta, n):
    return np.random.exponential(beta, n)

def run_carton_simu(beta=45, n=24, N=10000):
    # Run N simulations of cartons, track lifetime sum C
    C_vals = []
    for _ in range(N): C_vals.append(sum(generate_carton(beta, n)))

    # Central Limit: Calculate mean and s_dev for gaussian plot
    mean = n * beta
    s_dev = beta * sqrt(n)

    # Find the min and max values for bins
    min_val = float('inf')
    max_val = float('-inf')
    for c_val in C_vals:
        if c_val < min_val: min_val = c_val
        if c_val > max_val: max_val = c_val
    min_val = floor(min_val-1)
    max_val = ceil(max_val+1)
    print(min_val)

    # Plot PDF of carton lifetime f(c)
    plt.subplot(1,2,1)
    hist, b_edges = np.histogram(C_vals, bins=np.linspace(min_val, max_val), density=True)
    bar = (b_edges[:-1]+b_edges[1:]) / 2
    w = bar[1]-bar[0]
    plt.bar(x=bar, height=hist, width=w, edgecolor='w')

    # Plot normal distribution with calculated mean and s_dev
    norm_vals = [pdf(x, mu=mean, var=pow(s_dev,2)) for x in bar]
    plt.plot(bar, norm_vals, 'r')
    plt.xlabel("Lifetime of Carton of n=" + str(n) + " Batteries (days)")
    plt.ylabel("Probability Density Function")
    plt.title("Battery Carton Lifetime PDF f(x) and Normal Distribution")

    # Plot cumulative distribution function
    plt.subplot(1,2,2)
    cdf = np.cumsum(hist*w)
    plt.plot(np.linspace(min_val, max_val, len(cdf)), cdf)
    plt.xlabel("Lifetime of Carton of n=" + str(n) + " Batteries (days)")
    plt.ylabel("Cumulative Distribution Function F(x)")
    plt.title("Battery Carton Lifetime CDF F(x)")
    plt.show()

run_carton_simu()