# The Cursed Crypt

'''In a haunted crypt deep within the dark woods, a legendary treasure lies hidden. However, the crypt is cursed, and a set of intricate puzzles must be solved to reach the treasure chamber. Each puzzle is guarded by a fearsome creature that can only be defeated by choosing the correct weapon from a limited selection.

Your task is to navigate through the cursed crypt, defeat each guardian creature by selecting the right weapon, and ultimately unlock the treasure chamber. We can encode this problem as an EXP-Space problem.

Let's assume the cursed crypt consists of a series of interconnected rooms, and each room contains a guardian creature and a set of available weapons. Each weapon has a unique property, and only one of them is effective against each guardian creature.

To solve this EXP-Space problem, we can use a backtracking algorithm combined with pruning techniques. We will systematically generate and explore all possible paths through the crypt, selecting weapons to defeat each guardian creature, and checking if we reach the treasure chamber successfully. Pruning techniques can be applied to eliminate certain branches of the search tree based on early failures or constraints.'''



def solve_cursed_crypt(crypt, current_room, weapons_collected, path):
    if current_room == "Treasure Chamber":
        return path
    
    for next_room, guardian_creature in crypt[current_room]:
        available_weapons = guardian_creature["weapons"]
        
        for weapon in available_weapons:
            if weapon in weapons_collected:
                new_weapons_collected = weapons_collected.copy()
                new_weapons_collected.remove(weapon)
                new_path = path + [(current_room, weapon, next_room)]
                
                result = solve_cursed_crypt(crypt, next_room, new_weapons_collected, new_path)
                if result:
                    return result
    
    return None

# Example usage
crypt = {
    "Entrance Hall": [
        ("Library", {"creature": "Specter", "weapons": ["Silver Sword", "Wooden Staff"]}),
        ("Dining Room", {"creature": "Ghoul", "weapons": ["Iron Dagger", "Wooden Staff"]}),
    ],
    "Library": [
        ("Study", {"creature": "Banshee", "weapons": ["Silver Sword", "Crystal Wand"]}),
        ("Bedroom", {"creature": "Wraith", "weapons": ["Iron Dagger", "Silver Sword"]}),
    ],
    "Dining Room": [
        ("Kitchen", {"creature": "Zombie", "weapons": ["Iron Dagger", "Steel Axe"]}),
    ],
    "Kitchen": [
        ("Treasure Chamber", {"creature": "Dragon", "weapons": ["Dragon Slayer Sword"]}),
    ],
    "Study": [],
    "Bedroom": [],
    "Treasure Chamber": []
}

start_room = "Entrance Hall"

path = solve_cursed_crypt(crypt, start_room, {"Wooden Staff"}, [])
if path:
    print("The path to the treasure chamber is:")
    for room, weapon, next_room in path:
        print(f"Enter {room}, defeat {crypt[room][0][1]['creature']} with {weapon}, and move to {next_room}")
else:
    print("No valid path to the treasure chamber exists.")



'''
In this code, the crypt dictionary represents the structure of the cursed crypt. Each room is a key in the dictionary, and the value is a list of tuples representing the neighboring rooms and their guardian creatures. The guardian creatures are represented as dictionaries containing their name and the available weapons to defeat them.

The solve_cursed_crypt() function takes the crypt structure, the current room, the weapons collected, and the current path as inputs. It recursively explores all possible paths through the crypt, defeating each guardian creature by selecting the right weapon, and checking if the treasure chamber is reached.

At each step, the function checks if the current room is the treasure chamber. If so, it returns the path. Otherwise, it iterates over the neighboring rooms and their guardian creatures. For each guardian creature, it checks the available weapons and selects one that is present in the collected weapons. If a valid weapon is found, the function creates a new set of collected weapons without the used weapon, updates the path, and recursively calls itself with the next room, the updated set of collected weapons, and the updated path. If a valid path to the treasure chamber is found, it is returned; otherwise, the search continues.
'''