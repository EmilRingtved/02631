import numpy as np
R = 6.371*10**6
g0 = 9.82
def gravitationalPull(x):
    if R <= x:
        g = g0*(R**2/x**2)
    elif 0<= x <= R:
        g = g0*(x/R)
    return g