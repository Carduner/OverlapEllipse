#I have not given or received any unauthorized assistance on this assignment
#Max Carduner, 11/01/2018

#main function calls print intro, overlap, stores results, then prints
#takes in a list of lists representing ellipses for an [ellipse(majorAxis, Point(1,3), Point(2,7)),ellipse(majorAxis, Point(1,1), Point(3,7))]

#overlap function calls square function to produce a square, and sim to do conduct simulation to get approximated area

import math
import random

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        'initialize coordinates to (xcoord, ycoord)'
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        'set x coordinate of point to xcoord'
        self.x = xcoord

    def sety(self, ycoord):
        'set y coordinate of point to ycoord'
        self.y = ycoord

    def get(self):
        'return coordinates of the point as a tuple'
        return (self.x, self.y)

    def move(self, dx, dy):
        'change the x and y coordinates by dx and dy'
        self.x += dx
        self.y += dy

    def distance(self, x):
        'returns distance between self and another point object'
        return ((self.x - x.get()[0])**2 + (self.y - x.get()[1])**2)**.5




class ellipse(Point):
    'class that represents an ellipse on the plane'

    def __init__(self, majorAxis=0, foc1=Point(), foc2=Point()):
        'initialze coordinates'
        self.a = majorAxis
        self.foc1 = foc1
        self.foc2 = foc2


    def set(self, majorAxis, foc1=Point(), foc2=Point()):
        'set major axis and two focal points of ellipse'
        self.a = majorAxis
        self.foc1 = foc1
        self.foc2 = foc2

    def get(self):
        'return coordinates of ellipse in tuple'
        return (self.a, self.foc1.get(), self.foc2.get())

    def getx(self):
        'return x of both foci in tuple'
        return (self.foc1.get()[0], self.foc2.get()[0])

    def gety(self):
        'return x of both foci in tuple'
        return (self.foc1.get()[1], self.foc2.get()[1])

    def area(self):
        'returns area of ellipse'
        a = self.foc1.distance(self.foc2)/2
        b = (self.a**2 - a**2)**.5
        area = (math.pi * self.a * b)
        area = round(area,4)
        return area

    def circumference(self):
        'returns approximated circumference using Ramanujan Approximation 3'
        a = self.foc1.distance(self.foc2) / 2
        b = (self.a**2 - a**2)**.5
        h = ((self.a - b)**2)/((self.a + b)**2)
        p = (math.pi*(self.a + b))*(1+((3*h)/(10 + (4-3*h)**.5)))
        p = round(p,4)
        return p

    def inEllipse(self, point=Point()):
        'returns True if in Ellipse, otherwise False'
        distance = self.foc1.distance(point) + self.foc2.distance(point)
        if distance <= (self.a * 2):
            return True
        else:
            return False




def main(ellipses, n):
    'returns approximated area of overlap between all ellipses passed using monte carlo simulation with n number of trials'

    # call function to print intro and explain what function is doing
    print_intro()

    #loop through ellipses, calculating overlap with all combinations
    for i in ellipses:
        for j in ellipses:
            area1 = overlap(i,j,n)
            area2 = overlap(j,i,n)
            area = round((area1+area2)/2,4)
            print('Overlap between ellipse {} and {} is approximately {}'.format(i.get(),j.get(),area))



def print_intro():
    print('Hello. This function will approximate the area of overlap between all ellipses passed in the main function as a list using monte carlo simulation.')


def overlap(a,b,n):
    'returns area of overlap using monte carlo simulation with n trials'
    p,length = square(a,b)
    area = sim(p,length,a,b,n)
    return area


def square(a,b):
    'returns dimensions of square that fits around ellipses'
    Xmin = min(a.getx() + b.getx())
    Xmax = max(a.getx() + b.getx())
    Ymin = min(a.gety() + b.gety())
    Ymax = max(a.gety() + b.gety())
    buffer = max(a.get()[0], b.get()[0])
    length = max(Ymax-Ymin,Xmax-Xmin) + (buffer*2)
    bottomLeftPoint = Point(Xmin-buffer,Ymin-buffer)
    return bottomLeftPoint, length



def sim(p,length,a,b,n):
    'returns area of overlap between ellipse a and b with monte carlo simulation of n trials'
    s = 0
    xmin = p.get()[0]
    ymin = p.get()[1]
    for i in range(n):
        randomPoint = Point(xmin,ymin)
        dx = random.uniform(xmin, xmin+length)
        dy = random.uniform(ymin, ymin+length)
        randomPoint.move(dx, dy)
        #check if randomPoint is in both ellipses
        if a.inEllipse(randomPoint) and b.inEllipse(randomPoint):
            s+=1
    return round((s/n)*(length*length),4)

#run it as commented out below
#main([ellipse(5, Point(1,3), Point(2,7)),ellipse(5, Point(1,1), Point(3,7)),ellipse(4,Point(8,8),Point(10,15))],10000)

