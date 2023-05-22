# The Witch's Cauldron

'''In the mystical forest, a group of witches gathers around a large cauldron to create powerful potions. Each witch possesses a unique set of ingredients, represented by a collection of items. To concoct a potion, the witches take turns adding one ingredient at a time to the cauldron.

The goal is to determine if it is possible to add a specific set of target ingredients to the cauldron using the available ingredients possessed by the witches, while adhering to certain rules.

Each witch can only add an ingredient that they possess to the cauldron, and once an ingredient is added, it cannot be removed. The order in which the witches take turns adding ingredients is fixed and must be followed. Additionally, the cauldron must contain the target set of ingredients exactly, without any additional items.

Your task is to determine whether it is possible to create the desired potion by adding the ingredients in the correct order and following the rules of the witches' gathering.

This problem falls into the complexity class of NP, as we can easily verify a proposed solution in polynomial time by checking if the ingredients are added in the correct order and if the final cauldron matches the target set.

To illustrate this concept, let's consider an example code that demonstrates the verification of a solution for the Witch's Cauldron problem:'''


def verify_witch_cauldron(ingredients, witches_order, target_ingredients):
    cauldron = []

    # Iterate through the witches in the specified order
    for witch in witches_order:
        # Check if the witch has the ingredient and add it to the cauldron
        if witch in ingredients:
            cauldron.append(witch)

        # Check if the current cauldron matches the target ingredients
        if cauldron == target_ingredients:
            return "The desired potion can be created!"

    # If the loop completes without finding a match, the potion cannot be created
    return "The desired potion cannot be created."

# Example usage
ingredients = ["toadstool", "eye of newt", "bat wing", "snake scale"]
witches_order = ["toadstool", "eye of newt", "bat wing", "snake scale"]
target_ingredients = ["eye of newt", "bat wing", "snake scale"]

result = verify_witch_cauldron(ingredients, witches_order, target_ingredients)
print(result)


'''
In this code, the ingredients list represents the available ingredients possessed by the witches. The witches_order list specifies the order in which the witches take turns adding ingredients to the cauldron. The target_ingredients list represents the desired set of ingredients for the potion.

The verify_witch_cauldron() function takes these parameters as input and verifies if it is possible to create the desired potion by iterating through the witches in the specified order and checking if each witch possesses the required ingredient. If the ingredients are added in the correct order and the final cauldron matches the target set, the function returns a positive result indicating that the desired potion can be created.
'''