from pickle import TRUE
import numpy as np
def bacteriaGrowth(n0, alpha, k, N):
    tN = 1
    while(TRUE):
        print(n0)
        n = (1 + alpha * (1-(n0/k)))*n0
        print(n)
        if n < N:
            n0 = n
            tN = tN + 1
        elif N <= n:
            return tN
