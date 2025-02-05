import sys
import matplotlib.pyplot as plt

def safe_input(prompt, cast_func=None):
    user_input = input(prompt)
    if user_input.lower() == "quit":
        print("Quitting the program... Goodbye!")
        sys.exit()
    if cast_func:
        try:
            return cast_func(user_input)
        except Exception:
            print("Invalid input. Please try again or type 'quit' to exit.")
            return safe_input(prompt, cast_func)
    return user_input

def calculate_tariff_effect(direct_effect, indirect_effects, weights, elasticities):
    weighted_indirect_effects = [
        weights[i] * indirect_effects[i] * elasticities[i+1]
        for i in range(len(indirect_effects))
    ]
    total_impact = direct_effect * elasticities[0] + sum(weighted_indirect_effects)
    return total_impact, [direct_effect * elasticities[0]] + weighted_indirect_effects

def plot_impact(sector_names, impacts):
    plt.figure(figsize=(10,5))
    plt.bar(sector_names, impacts, color=['red' if impact < 0 else 'blue' for impact in impacts])
    plt.axhline(0, color='black', linewidth=1)
    plt.title("Impact of Tariff on Different Sectors")
    plt.ylabel("Economic Impact")
    plt.xlabel("Sectors")
    plt.xticks(rotation=45)
    plt.show()

print("Advanced Economic Tariff Simulator")
print("This program calculates how tariffs on a sector affect the entire economy.")
print("It includes industry weight factors and elasticity to make the model more realistic.")
print("Type 'quit' at any prompt to exit.\n")

direct_effect = safe_input("How much does the main sector's profit change due to the tariff? (e.g., -5 for loss): ", float)
num_related_sectors = safe_input("How many related businesses are affected? (e.g., car manufacturing, construction): ", int)
sector_names = ["Main Sector"]
indirect_effects = []
weights = []
elasticities = []

elasticity_main = safe_input("Enter elasticity for the main sector (e.g., 1.0 - 2.0): ", float)
elasticities.append(elasticity_main)

for i in range(num_related_sectors):
    name = safe_input(f"Enter name of sector {i+1}: ")
    sector_names.append(name)
    effect = safe_input(f"Enter the impact on {name} (positive or negative): ", float)
    weight = safe_input(f"Enter weight (importance of {name} in the economy, e.g., 0.1 - 0.5): ", float)
    elasticity = safe_input(f"Enter elasticity for {name} (e.g., 1.0 - 2.0): ", float)
    indirect_effects.append(effect)
    weights.append(weight)
    elasticities.append(elasticity)

total_impact, adjusted_effects = calculate_tariff_effect(direct_effect, indirect_effects, weights, elasticities)
print(f"\nThe TOTAL impact of the tariff on the economy is: {total_impact:.2f}")
if total_impact < 0:
    print("Tariff caused an economic slowdown.")
elif total_impact > 0:
    print("Tariff boosted the economy.")
else:
    print("No overall economic change.")
plot_impact(sector_names, adjusted_effects)
