from heapq import heappop, heappush      #https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
#https://docs.python.org/3/library/heapq.html
from math import inf      #this is infinity

graph = {
    'A': [('B', 10), ('C', 3)],          #the numbers here are edges or weights. Reading this, there is a path from A to B with a cost of 10
    'C': [('D', 2)],                    #there is a path between C and D with a cost of 2, etc.
    'D': [('E', 10)],
    'E': [('A', 7)],
    'B': [('C', 3), ('D', 2)]
}


def dijkstras(graph, start):
    distances = {}

    for vertex in graph:    #by default it goes by keys
        distances[vertex] = inf       #you assign every key to infinity

    distances[start] = 0      #start key is set to zero
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)     #current_distance is 0, current_vertex is 'D' (first iteration)

        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    return distances


distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))
