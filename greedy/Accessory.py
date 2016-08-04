


#!/bin/python

import sys

'''
L - # accessories
A - # types of accessories (1..A)
N - # in Grouping
D - # of distinct in each grouping
'''
def printMaxCost(L,A,N,D):

    numGroups = L / N

    if (numGroups * D) > A:
        print "SAD"
        return

    #(N - D) * (L-N) = # duplicates allowed
    print "L=",L,"A=",A,"N=",N,"D=",D
    numDupsEach = (N-D) + 1

    print "numDupsEach=",numDupsEach
    cost = 0
    while L > 0:

        for i in xrange(numDupsEach):
            cost += A
            L -= 1

        A -= 1


        print "L=,", L, "A=", A, "N=", N, "D=", D
        print "cost=",cost
    print cost

T = int(raw_input().strip())
for a0 in xrange(T):
    L,A,N,D = raw_input().strip().split(' ')
    L,A,N,D = [int(L),int(A),int(N),int(D)]
    printMaxCost(L, A, N, D)


