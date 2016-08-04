'''
Created on Apr 9, 2016

@author: sstimmel
'''
#!/bin/python
def insertionSort(ar):    
    rIndex = len(ar)-1
    e = ar[rIndex]
    while(rIndex > 0 and e < ar[rIndex-1]):
        ar[rIndex] = ar[rIndex-1]
        rIndex = rIndex -1
        printArray(ar)
    
    
    ar[rIndex] = e
    printArray(ar)

def printArray(ar):
    row = ""
    for x in ar:
        row = row+" "+str(x)
    
    print row.lstrip()
    
m = input()
ar = [i for i in raw_input().strip().split()]
insertionSort(ar)
