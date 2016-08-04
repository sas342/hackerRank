'''
Created on Apr 9, 2016

@author: sstimmel
'''
def findPalindromeIndex(string):
    rIndex = len(string) - 1
    n = len(string)
    
    mid = len(string) / 2
    
    invalidIndex = -1
    for x in xrange(mid):
        print string[x]," ",string[n-x-1]
        if (string[x] != string[n-x-1]):
            if (string[x] == string[n-x-2]):
                invalidIndex = n-x-1
            else:
                invalidIndex = x
            return invalidIndex
    
    
    return invalidIndex
    
numCases = int(raw_input())
for x in range(0, numCases, 1):
    string = str(raw_input())
    print findPalindromeIndex(string)