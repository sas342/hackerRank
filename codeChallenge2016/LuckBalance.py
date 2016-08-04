'''
Created on Jun 27, 2016

@author: sstimmel
'''

def findMaxLuck(ary, luck, k):    
    #sort ary
    ary.sort(reverse=True)
    
    z = 1
    for x in ary:
        if z <= k:
            luck = luck + x
        else:
            luck = luck - x
        
        z = z + 1
    
    print luck
    
    
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
luck = 0
ary = []
for i in xrange(n):
    li,ti = raw_input().strip().split(' ')
    li,ti = [int(li),int(ti)]
    
    if ti == 0:
        luck = luck + li
    else:
        ary.append(li)

findMaxLuck(ary, luck, k)
    