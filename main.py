from utils.reader import read_input


def main():
    file_path = "input.txt"
    cities, distances = read_input(file_path)
    print(cities)
    print(distances)


if __name__ == "__main__":
    main()
