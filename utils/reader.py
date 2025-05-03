def read_input(file_path):
    try:
        with open(file_path, 'r') as file:
            n = int(file.readline())
            cities = file.readline().strip().split()
            distances = []
            for _ in range(n):
                row = list(map(float, file.readline().strip().split()))
                distances.append(row)
        return cities, distances
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return [], []
