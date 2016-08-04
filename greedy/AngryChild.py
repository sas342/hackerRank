'''
https://www.hackerrank.com/challenges/angry-children

'''


def findMinMax(A, n,k):

    #start 1st pointer at k
    #start 2nd pointer at 0
    #increment both at same time and record min change

    p1 = 0
    p2 = k - 1

    min = A[p2] - A[p1]
    while (p2 < n - 1):
        p1 += 1
        p2 += 1

        v = A[p2] - A[p1]
        if v < min:
            min = v


    return min


n = int(raw_input())
k = int(raw_input())
A = []
for i in xrange(n):
    A.append(int(raw_input().strip()))

A.sort()
print findMinMax(A,n,k)