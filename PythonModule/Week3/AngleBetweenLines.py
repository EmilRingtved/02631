import numpy as np
import math as math

def acuteAngle(v1,v2):
    if v1[0] == v2[0] and v1[1] == v2[1]:
        theta = 0
    else:
        if v1[0] < 0:
            theta = math.acos(np.dot(-v1,v2))
        else:
            theta = math.acos(np.dot(v1,v2))
    return theta