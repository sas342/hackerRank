'''
Created on Apr 8, 2016

@author: sstimmel
'''

def binarySearch(sortedlist, character):    
    if len(sortedlist) == 1:
        return sortedlist[0] == character
    
    mid = len(sortedlist) / 2
    
    if (sortedlist[mid] == character):
        return True
    
    if (sortedlist[mid] < character):
        return binarySearch(sortedlist[mid:], character)
    elif (sortedlist[mid] > character):
        return binarySearch(sortedlist[0:mid], character)
    
def findMinimumAnagramChange(string):
    
    
    if len(string) % 2 == 1:
        return -1
    
    length = len(string)
    mid = length / 2
    leftHalf = sorted(list(string[0:mid]))
    rightHalf = sorted(list(string[mid:length]))
    
    minChanges = 0
    for i in range(0,mid,1):
        j = 0
        matched = binarySearch(rightHalf, leftHalf[i])
        if (matched):
            rightHalf.remove(leftHalf[i])
        
    return len(rightHalf)
    
numCases = int(raw_input())
for x in range(0, numCases, 1):
    string = str(raw_input())
    print findMinimumAnagramChange(string)


