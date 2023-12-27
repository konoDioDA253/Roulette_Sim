"""
Author: Ilwad Issa
Description: 
This Python script simulates betting on odd numbers in a standard roulette game where the numbers range from 1 to 36. 
The simulation involves num_sets sets of num_simulations_per_set spins each, with a betting amount of $bet on odd numbers. 
It calculates the mean gain/loss for each set of spins and visualizes the frequency distribution of these mean gains/losses.
We can observe that the average gain is generally average as it follows a normal distribution of mean -0.26 for bets of 10$.
The moral of the story : casino always wins on the long run.
Date : 26/12/2023
"""

import random
import matplotlib.pyplot as plt
from collections import Counter

def roulette_spin():
    return random.randint(0, 36)  # Simulating numbers on a 37-number roulette wheel

def parity_check(number):
    return number % 2 == 0 and number != 0   # Check if number is even
    # return number % 2 != 0   # Check if number is odd

def simulate_roulette(num_spins, bet_amount):
    gains = []

    for _ in range(num_spins):
        spin_result = roulette_spin()

        if parity_check(spin_result):
            gains.append(bet_amount)  # If the result is even/odd, win the bet amount
        else:
            gains.append(-bet_amount)  # If not, lose the bet amount

    return sum(gains) / num_spins  # Return the mean gain for these spins

# Simulating 100000 sets of 100 spins each
num_simulations_per_set = 100
num_sets = 100000
bet = 10

mean_gains_over_sets = []

for _ in range(num_sets):
    mean_gain = simulate_roulette(num_simulations_per_set, bet)
    mean_gains_over_sets.append(mean_gain)

# Count the frequency of each mean gain
mean_gain_counts = dict(Counter(mean_gains_over_sets))

# Plotting the frequency of mean gains
plt.bar(mean_gain_counts.keys(), mean_gain_counts.values(), color='skyblue')

# Calculate the overall mean gain
overall_mean_gain = sum(mean_gains_over_sets) / num_sets

# Plotting the overall mean gain as a horizontal line
plt.axvline(x=overall_mean_gain, color='red', linestyle='--', label=f"Overall Mean: {overall_mean_gain:.2f}")
plt.xlabel('Mean Gain/Loss')
plt.ylabel('Frequency')
plt.title(f'Mean Gain/Loss over {num_sets} Simulation Sets of {num_simulations_per_set} Spins on Odd Numbers')
plt.legend()
plt.grid(axis='y')

# Setting y-axis limits to display the entire frequency range
plt.ylim(0, max(mean_gain_counts.values()) + 50)
plt.savefig(f"roulette_{num_sets}_sets_{num_simulations_per_set}_odd_numbers.png")

plt.show()
