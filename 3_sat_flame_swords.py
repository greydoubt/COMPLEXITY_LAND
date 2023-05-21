# The Witch's Flame Sword Collection

'''The powerful witch, Pyronia, has an impressive collection of flame swords. Each flame sword in her collection is unique and possesses specific magical properties. Pyronia is an expert in organizing her swords, and she has set the following rules for arranging them:

    Rule 1: Each flame sword must be displayed in a different position on the shelf.
    Rule 2: Certain pairs of flame swords have conflicting magical properties and should not be displayed together.

Your task is to determine if it is possible to arrange Pyronia's flame swords on the shelf while satisfying these rules. We can encode this problem as a SAT problem.

Let's assume Pyronia has five flame swords in her collection, numbered from 1 to 5. We can use variables x1, x2, x3, x4, and x5 to represent the positions of the flame swords on the shelf.

To encode the rules, we can define the following clauses:

    Rule 1: Each flame sword must be displayed in a different position on the shelf:
        Clause 1: (-x1 v -x2) AND (-x1 v -x3) AND (-x1 v -x4) AND (-x1 v -x5)
        Clause 2: (-x2 v -x3) AND (-x2 v -x4) AND (-x2 v -x5)
        Clause 3: (-x3 v -x4) AND (-x3 v -x5)
        Clause 4: (-x4 v -x5)

    Rule 2: Certain pairs of flame swords have conflicting magical properties and should not be displayed together:
        Clause 5: (-x1 v -x2)
        Clause 6: (-x2 v -x3)
        Clause 7: (-x4 v -x5)

To solve this SAT problem, we can use the pycosat to check if a valid arrangement of flame swords exists:'''

import pycosat

def arrange_flame_swords():
    clauses = [
        [-1, -2], [-1, -3], [-1, -4], [-1, -5],   # Rule 1: Unique positions on the shelf
        [-2, -3], [-2, -4], [-2, -5],             # Rule 1: Unique positions on the shelf
        [-3, -4], [-3, -5],                       # Rule 1: Unique positions on the shelf
        [-4, -5],                                 # Rule 1: Unique positions on the shelf
        [-1, -2],                                 # Rule 2: Conflicting swords
        [-2, -3],                                 # Rule 2: Conflicting swords
        [-4, -5]                                  # Rule 2: Conflicting swords
    ]
    
    solution = pycosat.solve(clauses)
    if solution != "UNSAT":
        arrangement = ""
        for i in range(5):
            sword = abs(solution[i])
            position = i + 1
            arrangement += f"Flame Sword {sword} at Position {position}\n"
        return arrangement
    else:
        return "No valid arrangement exists."

flame_sword_arrangement = arrange_flame_swords()
print("The valid arrangement of flame swords is:\n", flame_sword_arrangement)

''' If a solution exists (i.e., a valid arrangement is found), we decode the solution to obtain the positions and corresponding flame swords in the arrangement. The positions are determined by the values of the position variables, while the flame swords are determined by the positive values of the sword variables.

Finally, we print the valid arrangement of flame swords if one is found, or a message indicating that no valid arrangement exists.'''