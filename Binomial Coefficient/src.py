import random
import matplotlib.pyplot as plt

'''
A certain population consists of N=1000 people. 500 of them support party A; 300 of them
support party B; and 200 support party C. A group of 4 people is chosen at random from the
population. What is the probability that all persons in the group support {A, B, C}
'''

# Returns True if the randomly selected supporters all
# hold the same party affiliation, False otherwise
def full_support(sample): return len(set(sample)) == 1

def party_support(N=1000, A=500, B=300, C=200, group=4, trials=100000):
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
        # The sample is entirely affiliated, increment its count
        if full_support(sample): support_count[sample[0]] += 1
    
    # Calculate probabilities
    a_support = round(support_count['A']/trials, 5)
    b_support = round(support_count['B']/trials, 5)
    c_support = round(support_count['C']/trials, 5)

    # Output the sampled probability of each party having unanimous support from our trials
    print("Results\n-------")
    print("Number of samples:", trials)
    print("Population size:", N)
    print("Number of A supporters:", A)
    print("   Probability of full A support", a_support, 
        "(" + str(support_count['A']) + "/" + str(trials) + ")")
    print("Number of B supporters:", B)
    print("   Probability of full B support", b_support, 
        "("+ str(support_count['B']) + "/" + str(trials) + ")")
    print("Number of C supporters:", C)
    print("   Probability of full C support", c_support, 
        "(" + str(support_count['C']) + "/" + str(trials) + ")")

    # Generate plot
    plt.bar(x=['A','B','C'], height=[a_support, b_support, c_support])
    plt.title("Unanimous Party Support For Random Sample of Size=" 
        + str(group) + " From Population Size N=" + str(N) + " Over Trials=" + str(trials))
    plt.xlabel("Party Affiliation")
    plt.ylabel("Probability of Unanimous Support")
    plt.show()

# party_support()

'''
A class of 4n children contains 2n boys and 2n girls. A group of 2n children is chosen at random.
What is the probability that the group contains an equal number of boys and girls?
'''
# Returns True if the sample contains an equal number of boys and girls
# RECALL: a "boy" is represented by a boolean value of True
def has_equal(sample):
    counts = {'Boy' : 0, 'Girl': 0}
    for boy in sample:
        if not boy: counts['Girl'] += 1
        else: counts['Boy'] += 1 
    return counts['Boy'] == counts['Girl']

def class_select(select_scalar=2, boy_scalar=2, girl_scalar=2, N=10, trials=100000):
    # Let True represent a "boy", create population according to the ratios
    population = []
    for _ in range(boy_scalar*N): population.append(True)
    for _ in range(girl_scalar*N): population.append(False)
    
    # Shuffle the population for randomized distribution
    for _ in range(500): random.shuffle(population)

    # Randomly select select_scalar*N children trials amount of times, log the
    # amount of times the sample contains an equal amount of boys and girls 
    equal_count = 0
    for _ in range(trials):
        sample = random.sample(population, (select_scalar*N))
        if has_equal(sample): equal_count += 1
    p_equal = round(equal_count/trials, 5)

    # Output results
    print("Results\n-------")
    print("Amount of boys:", str(boy_scalar) + "n")
    print("Amount of girls:", str(girl_scalar) + "n")
    print("Selection size:", str(select_scalar) + "n")
    print("For values: n=" + str(N))
    print("Number of trials:", trials)
    print("\nProbability of equal distribution:", p_equal, 
        "(" + str(equal_count) + "/" + str(trials) + ")")

# class_select()

'''
In a lottery game, the player picks 4 numbers from a sequence of 1 through 20. At lottery
drawing, 4 balls are drawn at random from a box containing 20 balls numbered 1 through 20.
What is the probability that the player will win the lottery (i.e. getting 4 matches in any order)?
'''
def lottery(min_number=1, max_number=20, draw_size=4, trials=100000):
    # Generate randomized number pool
    number_pool = [i for i in range(min_number, max_number+1)]
    for _ in range(500): random.shuffle(number_pool)

    # For each trial, randomly select draw_size numbers for the player, then
    # draw_size numbers representing the the winning numbers
    win_count = 0
    for _ in range(trials):
        player = set(random.sample(number_pool, draw_size))
        winning = set(random.sample(number_pool, draw_size))
        # Sets are unordered, winning numbers can match in any order
        if player == winning: win_count += 1
    p_win = round(win_count/trials, 5)

    # Output results
    print("Results\n-------")
    print("Number pool: [" + str(min_number) + ", " + str(max_number) + "]") 
    print("Amount of numbers selected:", draw_size)
    print("Number of trials:", trials)
    print("\nProbability of lottery win:", p_win, 
        "(" + str(win_count) + "/" + str(trials) + ")")
    


lottery()