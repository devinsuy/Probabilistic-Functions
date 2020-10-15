import random

'''
A certain population consists of N=1000 people. 500 of them support party A; 300 of them
support party B; and 200 support party C. A group of 4 people is chosen at random from the
population. What is the probability that all persons in the group support {A, B, C}
'''

# Returns True if the randomly selected supporters all
# hold the same party affiliation, False otherwise
def full_support(sample):

    return len(set(sample)) == 1

def party_support(N=1000, A=500, B=300, C=200, group=4, trials=10000):
    # Create the population with the given supporter values
    population = []
    for _ in range(A): population.append("A")
    for _ in range(B): population.append("B")
    for _ in range(C): population.append("C")

    # Shuffle the population for randomized distribution
    for _ in range(500): random.shuffle(population)
    
    # Randomly select group amount from the population, log the amount
    # of times the entire selection contains all A, B, or C supporters
    support_count = {'A' : 0, 'B' : 0, 'C' : 0}
    for _ in range(trials):
        sample = random.sample(population, group)
        # The sample is entirely affiliated with a single party, increment its count
        if full_support(sample): support_count[sample[0]] += 1

    # Output the sampled probability of each party having unanimous support from our trials
    print("Results\n-------")
    print("Number of samples:", trials)
    print("Population size:", N)
    print("Number of A supporters:", A)
    print("   Probability of full A support", round(support_count['A']/N, 4))
    print("Number of B supporters:", B)
    print("   Probability of full B support", round(support_count['B']/N, 4))
    print("Number of C supporters:", C)
    print("   Probability of full C support", round(support_count['C']/N, 4))

party_support()