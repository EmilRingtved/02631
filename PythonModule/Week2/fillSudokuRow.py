import numpy as np
def fillSudokuRow(row):
    missingNum = 45 - sum(row)
    for x in range(len(row)):
        if row[x] == 0:
            row[x] = missingNum
    return row
    