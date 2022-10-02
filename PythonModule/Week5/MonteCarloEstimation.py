import numpy as np
def circleAreaMC(xvals,yvals):
    aSqr = 4 #Asquare = 4
    r = 1 #radius of the circle is 1
    n = 0 #point in the circle
    for i in range(len(xvals)):
         distOrigo = xvals[i]**2 + yvals[i]**2 #calculate the distance form the origin of the circle a point
         if distOrigo <= 1: #if the magnetude of the generated vector is <= 1 it is within the circle
            n = n+1
    aCirc = 4*(n/len(xvals))#calculates the area of the circle
    return aCirc