import matplotlib.pyplot as plt
import numpy as np
import random
import math

# Run a nCr calculation
def combinations(n, r):
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))

def four_kind():
    # The number of possible ways to draw 6 cards
    num_hands = combinations(52, 6)
    
    # There are 13 cards we could possibly get four of a kind with:
    # 2,3,4,5,6,7,8,9,10,J,Q,K,A
    num_cards = 13

    # We are interested in drawing 4 of a kind but 2 cards will still remain, 
    # 52-4 = 48, there are 48C2 ways to draw the remaining 2 cards
    remaining_draws = combinations(48, 2)

    # There are only four of each card in the 52 deck, meaning there is only one
    # possible way to get four-of-a-kind for a given card
    four_kind_hands = 1 * num_cards * remaining_draws 
    probability = round(four_kind_hands / num_hands, 6)

    # Output results
    print("Results\n-------")
    print("   Number of possible four-of-a-kind hands:", four_kind_hands)
    print("   Total number of possible hands:", num_hands)
    print("   Probability of drawing a four-of-a-kind hand:", probability)

four_kind()


def exact_tosses(N=100000, target_freq=35):
    exact_count = 0
    heads_reached = []
    # Perform N experiments in which 100 coin flips are simulated in each
    for _ in range(N):
        num_heads = 0
        # Perform "coin flips" where a value of False represents tails
        for _ in range(100):
            # Let a boolean True value represent "heads" as result of flip 
            if random.choice([True, False]): num_heads += 1
        heads_reached.append(num_heads)

        # Trial of experiment yielded exactly the correct number of heads
        # log the count, before advancing to next trial
        if num_heads == target_freq: exact_count += 1
        
    # Calculate and output coin flip data
    print("Results\n-------")
    print("Target Number of Heads:", target_freq)
    print("   Average Number of Heads:", round(sum(heads_reached) / N, 3))
    print("   Number of trials with exactly", target_freq, "heads:", exact_count)
    print("   Probability of getting exactly", target_freq, "heads:", round(exact_count/N, 4))

    # Create histogram
    plt.hist(heads_reached)
    plt.title("Number of Heads Achieved in 100,000 Trials of 100 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Number of Occurrences")
    plt.show()

# exact_tosses()

def unfair_die(N=10000):
    # Maps the die value to the amount of times that it 
    # should appear (out of 100) from the given probabilities
    occurences = {
        1 : 10,
        2 : 15,
        3 : 30,
        4 : 25,
        5 : 5,
        6 : 15 
    }

    # Populate the die with 100 options proportional to
    # the probability of each die value occurring
    die = []
    for die_val, die_freq in occurences.items():
        # For each die value, it should appear die_freq 
        # amount of times out of 100 possible total
        for _ in range(die_freq): die.append(die_val)

    # Randomize our "die" to equally distribute values
    for _ in range(10000): random.shuffle(die)

    # Perform N "rolls" by randomly selecting a value on
    # the die, log the result of each roll
    roll_vals = []
    for _ in range(N): roll_vals.append(die[random.randint(0, 99)]) 

    # Create stem plot
    hist, bin_edges = np.histogram(np.asarray(roll_vals), bins=range(1,8))
    plt.stem(bin_edges[0:6], hist)
    plt.title("Stem Plot - 10,000 Rolls of A Unfair Die")
    plt.xlabel("Value of Roll")
    plt.ylabel("Frequency")
    plt.show()

# unfair_die()

def rolls_to_target(N=100000, target_val=7):
    num_rolls_needed = []
    # Perform N trials
    for _ in range(N):
        roll_count = 0
        while True:
            # Perform "roll" of two dice, track the roll count
            roll_val = random.randint(1, 6) + random.randint(1, 6)
            roll_count += 1

            # Number of rolls exceeded, discard 
            if roll_count > 60: break 

            # Target value reached, save the amount of rolls required
            if roll_val == 7:
                num_rolls_needed.append(roll_count)
                break

    # Calculate and output roll data
    avg_rolls = round(sum(num_rolls_needed) / N, 3)
    min_roll = min(num_rolls_needed)
    max_roll = max(num_rolls_needed)
    print("Results\n-------")
    print("Target value:", target_val)
    print("   Average rolls required:", avg_rolls)
    print("   Minimum number of rolls:", min_roll)
    print("   Maximum number of rolls:", max_roll)
    
    # Create histogram
    plt.hist(np.asarray(num_rolls_needed), bins=range(1,max_roll))    
    plt.title("Number of Dice Rolls to Reach Value 7")
    plt.xlabel("Number of Rolls")
    plt.ylabel("Number of Occurrences")
    plt.show()

# rolls_to_target()
