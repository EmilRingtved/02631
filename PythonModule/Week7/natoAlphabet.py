import numpy as np
dict = {'A':'Alpha', 'B':'Bravo','C':'Charlie', #dictionary for relating letters to NATO letters
        'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 
        'G':'Golf',"H":"Hotel", 'I':'India', 
        'J':'Juliet', 'K':'Kilo', 'L':'Lima', 
        'M':'Mike', 'N':'November', 'O':'Oscar', 
        'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 
        'S':'Sierra', 'T':'Tango', 'U':'Uniform', 
        'V':'Victor', 'W':'Whiskey', 'X':'Xray', 
        'Y':'Yankee', 'Z':'Zulu'}
def textToNato (word):
    wordlist = list(word.upper()) #convert the string to a list containing all letter in all-caps
    #print(wordlist) #prints the wordlist
    NATOword = "-".join([dict[x] for x in wordlist]) #Converts each letter in the wordlist to dictionary value and joins them with "-" 
    return NATOword 