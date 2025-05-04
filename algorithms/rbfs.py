import math
from models.node import Node
from algorithms.heuristics import heuristic


def rbfs(node, cities, distances, f_limit):
    n = len(cities)

    if len(node.visited) == n:
        return node.path + [0], node.cost + distances[node.path[-1]][0], 0

    successors = []
    for neighbor in range(n):
        if neighbor not in node.visited:
            new_path = node.path + [neighbor]
            new_visited = node.visited | {neighbor}
            new_cost = node.cost + distances[node.path[-1]][neighbor]
            new_estimate = heuristic(neighbor, new_visited, distances)
            successor = Node(new_path, new_visited, new_cost, new_estimate)
            successors.append(successor)

    if not successors:
        return None, math.inf, math.inf

    for s in successors:
        s.f_value = max(node.f(), s.f())

    while successors:
        successors.sort(key=lambda x: x.f_value)
        best = successors[0]

        if best.f_value > f_limit:
            return None, math.inf, best.f_value

        alternative = successors[1].f_value if len(successors) > 1 else math.inf
        result, cost, best.f_value = rbfs(best, cities, distances, min(f_limit, alternative))

        if result is not None:
            return result, cost, best.f_value

    return None, math.inf, math.inf


def run_rbfs(cities, distances):
    start_node = Node(path=[0], visited={0}, cost=0, estimate=heuristic(0, {0}, distances))
    result, cost, _ = rbfs(start_node, cities, distances, math.inf)
    return result, cost
