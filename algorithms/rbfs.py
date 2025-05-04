import math
from models.node import Node              # Importing the Node class used to represent each state
from algorithms.heuristics import heuristic  # Importing the heuristic function used in RBFS


def rbfs(node, cities, distances, f_limit):
    """
    Recursive Best-First Search (RBFS) algorithm to solve the TSP.
    :param node: Current node in the search tree
    :param cities: List of city names
    :param distances: Distance matrix between cities
    :param f_limit: Current limit for f(n) = g(n) + h(n)
    :return: Best path, its cost, and the best alternative f-value
    """
    n = len(cities)

    # Goal test: if all cities are visited, return path + cost to return to start
    if len(node.visited) == n:
        return node.path + [0], node.cost + distances[node.path[-1]][0], 0

    # Generate successors (unvisited neighbors)
    successors = []
    for neighbor in range(n):
        if neighbor not in node.visited:
            new_path = node.path + [neighbor]
            new_visited = node.visited | {neighbor}
            new_cost = node.cost + distances[node.path[-1]][neighbor]
            new_estimate = heuristic(neighbor, new_visited, distances)
            successor = Node(new_path, new_visited, new_cost, new_estimate)
            successors.append(successor)

    # If no successors (dead end), return failure
    if not successors:
        return None, math.inf, math.inf

    # Set f-value for each successor
    for s in successors:
        s.f_value = max(node.f(), s.f())  # Avoid decreasing f(n) along the path

    # Main RBFS loop
    while successors:
        # Sort successors by their f-value (lowest first)
        successors.sort(key=lambda x: x.f_value)
        best = successors[0]

        # If best f-value exceeds the current f-limit, backtrack
        if best.f_value > f_limit:
            return None, math.inf, best.f_value

        # Determine alternative f-value (second best option)
        alternative = successors[1].f_value if len(successors) > 1 else math.inf

        # Recursive call with updated f-limit
        result, cost, best.f_value = rbfs(best, cities, distances, min(f_limit, alternative))

        # If a valid result is found, return it
        if result is not None:
            return result, cost, best.f_value

    # No valid result found
    return None, math.inf, math.inf


def run_rbfs(cities, distances):
    """
    Initializes and runs the RBFS algorithm from the starting city.
    :param cities: List of city names
    :param distances: Distance matrix
    :return: Best path and total cost found by RBFS
    """
    start_node = Node(path=[0], visited={0}, cost=0, estimate=heuristic(0, {0}, distances))
    result, cost, _ = rbfs(start_node, cities, distances, math.inf)
    return result, cost
