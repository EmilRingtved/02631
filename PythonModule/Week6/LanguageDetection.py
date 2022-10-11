import numpy as np

def computeLanguageError(Ft):
    file  = np.loadtxt(open('letter_frequencies.csv',"rb"),delimiter=",",skiprows=1,usecols = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
    Fl = np.array(list(file)).astype("float")
    E = np.zeros(15)
    for i in range(15):
        SE = 0
        for j in range(26):
            SE = SE + np.sum(np.square(np.subtract(Ft[j], Fl[j,i])))
        E[i] = SE
    return(E)