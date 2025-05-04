from utils.reader import read_input
from algorithms.astar import a_star
from algorithms.rbfs import run_rbfs


def main():
    file_path = 'inputs/input-3.txt'
    cities, distances = read_input(file_path)

    print("Running A*...")
    path_a_star, cost_a_star = a_star(cities, distances)
    print("Path:", [cities[i] for i in path_a_star])
    print("Cost:", cost_a_star)

    print("\nRunning RBFS...")
    path_rbfs, cost_rbfs = run_rbfs(cities, distances)
    print("Path:", [cities[i] for i in path_rbfs])
    print("Cost:", cost_rbfs)


if __name__ == "__main__":
    main()
