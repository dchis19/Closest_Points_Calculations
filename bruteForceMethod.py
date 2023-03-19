import math

def bruteForce(points, n):
    min_distance = float("inf")
    point1 = (0,0)
    point2 = (0,0)
    for i in range(n):
        for j in range(i+1, n):
            if math.dist(points[i], points[j]) < min_distance:
                point1 = points[i]
                point2 = points[j]
                min_distance = math.dist(points[i], points[j])
    return point1, point2, min_distance

## TESTING DATA
# Don't change the data structure used, or points will be taken off

POINTS = [(7, 16), (13, 5), (4, 2), (20, 8), (5, 16), (2, 4), (6, 6), (20, 15), (17, 8), (11, 16)]

# Some test cases and results are given in the sample data below.  You should plan on
# generating your own test data as needed, in addition to the sample data.
point1, point2, distance = bruteForce(POINTS, len(POINTS))
print(f'The closest points are {point1} and {point2} at a distance of {distance}')