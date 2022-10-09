import numpy as np
def computeItemCost (resourceMatrix, resourceCost):
    itemCost = np.array(resourceCost) #sets the len of the returned array
    for i in range(len(resourceMatrix[1])):
       itemCost[i] = np.dot(resourceMatrix[:,i],resourceCost)#select each coloum of the matrix and dot it with the resource cost vector
    return itemCost
