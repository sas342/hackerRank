#!/bin/python

import sys


#5's first, must be divisible by 3
#3's second, must be divisible by 5

def getPivot(n):
    p = n
    while p >= 0:
        if p % 3 == 0:
            break
        p = p - 5

    return p

def run(n):
    if n < 3:
        return -1

    rv = ""

    p = getPivot(n)

    if p < 0:
        return -1
    rv = p * '5' + (n -p)*'3'
    return int(rv)
   



t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print run(n)