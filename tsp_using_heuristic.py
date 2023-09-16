import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tsp(cities):
    num_cities = len(cities)
    visited = [False] * num_cities
    tour = []
    
    # Start from the first city
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True
    
    while len(tour) < num_cities:
        min_distance = float('inf')
        nearest_city = None
        
        for next_city in range(num_cities):
            if not visited[next_city]:
                distance = euclidean_distance(cities[current_city], cities[next_city])
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = next_city
        
        tour.append(nearest_city)
        visited[nearest_city] = True
        current_city = nearest_city
    
    # Return to the starting city
    tour.append(tour[0])
    
    return tour

# Example cities in (x, y) coordinates
cities = [(0, 0), (1, 3), (4, 2), (3, 7), (8, 1)]
tour = nearest_neighbor_tsp(cities)
print("Optimal tour:", tour)
