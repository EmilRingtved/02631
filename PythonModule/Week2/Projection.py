import numpy as np
import math

def computeProjection(a):
    b = np.ones(len(a))
    p = np.dot(np.dot(a,b)/(np.linalg.norm(a)**2),a)
    return (p)

