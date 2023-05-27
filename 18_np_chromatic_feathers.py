# Vurt's Colorful Feathers

'''In the magical realm of Vurt, there exist enchanted feathers imbued with different colors. These feathers possess mystical properties and can be combined to create potent spells or access alternate dimensions of degenerate modality. However, combining feathers of certain colors can result in unpredictable outcomes, and the Vurtians want to ensure a harmonious combination of colors.

The goal is to determine whether a given set of colorful feathers can be combined in such a way that avoids the formation of certain color patterns specified by Ramsey theory.

Each feather in Vurt is assigned a color from a known palette of colors. The Vurtians want to avoid certain color patterns, which are represented by tuples of colors that should not appear together. These color patterns are defined based on Ramsey theory, which studies the emergence of certain combinatorial patterns in a set of objects.

Your task is to determine whether there exists a combination of feathers from the given set that avoids the specified color patterns.'''



from itertools import combinations

def check_feather_combination(feathers, forbidden_patterns):
    # Generate all possible pairs of feathers
    pairs = combinations(feathers, 2)

    # Check if any forbidden pattern exists
    for pattern in forbidden_patterns:
        if all(color_pair not in pairs for color_pair in pattern):
            continue
        else:
            return False

    # If no forbidden pattern exists, return True
    return True

# Example usage
feathers = ["Red", "Blue", "Green", "Yellow"]
forbidden_patterns = [[("Red", "Blue"), ("Blue", "Green")], [("Green", "Yellow"), ("Yellow", "Red")]]
result = check_feather_combination(feathers, forbidden_patterns)

if result:
    print("A combination of feathers exists that avoids the forbidden patterns!")
else:
    print("No combination of feathers exists that avoids the forbidden patterns.")


'''In this code, the check_feather_combination() function takes a list of feathers and a list of forbidden patterns as input. It generates all possible pairs of feathers and checks if any of the forbidden patterns exist within these pairs. If a forbidden pattern is found, the function returns False. If no forbidden pattern exists, the function returns True.

The example usage demonstrates how to check whether a combination of feathers can avoid the specified forbidden patterns. The provided feathers list contains colors of feathers, and the forbidden_patterns list contains tuples of colors that should not appear together. The code checks whether there exists a combination of feathers that avoids the forbidden patterns.

Modify the feathers and forbidden_patterns lists to create your own whimsical scenarios in Vurt. Experiment with different colors, forbidden patterns, and feather combinations to explore the possibilities of harmonious feather combinations while incorporating the concepts of Ramsey theory.'''