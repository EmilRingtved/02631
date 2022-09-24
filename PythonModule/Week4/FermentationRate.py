import numpy as np
def fermentationRate(measuredRate, lowerBound,upperBound):
    arraySum = 0
    arrayLen = len(measuredRate)
    for i in range(len(measuredRate)): #loop through the array of meassurements
        if (lowerBound < measuredRate[i]) and (measuredRate[i] < upperBound): #check bounds
            arraySum += measuredRate[i] #if within bounds add to the sum
        else:
            arrayLen = arrayLen - 1
    return (arraySum / arrayLen) #return calculated average
