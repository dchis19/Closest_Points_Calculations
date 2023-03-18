from random import randrange
import math

arrayX, arrayY, points_by_x, points_by_y, points, point1, point2 = [], [], [], [], [], [], []
minimumDis = []
miniumDistance = 1000000000000

##################################################################################
# Generates a random grid of points
# n is number of points (integer)
# m is size of grid (integer)
# Points is a list of n tuples
##################################################################################

def generate_pts(n, m):
    points = []
    for i in range(n):
        point = (randrange(m), randrange(m))
        points.append(point)
    return points


##################################################################################
# Append x and y values from POINTS array to respective arrays
##################################################################################

def appendXAndY(POINTS): 
    for x in POINTS:
        arrayX.append(x[0])
        arrayY.append(x[1])

##################################################################################
# Calculate the distance using distance formula. If calculated distance 
# is less than or equal to the previously calculated minimum value, then
# append the value and its respective points to their lists. Return 
# distance at end of method.
##################################################################################

def distanceCalculation(p1, p2):  
    global miniumDistance
    if ((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))**0.5 <= miniumDistance:
        miniumDistance = ((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))**0.5
        point1.append(p1)
        point2.append(p2)
        minimumDis.append(miniumDistance)
    return ((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))**0.5

##################################################################################
# Determine if x is less than y. If so return x, otherwise return y
##################################################################################

def minimum(x, y):
    return x if x < y else y

##################################################################################
# Takes a list of values and returns a sorted list after performing merge sort
##################################################################################

def mergeSort(inputList):
    if len(inputList) > 1:
        mid = len(inputList) // 2
        left = inputList[:mid]
        right = inputList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)
        
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              inputList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                inputList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            inputList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            inputList[k]=right[j]
            j += 1
            k += 1
            
    return (inputList) 

##################################################################################
# If data subset becomes less than n = 3, use the brute force method by 
# iterating through points using 2 for loops to determine minimum value. 
# Return minimum distance
##################################################################################

def bruteForce(points, n):
    min_distance = 100000000000000000000000000
    for i in range(n):
        for j in range(i+1, n):
            if distanceCalculation(points[i], points[j]) < min_distance:
                min_distance = distanceCalculation(points[i], points[j])
    return min_distance

##################################################################################
# Determine if points that are near the middle point are the closest points together.
# Only use this method for values in strip array from dividePoints() method. 
# Return values to dividePoints() method
##################################################################################

def lineClosestCalc(centerPoints, size, d):
    min_dist = d
    centerPoints = mergeSort(centerPoints)
    for i in range(size):
        for j in range(i+1, size):
            if (centerPoints[j][0] - centerPoints[i][0]) >= min_dist:
                break
            if distanceCalculation(centerPoints[i], centerPoints[j]) < min_dist:
                min_dist = distanceCalculation(centerPoints[i], centerPoints[j])
    return min_dist

##################################################################################
# The dividePoints() method takes the array, POINTS, and finds the middle point
# of the array. The dividePoints is recursively called and the points array is
# further divided. If values are smaller than the mid point then they equal 
# divideLeft. Otherwise, the values equal divideRight. Eventually, the furthest subset 
# of points occurs and we find the minimum (value = d) between divideLeft and 
# divideRight. The absolute value of the x values from index 0 to n (n progressively
# gets smaller with each recursive call) is compared to d, and if absolute value is 
# smaller, we append it to the CentralPoints array. The d values are then compared to 
# the values lineClosestCalc distance, and the smallest value is returned. 
##################################################################################

def dividePoints(points, n):
    if n <= 3:
        return bruteForce(points, n)
    mid = n//2
    midPoint = points[mid]
    divideLeft = dividePoints(points, mid)
    divideRight = dividePoints(points[mid:], n - mid)
    d = minimum(divideLeft, divideRight)
    CentralPoints = []
    for i in range(n):
        if abs(points[i][0] - midPoint[0]) < d:
            CentralPoints.append(points[i])
    return minimum(d, lineClosestCalc(CentralPoints, len(CentralPoints), d))

def closestPairCLRS(points):
    #create 10 points randomly between values 0 - 100000
    POINTS = points
    mini, tuple1, tuple2 = 100000000000000000000000000, 0, 0
    n = len(POINTS) #length of array
    appendXAndY(POINTS) #place x and y values from the points into respective arrays
    points_by_x = mergeSort(POINTS) #sort the points by x values
    y_First_Array = list(zip(arrayY, arrayX))
    points_by_y = mergeSort(y_First_Array)#sort the points by y values
    dividePoints(points_by_x, n) #divide array into sub components and calculate smallest distance
    #of minimum distances calculated, print the smallest one with its respective points
    for i in range(len(minimumDis)):
        if minimumDis[i] < mini:
            mini = minimumDis[i]
            tuple1 = point1[i]
            tuple2 = point2[i]
            
    return tuple1, tuple2, mini


##############################################################################################################

## TESTING DATA
# Don't change the data structure used, or points will be taken off

POINTS = [(7, 16), (13, 5), (4, 2), (20, 8), (5, 16), (2, 4), (6, 6), (20, 15), (17, 8), (11, 16)]

# Some test cases and results are given in the sample data below.  

## KICKOFF CODE

p1, p2, d = closestPairCLRS(POINTS)
print(f"Closest pair of points are {p1} and {p2}, distance = {d}")

# Expected output: 
# Closest pair of points are (7,16) and (5,16), distance = 2.0