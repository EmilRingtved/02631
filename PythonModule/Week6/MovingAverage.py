import numbers
import numpy as np
def movingAvg(y):
    ysmooth = []
    A = []
    B=[]
    v = [1,2,3,2,1]
   
    #if the signal is only 1 long, special case
    if len(y) == 1: 
        ysmooth = 1*3.0 / 9
        return ysmooth

    #generates an array of nunmbers len(y) by 5 long
    for i in range(len(y)):
        B = np.append(B,np.ones(5)) 
    #inserts zeros in the cornes of the matrix
    for i in range(2):
        B[0 + i] = 0
        B[len(B) -1 - i] = 0
    B[len(y)] = 0
    B[len(B) -1 - (len(y))] = 0
    #generates the weightmatrix
    B = np.reshape(B,(5,len(y)))
    #transpose the weightmatrix, B, and multiply with a weight-diagonal matrix, v
    B = np.transpose(np.dot(np.transpose(B),np.diag(v))) 
    #flip the matrix to arrange the zeros in the correct corners
    B = np.flip(B,0) 

    #aranges the matrix with the signal values and  shifts the coloumbs in the matrix
    for i in range(-2,3,1):
        A = np.append(A,np.roll(y,i))
    A = np.reshape(A,(5,len(y)))
    #multiply the shifted signal-matrix with the weight matrix
    A = B*A
    #sum and devide
    ysmooth = np.sum(A,axis=0) / 9
    return ysmooth