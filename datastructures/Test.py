'''
Created on Jun 24, 2016

@author: sstimmel
'''

n = int(raw_input().strip())
times = []
total = long(0)
index = long(0)
for a_i in xrange(n):
    tmp = raw_input().strip().split(' ')
    t1 =long(tmp[0])
    t2 = long(tmp[1])
    
    if index == 0:
        index = t1
    
    wait = index - t1 + t2
    print "wait=",wait
    total = total + wait
    index = index + t2
    
print total / n