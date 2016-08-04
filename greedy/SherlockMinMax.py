
'''
https://www.hackerrank.com/challenges/sherlock-and-minimax
'''
from math import fabs

def findMin(n, A, P, Q):

    #remove any from array outside
    copy = [int(x) for x in A]

    for i in xrange(n):
        #print i

        if (copy[i] < P and ((copy[i+1]-copy[i]) /2) +copy[i] < P) or (copy[i] > Q and Q < ((copy[i] - copy[i-1])/2) + copy[i-1]):
            A.remove(copy[i])

    n = len(A)
    maxDiff = 0
    maxLoc = 0
    for i in xrange(1, n, 1):

        diff = A[i] - A[i - 1]
        #print A[i], " ", A[i - 1], " diff=", diff
        if diff > maxDiff:
            maxDiff = diff
            maxLoc = i

    x1 = A[maxLoc - 1]
    x2 = A[maxLoc]
    #print "x1=",x1,"x2=",x2," maxDiff=",maxDiff/2
    maxDiff = maxDiff / 2
    xmid = x1 + maxDiff

    #checkout P and Q
    m = 0
    maxValue = 0
    for c in [P,xmid,Q]:
        min = abs(copy[0]-c)
        for i in xrange(1,len(copy),1):
            v = abs(copy[i]-c)
            if v < min:
                min = v

        if min > m:
            m = min
            maxValue = c
        #print "c=",c,"min=",min
    print maxValue
    return




n = int(raw_input())
A = [int(x) for x in raw_input().strip().split(' ')]
P,Q = [int(x) for x in raw_input().strip().split(' ')]
A.sort()

findMin(n, A, P, Q)