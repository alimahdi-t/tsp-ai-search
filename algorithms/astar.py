import heapq
import math
from models.node import Node
from algorithms.heuristics import heuristic


def a_star(cities, distances):
    n = len(cities)
    start_node = Node(path=[0], visited={0}, cost=0, estimate=heuristic(0, {0}, distances))
    open_list = []
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)
        if len(current.visited) == n:
            return current.path + [0], current.cost + distances[current.path[-1]][0]

        for neighbor in range(n):
            if neighbor not in current.visited:
                new_path = current.path + [neighbor]
                new_visited = current.visited | {neighbor}
                new_cost = current.cost + distances[current.path[-1]][neighbor]
                new_estimate = heuristic(neighbor, new_visited, distances)
                heapq.heappush(open_list, Node(new_path, new_visited, new_cost, new_estimate))

    return None, math.inf
