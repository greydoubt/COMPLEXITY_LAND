'''You find yourself trapped in an enchanted maze, and the only way to escape is by following a specific path. The maze consists of interconnected rooms, and each room has a magical symbol on its door. To navigate the maze and find the correct path, you need to follow these rules:

    Rule 1: Every room you enter must have a door with a symbol that you haven't encountered before.
    Rule 2: Each symbol can only appear once in the entire path.

Your task is to determine if there exists a valid path that satisfies these rules. To solve this problem, we can encode it as a SAT problem.

Let's assume that the maze has five rooms, and each room's door symbol is represented by a letter. The symbols on the doors of the five rooms are: A, B, C, D, and E. We can encode the problem using the following variables:

    Variables x1, x2, x3, x4, and x5 represent the rooms you enter in order.
    Variables a, b, c, d, and e represent whether you encounter symbols A, B, C, D, and E, respectively.

Now, let's write the clauses that capture the rules of the problem:

    Rule 1: Every room you enter must have a door with a symbol that you haven't encountered before:
        Clause 1: (!x1 v a) AND (!x2 v b) AND (!x3 v c) AND (!x4 v d) AND (!x5 v e)
        Clause 2: (!x2 v !a v b) AND (!x3 v !a v !b v c) AND (!x4 v !a v !b v !c v d) AND (!x5 v !a v !b v !c v !d v e)
    Rule 2: Each symbol can only appear once in the entire path:
        Clause 3: (!a v !b) AND (!a v !c) AND (!a v !d) AND (!a v !e)
        Clause 4: (!b v !c) AND (!b v !d) AND (!b v !e)
        Clause 5: (!c v !d) AND (!c v !e)
        Clause 6: (!d v !e)'''



import pycosat

def solve_maze():
    clauses = [
        [-1, 6], [-2, 7], [-3, 8], [-4, 9], [-5, 10],                  # Rule 1: Unique symbols in each room
        [-7, 11], [-8, 12], [-9, 13], [-10, 14],                       # Rule 1: Unique symbols in each subsequent room
        [-6, -7, 15], [-7, -8, 16], [-8, -9, 17], [-9, -10, 18],       # Rule 1: Room entry implies encountering the symbol
        [-6, -15], [-7, 15, -16], [-8, 16, -17], [-9, 17, -18],        # Rule 1: Not encountering the symbol implies not entering the room
        [-15, -16], [-16, -17], [-17, -18], # Rule 2: Unique symbols in the entire path
        [-6, -7], [-6, -8], [-6, -9], [-6, -10], # Rule 2: Symbol A cannot appear again
        [-7, -8], [-7, -9], [-7, -10], # Rule 2: Symbol B cannot appear again
        [-8, -9], [-8, -10], # Rule 2: Symbol C cannot appear again
        [-9, -10] # Rule 2: Symbol D cannot appear again
        ]

solution = pycosat.solve(clauses)
if solution != "UNSAT":
    path = ""
    for i in range(5):
        room = abs(solution[i])
        symbol = chr(ord("A") + abs(solution[i + 5]) - 1)
        path += f"Room {room}: Symbol {symbol}\n"
    return path
else:
    return "No valid path exists."

maze_path = solve_maze()
print("The valid path through the maze is:\n", maze_path)


'''
In this code, we define the clauses as a list of lists, similar to the previous example. We use the `pycosat.solve()` function to solve the SAT problem defined by the clauses. If a solution exists (i.e., a valid path is found), we decode the solution to obtain the rooms and symbols encountered in the path. The room numbers are determined by the positive values of the room variables, while the symbols are determined by the corresponding symbol variables.

Finally, we print the valid path through the maze if one is found, or a message indicating that no valid path exists.

'''