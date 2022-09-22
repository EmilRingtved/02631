import numpy as np

def unitVector(v):
    return v / np.linalg.norm(v)

def angleBetween(v1,v2):
    v1_u = unitVector(v1)
    v2_u = unitVector(v2)
    angle = np.arccos(np.clip(np.dot(v1_u,v2_u),-1.0,1.0))
    return angle

def computePassesGoalLine(point, directionVector):
    RightGoalPost = [105,30.34,105,37.66]
    LeftGoalPost = [0,30.34,0,37.66]
    vg1 = [RightGoalPost[0]-point[0],RightGoalPost[1]-point[1]]
    vg2 = [RightGoalPost[2]-point[0],RightGoalPost[3]-point[1]]
    vg3 = [LeftGoalPost[0]-point[0],LeftGoalPost[1]-point[1]]
    vg4 = [LeftGoalPost[2]-point[0],LeftGoalPost[3]-point[1]]

    if  angleBetween(vg1,directionVector) <= angleBetween(vg1,vg2) :
        score = True
    elif angleBetween(vg4,directionVector) <= angleBetween(vg3,vg4) :
        score = True
    else:
        score = False
    return score