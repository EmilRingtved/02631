import numpy as np
import math

def boxArea(boxCorners,area):
    ABoxArea = (boxCorners[1]-boxCorners[0])*(boxCorners[5]-boxCorners[4])
    BBoxArea = (boxCorners[3]-boxCorners[2])*(boxCorners[7]-boxCorners[6])
    Intersect = max(0,min(boxCorners[1],boxCorners[3]) - max(boxCorners[0],boxCorners[2])) * max(0,min(boxCorners[5],boxCorners[7]) - max(boxCorners[4],boxCorners[6]))
    if area == "Box1":
        a = ABoxArea
    elif area == "Box2":
        a = BBoxArea
    elif area == "Intersection":
        a = Intersect
    elif area == "Union":
        a = ((ABoxArea) + (BBoxArea)) - (Intersect)
    return a
    