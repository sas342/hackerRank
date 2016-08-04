



N,M = [int(x) for x in raw_input().split(' ')]

T = []
for i in xrange(N):
    T.append(0)

for i in xrange(M):
    a,b,k = [int(x) for x in raw_input().split(' ')]
    T[a-1] += k
    if b < N:
        T[b] -= k

max = 0
current = 0
for i in xrange(N):
    v = T[i]
    current += v
    if current > max:
        max = current


print max
