#!/usr/bin/env python
import re, sys, math
import itertools

# def solve_tsp(coordinates):
#     distances = []

reference_distance_matrix = {(37.77688, -122.3911496): 5, (37.7860105, -122.4025377): 2, (37.7821494, -122.405896): 3, (37.7768016, -122.4169151): 1, (37.7689269, -122.4029053): 4, (37.7706628, -122.4040139): 6}

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)

def distance(a, b):
    """
        >>> distance((1,1), (3,1))
        2.0
        >>> distance((37.7860105, -122.4025377), (37.7706628, -122.4040139)) < distance((37.7860105, -122.4025377), (37.7689269, -122.4029053))
        True
    """
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def distance_matrix(coordinates):
    """ Build a distance matrix
        >>> distance_matrix({(1, 2): 1, (3, 2) : 2})
        [[0, 2.0], [2.0, 0]]
        >>> distance_matrix({(1, 1): 1, (2, 1): 2, (3, 1): 3})
        [[0, 1.0, 2.0], [1.0, 0, 1.0], [2.0, 1.0, 0]]
    """
    n = len(coordinates)
    distances = [[0 for i in range(1, n+1)] for i in range(1, n+1)]
    for c in itertools.permutations(coordinates.keys(), 2):
        distances[coordinates[c[0]]-1][coordinates[c[1]]-1] = distance(*c)

    return distances

def calculate_distance(path, distances):
    """
        >>> calculate_distance([1, 2] , [[0, 2.0], [2.0, 0]])
        2.0
        >>> calculate_distance([1, 3, 2], [[0, 1.0, 2.0], [1.0, 0, 1.0], [2.0, 1.0, 0]])
        3.0
        >>> calculate_distance([1, 2, 3], [[0, 1.0, 2.0], [1.0, 0, 1.0], [2.0, 1.0, 0]])
        2.0
        >>> calculate_distance([5, 6, 4] , distance_matrix(reference_distance_matrix)) > calculate_distance([5, 4, 6] , distance_matrix(reference_distance_matrix))
        True
        >>> calculate_distance([1, 3, 2, 5, 6, 4] , distance_matrix(reference_distance_matrix)) > calculate_distance([1, 3, 2, 5, 4, 6] , distance_matrix(reference_distance_matrix))
        True
    """
    # print [distances[a-1][b-1] for a,b in pairwise(path)]

    return sum(distances[a-1][b-1] for a,b in pairwise(path))

def naive_solve_tsp(coordinates):
    distances = distance_matrix(coordinates)
    path, length = min( [ (t, calculate_distance(t, distances)) for t in itertools.permutations(range(1, len(coordinates)+1)) if t[0] == 1 ], key = lambda x: x[1] )
    for node in path:
        print node

if __name__ == "__main__":
    coordinates = {}
    with open(sys.argv[1]) as f:
        for line in f:
            num, rest = line.strip().split('|')
            coords = eval(re.findall(r'\(.*\)', rest)[0])
            coordinates[coords] = int(num)

    # print coordinates
    naive_solve_tsp(coordinates)
    # solve_tsp_dynamic((1,2))