# QuickHull Convex Hull Divide and Conquor Algorithm
# Author Anant Joshi (anant.joshi@live.com)
import graphics as graphics
from math import *
import random
import time

#set total number of points to be randomly generated
NUM_POINTS = 20

#slow down visualization time
SLOWDOWN_PER_STEP = 0.25


#initialize graphics window globally
win = graphics.GraphWin("Convex Hull", 1000, 1000)
win.setBackground("white")

def convexHull(pList: list) -> list:
    
    #loop to draw all points in list
    for i in pList:
        gPoint = graphics.Circle(graphics.Point(i[0], i[1]), 5)
        gPoint.setFill("blue")
        gPoint.draw(win)


    #define resulting conver hull list
    convexHullList = []


    #find left-most and right-most points and add to result
    leftPoint, rightPoint = min(pList), max(pList)
    convexHullList.append(leftPoint)
    convexHullList.append(rightPoint)

    #display/highlight points to yellow color using highlightPoint() function and join both points with a line
    highlightPoint(leftPoint)
    highlightPoint(rightPoint)
    joinPoints(leftPoint, rightPoint).draw(win)
    print(leftPoint)
    print(rightPoint)


    #call upperHull algorithm for upper part of convex hull
    allPointsUpper = upperHull(leftPoint, rightPoint, pList)

    #call upperHull algorithm for lower part of convex hull (lower hull)
    allPointsLower = upperHull(rightPoint, leftPoint, pList)

    #print(allPointsUpper)
    #print(allPointsLower)

    #create final result list (convexHullList)
    convexHullList += allPointsUpper
    convexHullList += allPointsLower


    #close graphics window at the end
    win.getMouse()
    win.close()

    print("convexHullList is ")
    print(convexHullList)

    return convexHullList

    


def upperHull(a: list, b: list, pList: list):
    
    #base case for when there are no points to the left of selected vector
    if len(pList) == 0:
        return []

    upperHullPoints = []
    resultPoints = []
    #find p farthest from the line
    maxDis = 0.0
    furthestPoint = []
    for p in pList:
        if isLeft(a, b, p) == True:
            upperHullPoints.append(p)
            pDis = findDistance(a, b, p)
            print(pDis)
            if(pDis > maxDis):
                maxDis = pDis
                furthestPoint = p
    print("maxDis = ")
    print(maxDis)
    print("Furthest Point is ")
    print(furthestPoint)


    #add the furthest point to convexHull result (finalList)
    
    if furthestPoint:
        resultPoints.append(furthestPoint)
        highlightPoint(furthestPoint)
        joinPoints(a, furthestPoint).draw(win)
        joinPoints(b, furthestPoint).draw(win)

    #calling upperHull algorithm on region 1 (left of vector a, furthestPoint) and region 3 (left of vector furthestPoint, b)
    region1 = upperHull(a, furthestPoint, upperHullPoints)
    region3 = upperHull(furthestPoint, b, upperHullPoints)


    resultPoints += region1
    resultPoints += region3

    
    #sleep function to slow down convexHull building to visualize for graphics value -> enable to slow down graphics viz and see step-by-step calculation
    time.sleep(SLOWDOWN_PER_STEP)
    return resultPoints

        
    
# Graphical Functions to display poitns
    
def highlightPoint(p: list):
    hullPoint = graphics.Circle(graphics.Point(p[0], p[1]), 7.5)
    hullPoint.setFill("yellow")
    hullPoint.draw(win)
    

def joinPoints(a: list, b: list):
    line = graphics.Line(graphics.Point(a[0], a[1]), graphics.Point(b[0], b[1]))
    return line


# Geometric Calculation Functions

def findDistance(a: list, b: list, p: list):
    #rewriting coordinates for simply geometric syntax
    ax, ay, bx, by = a[0], a[1], b[0], b[1]
    px, py = p[0], p[1]
    d = 0
    d = (abs(((bx - ax) * (ay - py)) - ((ax - px) * (by - ay)))) / sqrt((pow((bx - ax), 2)) + (pow((by - ay), 2)))
    return d


def isLeft(a: list, b: list, c: list) -> bool:
    #rewriting coordinates for simply geometric syntax
    ax, ay, bx, by, cx, cy = a[0], a[1], b[0], b[1], c[0], c[1]

    #we will take point a and point b and do the cross product of these points
    z = ((bx - ax) * (cy - ay)) - ((cx - ax) * (by - ay))

    if z > 0:
        return True
    else:
        return False


# Randomly generate set of points
# Randomly generate set of points
pointList = []
for _ in range(NUM_POINTS):
    x, y = random.randint(300,700), random.randint(300, 700)
    pointList.append([x,y])

'''
# Generate points by clicking on the canvas
pointList = []
for _ in range(NUM_POINTS):
    p = win.getMouse()
    x, y = p.getX(), p.getY()
    pointList.append([x,y])
    print(x, y)
    win.redraw()
'''

#Main Driver Code: result is stored in variable chResult which used used below for comparison
chResult = convexHull(pointList)

print(chResult)