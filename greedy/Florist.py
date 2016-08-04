
'''
n flowers, k friends
A is cost of flowers sorted
'''
def findCost(A, n, k):
    cost = 0

    timesThru = 1
    bought = 0
    while bought < n:


        for i in xrange(k):
            #print "i=",i
            cost += (timesThru * A[n-bought-1])
           # print "cost=",cost," ",timesThru," ",A[n-bought-1]
            bought += 1

            if bought == n:
                break

        timesThru += 1

    return cost


n,k = [int(x) for x in raw_input().strip().split(' ')]
A = [int(x) for x in raw_input().strip().split(' ')]

A.sort()
print findCost(A,n,k)