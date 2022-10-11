import numpy as np

def computeLanguageError():
    f  = np.loadtxt(open('02631\PythonModule\Week6\letter_frequencies.csv',"rb"),delimiter=",",skiprows=1,usecols = (1,2,3,4,5,6,7,8,9,10))
    res = np.array(list(f)).astype("float")
    return(res)
print(computeLanguageError())