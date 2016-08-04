'''
Created on Apr 9, 2016

@author: sstimmel
'''
#!/bin/python
def insertionSort(ar):    
    n = len(ar)
    
    for rIndex in range(1,n,1):
        e = ar[rIndex]
        innerIndex = rIndex
        while (innerIndex > 0 and e < ar[innerIndex-1]):
            tmp = ar[innerIndex-1]
            ar[innerIndex-1] = e
            ar[innerIndex] = tmp
            innerIndex = innerIndex-1
            
    
        printArray(ar)
    
    
   
    #printArray(ar)

def printArray(ar):
    row = ""
    for x in ar:
        row = row+" "+str(x)
    
    print row.lstrip()
    
m = input()
ar = [i for i in raw_input().strip().split()]
insertionSort(ar)
