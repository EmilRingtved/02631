
import numpy as np
import array as arr
def removeIncomplete(id):
    idComplete = np.array([])
    idClean = (np.floor(id))

    for i in range(len(idClean)):
        found = 0
        target = idClean[i]
        #print(target)

        for x in range(len(idClean)):
            if idClean[x] == target:
                found += 1
        if found == 3:
            #print("Complete!")
            idComplete = np.append(idComplete,id[i])
    return idComplete
