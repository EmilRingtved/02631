from pickle import TRUE
import numpy as np
def bacteriaGrowth(n0, alpha, k, N):
    if N <= n0:
        return 0
    tN = 1
    while(TRUE):
        n = (1 + alpha * (1-(n0/k)))*n0
        if n < N:
            n0 = n
            tN = tN + 1
        elif N <= n:
            return tN
