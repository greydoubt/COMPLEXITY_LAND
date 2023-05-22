#The Temporal Nexus

'''In a retro-futuristic world of time travel and arcane technology, a powerful sorcerer known as Tempus has discovered a hidden temporal nexus. The temporal nexus contains a series of artifacts scattered across different time periods, and these artifacts must be recovered in the proper sequence and order to unlock its true power.

Each artifact is located in a specific time period, and the temporal nexus allows the sorcerer to jump between these time periods. However, each jump in time consumes a specific amount of temporal energy, and there are constraints on the sequence and order in which the artifacts can be collected.

Your task is to help Tempus navigate through the temporal nexus, jump between time periods using the available temporal energy, and collect the artifacts in the proper sequence and order to unlock the nexus's power. We can encode this problem as an EXP-TIME problem.

To solve this EXP-TIME problem, we can use a dynamic programming approach. We will maintain a table to track the state of the temporal nexus at each time period, storing the minimum temporal energy required to reach each artifact in the proper sequence and order. By iteratively updating the table based on the temporal energy consumed in each jump, we can determine the optimal path through the temporal nexus.'''


def solve_temporal_nexus(nexus, artifacts):
    num_artifacts = len(artifacts)
    num_time_periods = len(nexus)
    
    # Initialize the dynamic programming table
    dp = [[float('inf')] * num_artifacts for _ in range(num_time_periods)]
    
    # Base case: No temporal energy required to reach the first artifact
    dp[0][0] = 0
    
    # Dynamic programming iteration
    for time_period in range(num_time_periods):
        for artifact_index in range(1, num_artifacts):
            # Calculate the temporal energy consumed in the jump
            jump_energy = nexus[time_period][artifact_index - 1][artifact_index]
            
            # Calculate the minimum energy required to reach the current artifact
            dp[time_period][artifact_index] = min(dp[time_period][artifact_index], dp[time_period][artifact_index - 1] + jump_energy)
            
            # Propagate the energy to subsequent time periods
            for next_time_period in range(time_period + 1, num_time_periods):
                next_jump_energy = nexus[time_period][artifact_index - 1][artifact_index] + nexus[time_period][artifact_index][artifact_index + 1]
                dp[next_time_period][artifact_index] = min(dp[next_time_period][artifact_index], dp[time_period][artifact_index - 1] + next_jump_energy)
    
    # Check if a valid path through the temporal nexus exists
    if dp[num_time_periods - 1][num_artifacts - 1] == float('inf'):
        return None
    
    # Reconstruct the optimal path
    path = []
    time_period = num_time_periods - 1
    artifact_index = num_artifacts - 1
    
    while artifact_index > 0:
        jump_energy = nexus[time_period][artifact_index - 1][artifact_index]
        
        if dp[time_period][artifact_index] == dp[time_period][artifact_index - 1] + jump_energy:
            # Jump to the previous time period
            time_period -= 1
        else:
            # Collect the artifact in the current time period
            path.append((artifacts[artifact_index], time_period))
            artifact_index -= 1
    
    # Add the first artifact to the path
    path.append((artifacts[0], time_period))
    
    # Reverse the path to display it in the correct order
    path.reverse()

    return path

nexus = [
# Time period 1
[
[0, 3, 4], # Jump energies from artifact 0 to 1, 1 to 2, and 2 to 3
[float('inf'), 0, 2], # Jump energies from artifact 1 to 2 and 2 to 3
[float('inf'), float('inf'), 0], # Jump energy from artifact 2 to 3
],
# Time period 2
[
[0, 5, 2], # Jump energies from artifact 0 to 1, 1 to 2, and 2 to 3
[float('inf'), 0, 4], # Jump energies from artifact 1 to 2 and 2 to 3
[float('inf'), float('inf'), 0], # Jump energy from artifact 2 to 3
],
# Time period 3
[
[0, 1, 7], # Jump energies from artifact 0 to 1, 1 to 2, and 2 to 3
[float('inf'), 0, 3], # Jump energies from artifact 1 to 2 and 2 to 3
[float('inf'), float('inf'), 0], # Jump energy from artifact 2 to 3
]
]

artifacts = ["A", "B", "C"]

path = solve_temporal_nexus(nexus, artifacts)

if path:
    print("The optimal path through the temporal nexus is:")
    for artifact, time_period in path:
    print(f"Collect {artifact} in Time Period {time_period}")
else:
    print("No valid path through the temporal nexus exists.")



'''In this code, the `nexus` represents the structure of the temporal nexus. It is a list of time periods, each containing a matrix of jump energies between artifacts. The `artifacts` list represents the artifacts to be collected in the proper sequence and order.

The `solve_temporal_nexus()` function applies dynamic programming to calculate the minimum temporal energy required to reach each artifact in the proper sequence and order. It iterates through the time periods and artifacts, updates the minimum energy based on the jump energies, and propagates the energy to subsequent time periods.

After the dynamic programming iteration, the function checks if a valid path through the temporal nexus exists by verifying if the energy required to reach the last artifact is finite. If a valid path exists, it reconstructs the optimal path by backtracking from the last artifact to the first.
'''