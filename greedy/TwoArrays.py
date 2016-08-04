import heapq

class TwoArray():

    def findPermutation(self, A,B,n):
        minHeap = []
        maxHeap = []

        for a_ in A:
            heapq.heappush(minHeap, int(a_))
        for b_ in B:
            heapq.heappush(maxHeap, int(b_)*-1)

        while heapq:
            try:
                a_ = heapq.heappop(minHeap)
                b_ = heapq.heappop(maxHeap)*-1

                if a_ + b_ < n:
                    return False
            except:
                return True


tests = int(raw_input())
for i in xrange(tests):
    n,sum = raw_input().split(' ')
    A = raw_input().split(' ')
    B = raw_input().split(' ')
    t = TwoArray()
    found = t.findPermutation(A,B,int(sum))
    if found:
        print "YES"
    else:
        print "NO"