import heapq


def prim_mst(unvisited, distances):
    """
    Computes the weight of the Minimum Spanning Tree (MST) over the unvisited nodes using Prim's algorithm.
    :param unvisited: A set of indices representing unvisited cities
    :param distances: 2D list (matrix) representing distances between cities
    :return: Total weight of the MST
    """
    if not unvisited:
        return 0

    visited = set()
    start = next(iter(unvisited))  # Pick an arbitrary start node
    pq = []                        # Priority queue to select the next closest edge
    total_weight = 0              # Total weight of the MST

    visited.add(start)

    # Add edges from the start node to all other unvisited nodes
    for v in unvisited:
        if v != start:
            heapq.heappush(pq, (distances[start][v], start, v))

    # Prime's algorithm main loop
    while pq:
        weight, u, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            total_weight += weight
            # Add edges from new node to all remaining unvisited nodes
            for w in unvisited:
                if w not in visited:
                    heapq.heappush(pq, (distances[v][w], v, w))

    return total_weight


def heuristic(current_city, visited, distances):
    """
    Heuristic function for A* or RBFS in TSP.
    It estimates the cost to complete the tour by:
      - MST over unvisited cities
      - Minimum cost to reach an unvisited city from the current city
      - Minimum cost to return to the start city from any unvisited city
    :param current_city: The current city index
    :param visited: A set of visited city indices
    :param distances: 2D list (matrix) representing distances between cities
    :return: Estimated cost to complete the tour
    """
    n = len(distances)
    unvisited = set(range(n)) - visited

    # If all cities are visited, return cost to return to start
    if not unvisited:
        return distances[current_city][0]

    # Compute MST over unvisited cities
    mst_weight = prim_mst(unvisited, distances)

    # Find the nearest unvisited city from current city
    min_to_unvisited = min(distances[current_city][u] for u in unvisited)

    # Find the minimum cost to return to the starting city from unvisited cities
    min_from_unvisited_to_start = min(distances[u][0] for u in unvisited)

    # Total estimated cost: MST + entry cost + exit cost
    return mst_weight + min_to_unvisited + min_from_unvisited_to_start
