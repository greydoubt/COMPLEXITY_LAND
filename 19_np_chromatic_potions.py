# Ouranian Swamp Witch's Chromatic Potions

'''Deep in the heart of the mystical Ouranian Swamp, resides the enigmatic Ouranian Swamp Witch. She possesses a rare and ancient knowledge of potion-making, specializing in creating chromatic potions that imbue various magical properties.

To concoct her chromatic potions, the Swamp Witch relies on the abundant resources found in the swamp. However, these resources are scattered and can only be located by her trained spiders. Each spider is adept at finding a specific type of resource.

The goal is to determine whether the Swamp Witch's spiders, when deployed strategically, can locate the required resources for crafting a specific chromatic potion.

Each chromatic potion recipe requires a unique combination of resources, represented by a list of required resources. The Swamp Witch has a team of trained spiders, each specializing in finding a particular resource. The spiders can be sent out to search for the required resources independently.

Your task is to determine whether there exists a deployment plan for the spiders that guarantees the discovery of all the required resources within a given time frame.'''


def check_resource_availability(required_resources, spider_deployments, cost_threshold):
    total_cost = 0

    # Check if all required resources are found within the cost threshold
    for resource in required_resources:
        found = False
        for deployment in spider_deployments:
            if resource in deployment:
                found = True
                total_cost += deployment[resource]  # Add the cost of obtaining the resource
                break
        if not found:
            return False
        
        if total_cost > cost_threshold:
            return False
    
    # If all required resources are found within the cost threshold, return True
    return True

# Example usage
required_resources = ["Mystic Mushrooms", "Glowing Ferns", "Swamp Water"]
spider_deployments = [
    {"Mystic Mushrooms": 3, "Glowing Ferns": 2},
    {"Swamp Water": 1},
    {"Mystic Mushrooms": 4}
]
cost_threshold = 6
result = check_resource_availability(required_resources, spider_deployments, cost_threshold)

if result:
    print("The spiders can locate all the required resources within the cost threshold!")
else:
    print("The spiders cannot locate all the required resources within the cost threshold.")




'''Each dictionary represents the resources found by a spider and includes the associated cost of obtaining each resource.

The check_resource_availability() function has been modified to consider the cost of obtaining resources. It iterates over each required resource and checks if it is found within the spider deployments. If a required resource is found, it adds the corresponding cost to the total_cost variable. If the total cost exceeds the cost_threshold, the function returns False. Otherwise, it continues to check the remaining resources. If all the required resources are found within the cost threshold, the function returns True.

The example usage demonstrates how to check whether the Swamp Witch's spiders can locate all the required resources while staying within the cost threshold. The provided required_resources list contains the names of the resources needed for the potion, and the spider_deployments list contains the deployments of the spiders, including the associated costs. The cost_threshold variable sets the maximum allowable cost. The code checks whether there exists a spider deployment plan that guarantees the retrieval of all the required resources under the cost threshold.'''


def verify_solution(required_resources, spider_deployments):
    # Create a set of found resources
    found_resources = set()

    # Check if all required resources are found
    for deployment in spider_deployments:
        found_resources.update(deployment)

    if found_resources == set(required_resources):
        return True
    else:
        return False

# Example usage
required_resources = ["Mystic Mushrooms", "Glowing Ferns", "Swamp Water"]
spider_deployments = [
    {"Mystic Mushrooms": 3, "Glowing Ferns": 2},
    {"Swamp Water": 1},
    {"Mystic Mushrooms": 4}
]
result = verify_solution(required_resources, spider_deployments)

if result:
    print("The solution is verified! All required resources are found.")
else:
    print("The solution is not correct. Some required resources are missing.")



'''In this second script, the verify_solution() function takes a list of required resources and a list of spider deployments as input. It creates a set of found resources by iterating over the spider deployments and adding each resource to the set. Then, it checks if the set of found resources matches the set of required resources. If the sets match, the function returns True, indicating that the solution is verified. Otherwise, it returns False, indicating that some required resources are missing.

The example usage demonstrates how to verify a solution for the Ouranian Swamp Witch's Chromatic Potions problem. The required_resources list contains the names of the resources needed for the potion, and the spider_deployments list contains the deployments of the spiders, including the associated costs. The code calls the verify_solution() function and checks if the solution is verified based on the found resources.

You can modify the required_resources and spider_deployments variables to match the scenario you want to verify. If the solution is correct and all the required resources are found, it will print "The solution is verified! All required resources are found." Otherwise, it will print "The solution is not correct. Some required resources are missing."'''