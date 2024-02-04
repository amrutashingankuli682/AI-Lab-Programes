from scipy.spatial import distance
import numpy as np

def nearest_neighbor_algorithm(distance_matrix, start_city=0):
    num_cities = len(distance_matrix)
    unvisited_cities = set(range(num_cities))
    tour = [start_city]
    current_city = start_city

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distance_matrix[current_city, city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    tour.append(start_city)
    return tour

# Example usage:
# Define the coordinates of cities
cities_coordinates = np.array([
    [0, 0],
    [1, 2],
    [3, 1],
    [5, 2]
])

# Calculate the distance matrix
distance_matrix = distance.cdist(cities_coordinates, cities_coordinates)

# Solve TSP using nearest neighbor algorithm
start_city = 0
tour = nearest_neighbor_algorithm(distance_matrix, start_city)

# Print the result
print("Optimal Tour:", tour)