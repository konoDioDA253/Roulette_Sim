import random
import matplotlib.pyplot as plt
import seaborn as sns

def roulette_spin():
    return random.randint(0, 36)  # Simulating numbers on a 37-number roulette wheel

def parity_check(number):
    return number % 2 == 0 and number != 0   # Check if number is even

def simulate_roulette(num_spins):
    gains = []

    for _ in range(num_spins):
        spin_result = roulette_spin()

        if parity_check(spin_result):
            gains.append(1)  # If the result is even/odd, the player wins 1
        else:
            gains.append(0)  # If not, the player wins 0

    return sum(gains) / num_spins  # Return the mean gain for these spins

# Simulating 100000 sets of 100 spins each
num_simulations_per_set = 100
num_sets = 100000

mean_gains_over_sets = []

for _ in range(num_sets):
    mean_gain = simulate_roulette(num_simulations_per_set)
    mean_gains_over_sets.append(mean_gain)

# Using Seaborn to plot kernel density estimation (KDE) instead of bar plot
sns.kdeplot(mean_gains_over_sets, color='skyblue', shade=True)

# Calculate the overall mean gain
overall_mean_gain = sum(mean_gains_over_sets) / num_sets

# Plotting the overall mean gain as a vertical line
plt.axvline(x=overall_mean_gain, color='red', linestyle='--', label=f"Overall Mean: {overall_mean_gain:.2f}")
plt.xlabel('Mean Gain/Loss')
plt.ylabel('Density')
plt.title(f'Distribution of Mean Gain/Loss over {num_sets} Sets of {num_simulations_per_set} Spins on Odd Numbers')
plt.legend()
plt.grid(axis='y')

plt.savefig(f"roulette_{num_sets}_sets_{num_simulations_per_set}_odd_numbers_smooth.png")

plt.show()
