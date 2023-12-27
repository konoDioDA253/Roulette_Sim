import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6)  # Simulating a standard six-sided dice

def roll_multiple_dice(num_dice):
    return sum(roll_dice() for _ in range(num_dice))

# Simulate rolling multiple dice 100 times and summing the results
num_rolls = 1000
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
plt.title(f'Sum of {num_dice} Dice Rolling Frequency for {num_rolls} Rolls')
plt.xticks(possible_sums)
plt.grid(axis='y')
plt.show()
