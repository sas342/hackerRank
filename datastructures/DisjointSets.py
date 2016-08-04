'''
Created on Jun 24, 2016

@author: sstimmel
'''
from Queue import Queue
import sys
import time

class Node():
    def __init__(self, value):
        #upper bound on height of x
        self.rank = 0
        self.value = value
        self.parent = self
'''
uses Forest approach over linked-list

'''
class DisjointSets():
    
    def __init__(self, size):
        #self.sets = []
        self.rootList = []
        self.sizeList = []
        
        for i in xrange(size+1):
            self.rootList.append(i)
            self.sizeList.append(1)
    
    def printArrays(self):
        print "rootList=",self.rootList
        print "sizeList=",self.sizeList
    #make set with one node
    #simulate tree
    def makeSet(self, x):
        #n = Node(x)
        #self.sets.append(n)
        return x
    
    def printSize(self, x):
        r = self.findSet(x)
        print self.sizeList[r]
        
    def union(self, x, y):
        self.link(self.findSet(x), self.findSet(y))
    
    #normally would be based on rank, but using size instead
    def link(self, x, y):
        if x == y:
            return
        if self.sizeList[x] > self.sizeList[y]:
            self.rootList[y] = x
            self.sizeList[x] = self.sizeList[x] + self.sizeList[y]
        else:
            self.rootList[x] = y
            self.sizeList[y] = self.sizeList[y] + self.sizeList[x]
            
        #if x.rank > y.rank:
        #    y.parent = x
        #else:
        #    x.parent = y
        #    if x.rank == y.rank:
        #        y.rank = y.rank + 1
    
    def findSet(self, x):
        if x == self.rootList[x]:
            return x
        
        return self.findSet(self.rootList[x])
            
        #if x != x.parent:
        #    x.parent = self.findSet(x.parent)
        #return x.parent

    
    
    
class GraphComponents():
    
    def __init__(self):
        self.s1 = {}
        self.s2 = {}
    
    
    
    def addEdge(self, gi, bi):
        if gi not in self.s1:
            self.s1[gi] = [bi]
        else :
            self.s1[gi].append(bi)
            
        if bi not in self.s2:
            self.s2[bi] = [gi]
        else :
            self.s2[bi].append(gi)
    
    #similar to Breadth First Search using Queue to keep track of children
    def findMaxAndMin(self):
        visitedNodes = sorted([])
        min = sys.maxint
        max = 0
        #for a in self.s1:
        #t1 = time.time()
        while self.s1:
            a = self.s1.keys()[0]
            connectedNodes = self.__findConnected(a, visitedNodes)
           
            if connectedNodes < min:
                min = connectedNodes
            
            if connectedNodes > max:
                max = connectedNodes
        #t2 = time.time()
        #print t2-t1
        return [min,max]
                
    def __findConnected(self, node, visitedNodes):
        q = Queue()
        
        q.put(node)
        numberOfNodes = 0
        
        while not q.empty():
            entry = q.get()
            if entry not in visitedNodes:
                visitedNodes.append(entry)
                numberOfNodes = numberOfNodes + 1
                
                if entry in self.s1:
                    l = self.s1[entry]
                    del self.s1[entry]
                else:
                    l = self.s2[entry]
                    del self.s2[entry]
                
                for x in l:
                    q.put(x)
        
        return numberOfNodes
                    
    
    def printAll(self):
        print self.s1
        print self.s2
 

#g = GraphComponents()
#n = int(raw_input())
#for x in xrange(n):
#    tmp = raw_input().strip().split(' ')
#    g.addEdge(int(tmp[0]), int(tmp[1]))
    
#t = g.findMaxAndMin()
#print t[0], t[1]



tmp = raw_input().strip().split(' ')
n = int(tmp[0])
q = int(tmp[1])
ds = DisjointSets(n)
#ds.printArrays()
for i in xrange(q):
    tmp = raw_input().strip().split(' ')
    if tmp[0] == 'Q':
        ds.printSize(int(tmp[1]))
    elif tmp[0] == 'M':
        ds.union(int(tmp[1]), int(tmp[2]))
    #ds.printArrays()   
