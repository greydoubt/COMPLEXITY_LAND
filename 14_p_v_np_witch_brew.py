# brute-force solver that demonstrates how solutions can be found through brute force in the NP complexity class, while verification can be done efficiently in the P complexity class


'''In this code, the ingredients list represents the available ingredients possessed by the witches. The witches_order list specifies the order in which the witches take turns adding ingredients to the cauldron. The target_ingredients list represents the desired set of ingredients for the potion.

The verify_witch_cauldron() function takes these parameters as input and verifies if it is possible to create the desired potion by iterating through the witches in the specified order and checking if each witch possesses the required ingredient. If the ingredients are added in the correct order and the final cauldron matches the target set, the function returns a positive result indicating that the desired potion can be created.'''


import itertools

def find_witch_cauldron(ingredients, witches_order, target_ingredients):
    # Generate all possible permutations of ingredients
    all_permutations = list(itertools.permutations(ingredients))

    # Iterate through each permutation
    for permutation in all_permutations:
        cauldron = []
        index = 0

        # Check if the permutation matches the witches' order
        for witch in witches_order:
            # Check if the witch has the ingredient and add it to the cauldron
            if witch in permutation[index:]:
                cauldron.append(witch)
                index = permutation[index:].index(witch) + 1 + index

            # Check if the current cauldron matches the target ingredients
            if cauldron == target_ingredients:
                return permutation

    # If no solution is found, return None
    return None

# Example usage
ingredients = ["toadstool", "eye of newt", "bat wing", "snake scale"]
witches_order = ["toadstool", "eye of newt", "bat wing", "snake scale"]
target_ingredients = ["eye of newt", "bat wing", "snake scale"]

solution = find_witch_cauldron(ingredients, witches_order, target_ingredients)
if solution:
    print("Solution found! Ingredients in the order:", solution)
else:
    print("No solution found.")


'''In this code, the find_witch_cauldron() function takes the ingredients, witches_order, and target_ingredients as input. It generates all possible permutations of the ingredients using the itertools.permutations() function. It then iterates through each permutation and checks if it matches the witches' order. If a matching permutation is found, it adds the ingredients to the cauldron in the specified order and checks if it matches the target set. If a solution is found, the function returns the permutation as the solution.

By using brute force and generating all possible permutations, this solver demonstrates how solutions can be found in the NP complexity class. However, the verification step, which checks if the cauldron matches the target ingredients, can be done efficiently in the P complexity class, as it simply involves comparing two lists.'''