import heapq


def prim_mst(unvisited, distances):
    if not unvisited:
        return 0
    visited = set()
    start = next(iter(unvisited))
    pq = []
    total_weight = 0
    visited.add(start)

    for v in unvisited:
        if v != start:
            heapq.heappush(pq, (distances[start][v], start, v))

    while pq:
        weight, u, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            total_weight += weight
            for w in unvisited:
                if w not in visited:
                    heapq.heappush(pq, (distances[v][w], v, w))

    return total_weight


def heuristic(current_city, visited, distances):
    n = len(distances)
    unvisited = set(range(n)) - visited
    if not unvisited:
        return distances[current_city][0]
    mst_weight = prim_mst(unvisited, distances)
    min_to_unvisited = min(distances[current_city][u] for u in unvisited)
    min_from_unvisited_to_start = min(distances[u][0] for u in unvisited)
    return mst_weight + min_to_unvisited + min_from_unvisited_to_start
