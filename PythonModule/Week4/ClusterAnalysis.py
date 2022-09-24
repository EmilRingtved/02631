import numpy as np
def assignCluster(cluster,m1Mean,m2Mean):
    m1Assigned = np.array()
    m2Assigned = np.array()
    for i in range(len(cluster)):
        if abs(cluster[i] - m1Mean) <= abs(cluster[i] - m2Mean):
            cluster[i] = m1Assigned[i]
        elif abs(cluster[i] - m2Mean < abs(cluster[i] - m1Mean)):
            cluster[i] = m2Assigned[i]
    return m1Assigned, m2Assigned

def clusterMean(array):
    arraySum = 0
    for i in range(len(array)): #loop through the array of meassurements
        arraySum += array[i] 
    return (arraySum / len(array)) #return calculated average

def clusterAnalysis(reflactance):
    m1 = np.array()
    m2 = np.array()
    for i in range(len(reflactance)):
        if (reflactance[i] % 2 == 0): #check if odd or even by remainder
            m1[i] = reflactance[i]    #add the value to cluster 1
        else:
            m2[i] = reflactance[i]    #add the value to cluster 2

    m1_old = m1
    m2_old = m2 
    while(1):
        if  (m1 == m1_old) and (m2 == m2_old): # cluster sorted
            for i in range(len(reflactance)):
                
            m1, m2 = assignCluster(reflactance,clusterMean(m1_old),clusterMean(m2_old)

