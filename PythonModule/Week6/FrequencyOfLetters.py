from mimetypes import init
import numpy as np
from collections import Counter

def letterFrequency(filename):
    initLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    freqNum = []
    values = []
    n = 0
    totVals = []
    letterCounter = Counter()
    for i in range(len(initLetters)):
        letterCounter[initLetters[i]] = 0
    with open(filename) as f:
        smallText = list(f.read())
        smallText = [text.lower() for text in smallText]#change all text to lower case
        smallTextSorted = [char for char in smallText if char.isalpha()] #cleans the sorted text for special chars
        letterCounter.update(Counter(smallTextSorted)) #update counter

    vals = [count for count in sorted(letterCounter.items())] #assign the sorted count to a new array array
    vals = np.vstack(vals)[:,1] #select count coulum
    vals = vals.astype(float) #convert array to int array
    freqNum =  vals / vals.sum() * 100 # calc frequency of each number
    return(freqNum)