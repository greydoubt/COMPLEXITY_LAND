# The Illusory Reality

'''Wanda Maximoff, the Scarlet Witch, possesses the extraordinary power to create illusions and bend reality. She has created a complex illusionary puzzle that must be solved by her companion, Vision, in order to unlock a hidden treasure. The puzzle consists of a series of interconnected rooms, each with its own set of doors and keys. However, not all keys can unlock all doors, and some doors may be illusions themselves.

Your task is to help Vision navigate through the illusionary puzzle, find the correct sequence of keys to unlock the doors, and reach the treasure. We can encode this problem as an EXP-Space problem.

Let's assume the puzzle consists of a graph representing the rooms, doors, and keys. Each room is represented as a node in the graph, while the doors and keys are represented as edges between nodes. The puzzle solution involves finding a path through the graph that connects the starting room to the treasure room, while collecting and using the correct keys to unlock the doors along the way.

To solve this EXP-Space problem, we can use a backtracking algorithm combined with pruning techniques. We will systematically generate and explore all possible paths through the graph, checking if each path leads from the starting room to the treasure room while satisfying the conditions of key usage and door unlocking. Pruning techniques can be applied to eliminate certain branches of the search tree based on early failures or constraints.'''



def solve_illusionary_puzzle(graph, start, treasure):
    def backtrack(current_room, keys_collected, path):
        if current_room == treasure:
            return path
        
        for next_room in graph[current_room]:
            door = (current_room, next_room)
            required_key = graph.edges[door]['key']
            
            if required_key in keys_collected:
                new_keys_collected = keys_collected.copy()
                new_keys_collected.remove(required_key)
                new_path = path + [door]
                
                result = backtrack(next_room, new_keys_collected, new_path)
                if result:
                    return result
        
        return None
    
    return backtrack(start, set(), [])

# Example usage
import networkx as nx

# Create the illusionary puzzle graph
graph = nx.Graph()
graph.add_edge('Room 1', 'Room 2', key='Key A')
graph.add_edge('Room 2', 'Room 3', key='Key B')
graph.add_edge('Room 2', 'Room 4', key='Key C')
graph.add_edge('Room 3', 'Room 5', key='Key C')
graph.add_edge('Room 4', 'Room 5', key='Key B')
graph.add_edge('Room 4', 'Room 6', key='Key D')
graph.add_edge('Room 5', 'Treasure Room', key='Key D')

start = 'Room 1'
treasure = 'Treasure Room'

path = solve_illusionary_puzzle(graph, start, treasure)
if path:
    print("The path to the treasure is:")
    for door in path:
        print(door)
else:
    print("No valid path to the treasure exists.")



'''In this code, we create an illusionary puzzle graph using the networkx library. Each room is represented as a node in the graph, and the doors are represented as edges between nodes. The key attribute is assigned to each door, specifying the key required to unlock it.

The solve_illusionary_puzzle() function takes the puzzle graph, the starting room, and the treasure room as input. The main algorithm continues with the backtrack() function, which implements the backtracking approach to explore all possible paths through the graph.

At each step, the function checks if the current room is the treasure room. If so, it returns the path. Otherwise, it iterates over the neighboring rooms connected by edges in the graph and checks if the required key for each door is present in the collected keys. If the required key is available, a new set of collected keys is created without the used key, and the function recursively calls itself with the next room, the updated set of keys, and the updated path. If a valid path to the treasure room is found, it is returned; otherwise, the search continues.

'''