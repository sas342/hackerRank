import heapq

class Orders():
    def __init__(self,t,d,n):
        self.t=t
        self.d = d
        self.n = n

    def value(self):
        return self.t + self.d



    def __cmp__(self, other):
        a = self.t + self.d
        b = other.t + other.d

        if a < b:
            return -1
        if b < a:
            return 1

        if self.n <= other.n:
            return -1

        return 1

orders = []
n = int(raw_input())
j=1
for i in xrange(n):
    t,d = raw_input().split(' ')
    o = Orders(int(t),int(d),j)
    j = j + 1
    heapq.heappush(orders, o)

rv = ""
try:
    while orders:
        min = heapq.heappop(orders)
        rv = rv + str(min.n)+" "
except:
    pass

print rv.strip()