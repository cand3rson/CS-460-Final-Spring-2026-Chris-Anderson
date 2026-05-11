"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Christopher Anderson
Student ID:   827320059

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return (
        "A single shortest-path run from S finds the cheapest way to reach each node on its own but can't find the order for  when to visit multiple chambers. This is becuase visiting them in a different order produces leads to different total costs.\n\n"
        "After all inter-location costs are known we are left with finding out which order of relics minimizes total fuel.\n\n"
        "This requires a serach over oders becuase the overal costs depeneds on the sequence of vists not the shortest immedidiate path.\n\n"
    )


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    # The exit node is excluded since T is always the destination node
    visited = set()
    source = []

    
    for node in [spawn] + list(relics):
        if node not in visited:
            visited.add(node)
            source.append(node)


    return source
    
def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """

    # All sources are set to infinty except the source node which is set to 0
    distance = {}
    

    for node in graph:
        distance[node] = float('inf')

    distance[source] = 0

    # Min heap reads cost then node
    # Always process chepeast ode first
    heap = [(0, source)]
    visited = set()


    while heap:
        cost, node = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)

        for neighbor_node, weight in graph[node]:
            total_cost = cost + weight


            if total_cost < distance[neighbor_node]:
                distance[neighbor_node] = total_cost
                heapq.heappush(heap, (total_cost, neighbor_node))
                
    return distance


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """

    # Run once for each source node
    dist_table = {}

    for source in select_sources(spawn, relics, exit_node):
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return (
        "For nodes already finalized the nodes distance is locked as the shortest path and won't be updated again. For nodes not yet finalized the current distance represents the best path found so far using only already finalized nodes as stops, but it could still improve.\n\n"
        "Before iteration 1 S is empty with all nodes having a distance of infinity and the source nodes distance is 0 since it is itself. The invariant holds because no nodes have been finalized. When the min distance node is revelaed it's distance is always the shortest path. This is because all edge weights are non-negative and no other path can be smaller.The invariant gurantees that when the heap is empty every node has been finialized and their distance value is the shortest distance to the source.\n\n"
        "This matters for the Route Planner because if Dijkstra's output is wrong the Route Planner would pick the wrong relic order and not find the minniumum fuel route.\n\n"
    )


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return (
        "The failure mode is that a greedy apporach will pick the cheapest current node even if it leads to to a more expensive overall route.\n\n"
        "A weighted and directed graph G{S,A,B,T} with S pointing to A for 1, S pointing to B for 4, A pointing to T for 1, A pointing to B for 8 and B pointing to T for 1 and B pointing to A for 1.\n\n"
        "A greedy algorithim selects S,A,B,T for a total cost of 10.\n\n"
        "The optimal solution selects S,B,A,T for a total cost of 6.\n\n"
        "When the greedy path had to choose between S to A for 1 or S to B for 4, it picekd S to A. However, this forced the greedy algorithim to pick A to B for 8, a much slower apporach.\n\n"
        "The algorithm must explore every possible order of visiting relic chambers because the total cost depends on the order of the relics found not just the local shortest path costs between nodes.\n\n"
    )


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    # Part 5b
    relics_remaining = set(relics)
    # Part 5a
    relics_visited_order = []
    # Part 6a
    best = [float('inf'), []]


    _explore(dist_table, spawn, relics_remaining, relics_visited_order, 0, exit_node, best)
    return (best[0], best[1])


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    # Best-so-far pruning from part 6a
    if cost_so_far >= best[0]:
        return

    # Lower bound pruning from part 6b
    if relics_remaining:
        cheapest_to_remaining_relic = min(

            dist_table.get(current_loc, {}).get(relic, float('inf'))
            for relic in relics_remaining )


        # cheapest cost from any of the remaining relics to exit
        cheapest_to_relic_t = min(

            dist_table.get(relic, {}).get(exit_node, float('inf'))
            for relic in relics_remaining)

            
        lower = cost_so_far + cheapest_to_remaining_relic + cheapest_to_relic_t

        # Part 6c: The lower bound is found from the shortest path of the least expensive
        # move to any  relic left over and the least expensive move from any relic to the exit.
        # This means it will never go over the cost to finish and it will never
        # beat the current best leading to the optimal solution never being pruned.
        if lower >= best[0]:
            return



    # Part 5c search space exploration.
    # BASE CASE:
    # All relics collected.
    if not relics_remaining:
        # Cost for current location + exit
        final_cost = dist_table.get(current_loc, {}).get(exit_node, float('inf'))
        total_cost = cost_so_far + final_cost


        # If a solution is better than best, update best
        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = list(relics_visited_order)
        return


    # Part 5c exploration.
    # Using recurison to explore each remaining relic as next destination
    for relic in list(relics_remaining):
        travel_cost = dist_table.get(current_loc, {}).get(relic, float('inf'))

        # Unreachable 
        if travel_cost == float('inf'):
            continue


        # Part 5b visit relic
        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        # Part 5c recursion logic
        _explore(dist_table,relic, relics_remaining, relics_visited_order,cost_so_far + travel_cost,exit_node,best)


        # Part 5b backgracking logic.
        relics_visited_order.pop()
        relics_remaining.add(relic)



# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    
    dist_table = precompute_distances(graph, spawn, relics, exit_node)

    return find_optimal_route(dist_table, spawn, relics, exit_node)
    



# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
