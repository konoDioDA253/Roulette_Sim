"""
Author: Ilwad Issa
Description: 
This Python script simulates rolling two six-sided dice a specified number of times and calculates the sum of the dice outcomes. 
It then counts the frequency of each possible sum and generates a bar graph using matplotlib to visualize the distribution of the sums obtained.
A gaussian curv is deduced from the shape of the distribution that emerges from the sum of discrete binomial random variables, which is the core statement of the Central Limit Theorem.
Date : 26/12/2023
"""

import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6)  # Simulating a standard six-sided dice

def roll_multiple_dice(num_dice):
    return sum(roll_dice() for _ in range(num_dice))

# Simulate rolling multiple dice 100 times and summing the results
num_rolls = 100000
num_dice = 10  # Change this number to roll a different quantity of dice
results = []
for _ in range(num_rolls):
    total = roll_multiple_dice(num_dice)
    results.append(total)

# Count the frequency of each sum
possible_sums = list(range(num_dice, num_dice * 6 + 1))  # Possible sum range for given number of dice
frequency = {i: results.count(i) for i in possible_sums}

# Create a bar graph
plt.bar(frequency.keys(), frequency.values(), color='skyblue')
plt.xlabel('Sum of Dice')
plt.ylabel('Frequency')
plt.title(f'Sum of {num_dice} Dice for {num_rolls} Rolls')
plt.xticks(possible_sums)
plt.grid(axis='y')
plt.savefig(f"Sum_of_{num_dice}_dices_for_{num_rolls}_rolls.png")
plt.show()
