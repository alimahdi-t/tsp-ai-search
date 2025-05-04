from utils.reader import read_input
from algorithms.astar import a_star_algorithm
from algorithms.rbfs import rbfs_algorithm


file_path = 'inputs/input-3.txt'
cities, distances = read_input(file_path)

print("A* algorithm:")
path_a_star, cost_a_star = a_star_algorithm(cities, distances)
print("Best path:", " -> ".join([cities[i] for i in path_a_star]))
print("Path cost:", cost_a_star)

print("\n\n\nRBFS algorithm:")
path_rbfs, cost_rbfs = rbfs_algorithm(cities, distances)
print("Best path:", " -> ".join([cities[i] for i in path_rbfs]))
print("Path cost:", cost_rbfs)

