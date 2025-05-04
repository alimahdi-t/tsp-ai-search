def read_input(file_path):
    try:
        # Open the input file in read mode
        with open(file_path, 'r') as file:
            # Read the first line which contains the number of cities
            n = int(file.readline())

            # Read the second line which contains the names of the cities
            cities = file.readline().strip().split()

            # Initialize an empty list to store the distance matrix
            distances = []

            # Read the next 'n' lines to build the distance matrix
            for _ in range(n):
                # Read and convert each line to a list of floats (distances)
                row = list(map(float, file.readline().strip().split()))
                distances.append(row)  # Append each row to the distance matrix

        # Return the list of city names and the distance matrix
        return cities, distances

    except Exception as e:
        # Handle any error that occurs during file reading or parsing
        print(f"An error occurred while reading the file: {e}")
        return [], []  # Return empty lists if an error occurs
