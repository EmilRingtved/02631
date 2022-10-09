import numbers
import numpy as np
def movingAvg(y):
    ysmooth = []
    A = []
    B=[]
    
   

    if len(y) == 1: #if the signal is only 1 long special case
        ysmooth = 1*3.0 / 9
        return ysmooth

    #masks for multiplying and adding zeros, not very fast
    for i in range(len(y)):
        B = np.append(B,np.ones(5))
    for i in range(2):
        B[0 + i] = 0
        B[len(B) -1 - i] = 0
    B[len(y)] = 0
    B[len(B) -1 - (len(y))] = 0

    #build the matrix and flips it
    B = np.reshape(B,(5,len(y)))
    B = np.flip(B,0)
    print("B")
    print(B)

    #aranges the matrix with the signal values and  shifts the coloumbs in the matrix
    for i in range(-2,3,1):
        A = np.append(A,np.roll(y,i))
    A = np.reshape(A,(5,len(y)))
    print("A")
    print(A)
    ysmooth = np.sum(A,axis=0) / 9
    return ysmooth
print(movingAvg(np.array([1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0])))