
from __future__ import print_function
import sys




def reverse(arr):
    for x in range(len(arr)-1,-1,-1):
        print(arr[x],sep='',end=' ')


def hrGlassCnt(grid, startx, starty):
   
    cnt = 0
    cnt = grid[starty][startx]+grid[starty][startx+1]+grid[starty][startx+2]
    cnt += grid[starty+1][startx+1]
    cnt += grid[starty+2][startx]+grid[starty+2][startx+1]+grid[starty+2][startx+2]
    
    return cnt

def hourGlass(grid):
    hlen = 3
    hheight = 3
    
    length = len(grid[0])
    height = len(grid)
    
    maxcnt = -sys.maxint-1
    for i in xrange(height-hheight+1):
        
        for j in xrange(length-hlen+1):
            cnt = hrGlassCnt(grid, i, j)
            
            if (cnt > maxcnt):
                maxcnt = cnt
           
    
    return maxcnt 

def q1(seqList, lastAns, x, y):
    s = ((x ^ lastAns) % len(seqList))
    #print("q1", s)
    seq = seqList[s]
    seq.append(y)
   # print(seqList)
    return seq

def q2(seqList, lastAns, x, y):
    #print(x,"^",lastAns,"%",len(seqList))
    s = ((x ^ lastAns) % len(seqList))
    seq = seqList[s]
    #print("seq=",seq,"y=",y)
    index = y % len(seq)
    lastAns = seq[index]
    print(lastAns)
    return lastAns


    

#arr = []
#for arr_i in xrange(6):
r1 = map(int,raw_input().strip().split(' '))
numSeq = r1[0]
numQ = r1[1]
seqList = list()
for x in xrange(numSeq):
    seqList.append(list())

lastAns = 0
for i in xrange(numQ):
    r = map(int,raw_input().strip().split(' '))
    q = r[0]
    x = r[1]
    y = r[2]
    
    if q == 1:
        q1(seqList, lastAns, x,y)
    elif q == 2:
        lastAns = q2(seqList, lastAns,x,y)
#cnt = hourGlass(arr)
#print(cnt)