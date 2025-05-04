import heapq
import math
from models.node import Node
from algorithms.heuristics import heuristic


def a_star_algorithm(cities, distances):
    """
    Implements the A* search algorithm to solve the Traveling Salesman Problem (TSP).

    :param cities: List of city names (only used for length here)
    :param distances: 2D list representing the distance matrix between cities
    :return: A tuple (optimal_path, total_cost)
    """
    n = len(cities)

    # Create the start node (starting from city 0)
    start_node = Node(
        path=[0],
        visited={0},
        cost=0,
        estimate=heuristic(0, {0}, distances)  # Estimate cost to finish the tour
    )

    # Priority queue to hold nodes ordered by f = g + h
    open_list = []
    heapq.heappush(open_list, start_node)

    # A* main loop
    while open_list:
        # Get the node with the lowest estimated total cost
        current = heapq.heappop(open_list)

        # If all cities have been visited, return to the start to complete the tour
        if len(current.visited) == n:
            return current.path + [0], current.cost + distances[current.path[-1]][0]

        # Expand neighbors (unvisited cities)
        for neighbor in range(n):
            if neighbor not in current.visited:
                new_path = current.path + [neighbor]
                new_visited = current.visited | {neighbor}
                new_cost = current.cost + distances[current.path[-1]][neighbor]
                new_estimate = heuristic(neighbor, new_visited, distances)

                # Push new node to the open list
                heapq.heappush(open_list, Node(new_path, new_visited, new_cost, new_estimate))

    # If no solution found
    return None, math.inf
