class Node:
    def __init__(self, path, visited, cost, estimate):
        self.path = path
        self.visited = visited
        self.cost = cost
        self.estimate = estimate

    def f(self):
        return self.cost + self.estimate

    def __lt__(self, other):
        return self.f() < other.f()
