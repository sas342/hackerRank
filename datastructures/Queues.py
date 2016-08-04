import heapq
from math import sqrt
import sys

class DownToZero():
    def __init__(self):
        self.cache = {}

    def findFactors(self, n):
        factors = []
        mid = n / 2
        for i in xrange(n-1,2,-1):

            if n % i == 0:
                t = n / i
                if factors.count(t) == 0:
                    factors.append(i)

        return factors

    def reduce(self, n):
        print "reduce",n
        if n == 0:
            return 0

        if self.cache.has_key(n):
            return self.cache[n]

        factors = self.findFactors(n)
        factors.append(n - 1)

        cnt = sys.maxint
        for i in factors:
            c = 1 + self.reduce(i)
            self.cache[i] = c
            if c < cnt:
                cnt = c

        return cnt

    def run(self):
        q = int(raw_input())
        for i in xrange(q):
            t = int(raw_input())
            reduce(t)

class Cookies():

    def __init__(self):
        self.queue = []

    def findSweetness(self, array, sweetness):
        for x in array:
            heapq.heappush(self.queue, int(x))

        if len(array) < 2:
            print "-1"
            return

        ops = 0


        min = self.queue[0]

        while min < sweetness:
            #self.queue.printHeap()
            min = heapq.heappop(self.queue)
            #print 'min=',min
            try:
                secondMin = heapq.heappop(self.queue)
            #print 'secodnmin =',secondMin
            except:
                print "-1"
                return

            newCookie = (1 * min) + (2 * secondMin)
            ops = ops + 1

            heapq.heappush(self.queue, int(newCookie))

            min = self.queue[0]
        print ops


#n,k = raw_input().strip().split(' ')
#tmp = raw_input().strip().split(' ')
#c = Cookies()
#c.findSweetness(tmp, int(k))

d = DownToZero()
print d.reduce(214567)