class Node:
    def __init__(self, path, visited, cost, estimate):
        # List of city indices representing the path taken so far
        self.path = path

        # Set of visited city indices to avoid revisiting
        self.visited = visited

        # Accumulated cost of the current path (g(n))
        self.cost = cost

        # Heuristic estimate of the remaining cost to complete the tour (h(n))
        self.estimate = estimate

    def f(self):
        # Total estimated cost function f(n) = g(n) + h(n)
        return self.cost + self.estimate

    def __lt__(self, other):
        # Comparison method to prioritize nodes with lower f(n) in a priority queue
        return self.f() < other.f()
