from math import floor, log
import abc

class Heap():
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        self.heap = []
    
    def size(self):
        return len(self.heap)
    
    def height(self):
        return floor(log(self.size()))
    
    def printRoot(self):        
        print self.heap[0]
        #output.write(str(self.heap[0])+'\n')
        #pass
    
           
    def printHeap(self):
        print self.heap
    
    def root(self):
        if len(self.heap) == 0:
            return None
        
        return self.heap[0]
    
    def remove_root(self):
        #swap head with last
        n = self.size()
        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[n-1]   
        self.heap.pop()
        
        self.__downheap(0)
        
        return root
    
    @abc.abstractmethod
    def __downheap(self, value):
        return
    
    def remove(self, value):
       
        try:
            i = self.heap.index(value)
            self.heap[i] = self.heap[self.size()-1]
            self.heap.pop()
            self.__downheap(i)
        except:
            pass


class MinHeap(Heap):


    def insert(self, value):
        # add to end of list
        self.heap.append(value)

        n = self.size()
        if n == 1:
            return

        p = n / 2
        # print "p=",p," heap is ",self.heap," n=",n
        while p != 0 and self.heap[n - 1] < self.heap[p - 1]:
            # swap p and n
            tmp = self.heap[p - 1]
            self.heap[p - 1] = self.heap[n - 1]
            self.heap[n - 1] = tmp

            n = p
            p = p / 2


    def _Heap__downheap(self, index):
        size = self.size()

        c = index + 1
        # print "c=",c
        if c * 2 <= size:
            left = self.heap[c * 2 - 1]
            min = c * 2 - 1
            if c * 2 < size:
                right = self.heap[c * 2]
                # print "left=",left," right=",right
                if right < left:
                    min = c * 2
            # print "min=",min
            if self.heap[min] < self.heap[index]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[min]
                self.heap[min] = tmp
                self._Heap__downheap(min)


class MaxHeap(Heap):
   
           
    def insert(self, value):
        #add to end of list
        self.heap.append(value)
        
        n = self.size()
        if n == 1:
            return
        
        p = n / 2
        #print "p=",p," heap is ",self.heap," n=",n
        while p != 0 and self.heap[n-1] > self.heap[p-1]:
            #swap p and n
            tmp = self.heap[p-1]
            self.heap[p-1] = self.heap[n-1]
            self.heap[n-1] = tmp
            
            n = p
            p = p / 2
    
    def _Heap__downheap(self, index):
        size = self.size()
        
        c = index + 1
       # print "c=",c
        if c * 2 <= size:
            left = self.heap[c*2-1]
            max = c*2-1
            if c * 2  < size:
                right = self.heap[c*2]
                #print "left=",left," right=",right
                if right > left:
                    max = c*2
            #print "min=",min
            if self.heap[max] > self.heap[index]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[max]
                self.heap[max] = tmp
                self._Heap__downheap(max)
        
     

    

            
        
class MinKVHeap():    
          
     
    def __init__(self):
        self.heap = []
    
    def size(self):
        return len(self.heap)
    
    def height(self):
        return floor(log(self.size()))
    
    def printRoot(self):        
        print self.heap[0]
        #output.write(str(self.heap[0])+'\n')
        #pass
    
           
    def printHeap(self):
        print self.heap
    
    def root(self):
        if len(self.heap) == 0:
            return None
        
        return self.heap[0]
    
    def remove_root(self):
        #swap head with last
        n = self.size()
        root = self.heap[0]
        self.heap[0] = self.heap[n-1]   
        self.heap.pop()
        
        self.__downheap(0)
        
        return root
    
    
   
    
            
    def insert(self, key,value):
        #add to end of list
        self.heap.append([key,value])
        
        n = self.size()
        if n == 1:
            return
        
        p = n / 2
        #print "p=",p," heap is ",self.heap," n=",n
        while p != 0 and self.heap[n-1][0] < self.heap[p-1][0]:
            #swap p and n
            tmp = self.heap[p-1]
            self.heap[p-1] = self.heap[n-1]
            self.heap[n-1] = tmp
            
            n = p
            p = p / 2
    
    def __downheap(self, index):
        
        size = self.size()
        
        c = index + 1
       # print "c=",c
        if c * 2 <= size:
            left = self.heap[c*2-1]
            min = c*2-1
            if c * 2  < size:
                right = self.heap[c*2]
                #print "left=",left," right=",right
                if right[0] < left[0]:
                    min = c*2
            #print "min=",min
            if self.heap[min][0] < self.heap[index][0]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[min]
                self.heap[min] = tmp
                self.__downheap(min)
                    
            
        

class WaitLine():
    
    def __init__(self):
        self.minHeap = MinKVHeap()
        self.index = 0
        self.totalWait = long(0)
        self.count = 0

    def printAvg(self):
        print self.totalWait / self.count
        
    def processWaitingTimes(self, times):
        if self.index == 0:            
            self.index = times[0][0]
        
        while times or self.minHeap.size() > 0:
            
            #print "self.index=",self.index
            #print "self.totalWait=",self.totalWait
            while times and times[0][0] <= self.index:
                #get entry
                entry = times.pop(0)
                heapValue = entry[1] - entry[0]
                #print "adding to heap",heapValue
                self.minHeap.insert(entry[1],heapValue)
            
            
            if self.minHeap.size() > 0:
                
                #process one entry
                kv = self.minHeap.remove_root()
                #print "kv=",kv
                wait = self.index +kv[1]
                self.index = kv[0] + self.index
                
                #print "adding to total wait ",wait
                self.totalWait = self.totalWait + wait
                self.count = self.count + 1
                #print "totalWait=",self.totalWait
            else:
                self.index = times[0][0]
            
            
            #print ""    
            
        
        
    
    
    
       
    
class Median():
    def __init__(self):
        self.minHeap = MinHeap() #numbers greater than median
        self.maxHeap = MaxHeap() #numbers less than median
        
    def rebalance(self):
       # self.printMedians()
        if self.minHeap.size() > self.maxHeap.size()+1:
            min = self.minHeap.remove_root()
            self.maxHeap.insert(min)
        elif self.maxHeap.size() > self.minHeap.size()+1:
            max = self.maxHeap.remove_root()
            self.minHeap.insert(max)
        #self.printMedians()
    
    def getMedian(self):
        minSize = self.minHeap.size()
        maxSize = self.maxHeap.size()
        
        if minSize == 0 and maxSize == 0:
            return None
        
        if minSize == maxSize:
            return (float(self.minHeap.root()) + float(self.maxHeap.root())) / 2.0
        elif minSize > maxSize:
            return float(self.minHeap.root())
        else:
            return float(self.maxHeap.root())
           
    def insert(self, value):
        maxRoot = self.maxHeap.root()
        minRoot = self.minHeap.root()
        
        if maxRoot == None:
            self.maxHeap.insert(value)
            #print "inserting into maxHeap", value
            return
        elif minRoot == None:
            
            #swap with maxRoot if value < maxRoot
            if maxRoot > value:
                self.maxHeap.heap[0] = value
                value = maxRoot
                
            self.minHeap.insert(value)
            #print "inserting into minHeap", value
            return
        
                    
        if value > maxRoot:
            #print "inserting into minHeap ", value
            self.minHeap.insert(value)
        else:
            self.maxHeap.insert(value)
            #print "inserting into maxheap ",value
        
        self.rebalance()
    
    def printMedians(self):
        
        self.maxHeap.printHeap()  
        self.minHeap.printHeap()



class Cookies():

    def __init__(self):
        self.queue = MinHeap()

    def findSweetness(self, array, sweetness):
        for x in array:
            self.queue.insert(int(x))

        if len(array) < 2:
            print "-1"
            return

        ops = 0


        min = self.queue.root()

        while min < sweetness:
            self.queue.printHeap()
            min = self.queue.remove_root()
            print 'min=',min
            secondMin = self.queue.remove_root()
            print 'secodnmin =',secondMin

            if secondMin == None:
                print "-1"
                return

            newCookie = (1 * min) + (2 * secondMin)
            ops = ops + 1

            self.queue.insert(newCookie)

            min = self.queue.root()
        print ops

#heap = MinHeap()
#n = int(raw_input())
#for i in xrange(n):
#    tmp = raw_input().strip().split(' ')
    
#    if tmp[0] == '1':
#        heap.insert(int(tmp[1]))
#    elif tmp[0] == '2':
#        heap.remove(int(tmp[1]))
#    else:
#        heap.printRoot()


#median = Median()
#n = int(raw_input().strip())
#a = []
#a_i = 0
#for a_i in xrange(n):
#    a_t = int(raw_input().strip())
#    median.insert(a_t)
#    print median.getMedian()
    #print output.getvalue()
    
    #heap.printHeap()           
#median.printMedians()

#wait = WaitLine()
#n = int(raw_input().strip())
#times = []
#for a_i in xrange(n):
#    tmp = raw_input().strip().split(' ')
#    times.append([long(tmp[0]), long(tmp[1])])

#times.sort()
#print times
#wait.processWaitingTimes(times)
#wait.printAvg()


n,k = raw_input().strip().split(' ')
tmp = raw_input().strip().split(' ')
cookie = Cookies()
cookie.findSweetness(tmp, int(k))