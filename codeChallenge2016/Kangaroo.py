'''
Created on Jun 27, 2016

@author: sstimmel
'''

#!/bin/python

import sys

def findSameLandingSpot(x1,v1,x2,v2):
    if x1 < x2:
        l = x1
        u = x2
    else:
        l = x2
        u = x1
    
    if x1 <= x2:
        while x1 <= x2:
            if x1 == x2:
                print "YES"
                return
            
            x1 = x1 + v1
            x2 = x2 + v2
    elif x2 <= x1:
        while x2 <= x1:
            if x2 == x1:
                print "YES"
                return   
            
            x1 = x1 + v1
            x2 = x2 + v2
            
    print "NO"
    

x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]


if (x1 < x2 and v1 < v2) or (x2 < x1 and v2 < v1):
    print "NO"
else:
    findSameLandingSpot(x1, v1, x2, v2)