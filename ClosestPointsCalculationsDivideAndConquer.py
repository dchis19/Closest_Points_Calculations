from random import randrange
import math

"""
Author: Daniel Chisner
Input: Array of Points
Output: Tuples/Points that are closest together with their respective distance apart

This algorithm determines the closest two points together and prints out the points and their 
respective distance apart. Points are stored in an array as tuples in (x,y) format. 
First, points are sorted by their x values using merge sort. The dividePoints() method is then 
called which recursively divides the points array into smaller sub components based on the 
midpoint of the array/sub components. X values that are less than the minimum of the two sub 
components are appended to a centralPoints array for later use. Once the subcomponents are 
less than or equal to 3 elements in size, a brute force method is called to determine the 
distance. At the end of the dividePoints() method, the minimum is returned, which calls the 
lineClosestCalc() method.

The lineClosestCalc() determines if points near the midpoint are closer together than previously 
calculated distances. If so, the minimum distance variable is updated. At the end of the 
lineClosestCalc() method, the minimum distance is returned.

"""

class DivideAndConquer:
  arrayX, arrayY, points, point1, point2 = [], [], [], [], []
  minimumDis = []
  miniumDistance = float('inf')

  def __init__(self):
    p1, p2, d = DivideAndConquer.closestPairCLRS(POINTS)
    print(f"Closest pair of points are {p1} and {p2}, distance = {d}")

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
  # Calculate the distance using distance formula. If calculated distance 
  # is less than or equal to the previously calculated minimum value, then
  # append the value and its respective points to their lists. Return 
  # distance at end of method.
  ##################################################################################

  def distanceCalculation(p1, p2):  
      global miniumDistance
      if ((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))**0.5 <= DivideAndConquer.miniumDistance:
          miniumDistance = ((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))**0.5
          DivideAndConquer.point1.append(p1)
          DivideAndConquer.point2.append(p2)
          DivideAndConquer.minimumDis.append(miniumDistance)
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
          DivideAndConquer.mergeSort(left)
          DivideAndConquer.mergeSort(right)
          
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
      min_distance = float('inf')
      for i in range(n):
          for j in range(i+1, n):
              if DivideAndConquer.distanceCalculation(points[i], points[j]) < min_distance:
                  min_distance = DivideAndConquer.distanceCalculation(points[i], points[j])
      return min_distance

  ##################################################################################
  # Determine if points that are near the middle point are the closest points together.
  # Only use this method for values in strip array from dividePoints() method. 
  # Return values to dividePoints() method
  ##################################################################################

  def lineClosestCalc(centerPoints, size, d):
      min_dist = d
      centerPoints = DivideAndConquer.mergeSort(centerPoints)
      for i in range(size):
          for j in range(i+1, size):
              if (centerPoints[j][0] - centerPoints[i][0]) >= min_dist:
                  break
              if DivideAndConquer.distanceCalculation(centerPoints[i], centerPoints[j]) < min_dist:
                  min_dist = DivideAndConquer.distanceCalculation(centerPoints[i], centerPoints[j])
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
          return DivideAndConquer.bruteForce(points, n)
      mid = n//2
      midPoint = points[mid]
      divideLeft = DivideAndConquer.dividePoints(points, mid)
      divideRight = DivideAndConquer.dividePoints(points[mid:], n - mid)
      d = DivideAndConquer.minimum(divideLeft, divideRight)
      CentralPoints = []
      for i in range(n):
          if abs(points[i][0] - midPoint[0]) < d:
              CentralPoints.append(points[i])
      return DivideAndConquer.minimum(d, DivideAndConquer.lineClosestCalc(CentralPoints, len(CentralPoints), d))

  def closestPairCLRS(points):
      #create 10 points randomly between values 0 - 100000
      POINTS = points
      mini, tuple1, tuple2 = float('inf'), 0, 0
      n = len(POINTS) #length of array
      points_by_x = DivideAndConquer.mergeSort(POINTS) #sort the points by x values
      y_First_Array = list(zip(DivideAndConquer.arrayY, DivideAndConquer.arrayX))
      points_by_y = DivideAndConquer.mergeSort(y_First_Array)#sort the points by y values
      DivideAndConquer.dividePoints(points_by_x, n) #divide array into sub components and calculate smallest distance
      #of minimum distances calculated, print the smallest one with its respective points
      for i in range(len(DivideAndConquer.minimumDis)):
          if DivideAndConquer.minimumDis[i] < mini:
              mini = DivideAndConquer.minimumDis[i]
              tuple1 = DivideAndConquer.point1[i]
              tuple2 = DivideAndConquer.point2[i]
              
      return tuple1, tuple2, mini

  ##################################################################################
  # If the DivideAndConquer class needs to be used multiple times, use the __del__ function to reset class variables
  ################################################################################## 

  def __del__(self):
    DivideAndConquer.arrayX, DivideAndConquer.arrayY, DivideAndConquer.points, DivideAndConquer.point1, DivideAndConquer.point2 = [], [], [], [], []
    DivideAndConquer.minimumDis = []
    DivideAndConquer.miniumDistance = float('inf')

##############################################################################################################

## TESTING DATA

POINTS = [(7, 16), (13, 5), (4, 2), (20, 8), (5, 16), (2, 4), (6, 6), (20, 15), (17, 8), (11, 16)]

## KICKOFF CODE

obj = DivideAndConquer()
del obj
# Expected output: 
# Closest pair of points are (7,16) and (5,16), distance = 2.0


# Test data that generates an array of 10 random points with x/y values between 0 and 1000
points = DivideAndConquer.generate_pts(10,1000)
p1, p2, d = DivideAndConquer.closestPairCLRS(points)
print(f'\n\nNew points: {points}\n')
print(f"Closest pair of points are {p1} and {p2}, distance = {d}")
