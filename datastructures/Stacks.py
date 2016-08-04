'''
Created on Jun 11, 2016

@author: sstimmel
'''

class BalancedParen():
    
    def __init__(self):
        self.balanced = True
        self.stack1 = []
    
    def nextchar(self, char):
        if self.balanced == False:
            return
        
        if char == '{' or char == '[' or char == '(':
            self.stack1.append(char)
       
        elif char == '}' or char == ']' or char == ')':
            try:
                d = self.stack1.pop()
                if char == '}' and d != '{':
                    self.balanced = False
                elif char == ']' and d != '[':
                    self.balanced = False
                elif char == ')' and d != '(':
                    self.balanced = False
                    
            except:
                self.balanced = False
        
        
    
    def isBalanced(self):
        if not self.balanced:
            print "NO"
            return
        
        if len(self.stack1) == 0:
            print "YES"
            return
        
        print "NO"
        
class MaxStack():
    maxStack = []
    allStack = []
    
    def push(self, number):
        self.allStack.append(number)
        
        size = len(self.maxStack)
        if size == 0:
            self.maxStack.append(number)
            
        elif self.maxStack[size-1] <= number:
            self.maxStack.append(number)
    
    
    def delete(self):
        num = self.allStack.pop()       
        
        size = len(self.maxStack)
       
        if self.maxStack[size-1] == num:
            self.maxStack.pop()
    
    def printMax(self):
        size = len(self.maxStack)
        
        print self.maxStack[size-1]

class MaxRectangle():
    
    def __init__(self):
        self.stack = []
        self.max = 0
    
    def insert(self, number, index):
        #if num < top, keep popping until <=
        #calculate size for popped entries and store max if needed
        currentSize = len(self.stack)
        
        lastStart = None
        while currentSize > 0 and self.stack[currentSize-1].val > number:            
            r = self.stack.pop()
            print "popping of ",r.val, "at start",r.start
            m = r.val * (index - r.start)
            lastStart = r.start
            if m > self.max:
                self.max = m
                print "new max is ",self.max
            currentSize = currentSize - 1
        
        if lastStart != None:
            r = Rect(number, lastStart)
            self.stack.append(r)
            
        
        if lastStart == None and (currentSize == 0 or self.stack[currentSize-1].val < number):
            r = Rect(number, index)
            self.stack.append(r)
            print "adding ",r.val

    def getMax(self, index):
        while len(self.stack) > 0:
            try:
                r = self.stack.pop()
                possibleMax = r.val * (index - r.start)
                print "computing ",r.val, "start = ",r.start," end is ",index
                if possibleMax > self.max:
                    self.max = possibleMax
            
            except:
                pass
        return self.max
    
class Rect():
    
    def __init__(self, val, start):
        self.val = val
        self.start = start

class TextEditor():
    
    def __init__(self):
        self.operations = []
        self.w = ""
        
    
    def add(self, value):
        self.w = self.w + value
    
    def delete(self, number):
        self.w = self.w[0:len(self.w)-int(number)]
    
    def printKth(self, k):
        print self.w[int(k)-1]
    
    def undo(self):
        op = self.operations.pop()
        self.performCalc(op, False)
       # print self.w
        
    def performCalc(self, operation, add=True):
        tmp = operation.strip().split(' ')
        action = tmp[0]
        if action != '4':
            val = tmp[1]
        
        if add and (action == '1' or action == '2'):
            if action == '1':
                l = len(val)
                self.operations.append('2 '+str(l))
            elif action == '2':
                x = self.w[len(self.w)-int(val):]
                self.operations.append('1 '+x)
                
        if action == '1':
            self.add(val)
        elif action == '2':
            self.delete(val)
        elif action == '3':
            self.printKth(val)
        elif action == '4':
            self.undo()

class Poison():
    
    def __init__(self):
        self.stack = []
    
    def findMaxNumberOfDays(self, array):
        maxN = 0
        for i in array:
            iv = int(i)
            
            daysAlive = 0
            if len(self.stack) == 0:
                self.stack.append([iv, daysAlive])
            
            #print "current is ",iv
            print self.stack
            
            while len(self.stack) > 0 and iv <= self.stack[len(self.stack)-1][0]:
                daysAlive = max(daysAlive, self.stack.pop()[1])
            
            #if stack is empty, set days alive to 0
            if len(self.stack) == 0:
                daysAlive = 0
            else:
                daysAlive = daysAlive + 1
            
            #print "days alive ",daysAlive
            
            maxN = max(maxN, daysAlive)
            self.stack.append([iv, daysAlive])
        
        return maxN
            
            
        
        
        
        
#maxstack = MaxStack()
#N = input()
# for i in range(0, N):
#     tmp = raw_input().strip().split(' ')
#     if int(tmp[0]) == 1:
#         maxstack.push(int(tmp[1]))
#     elif int(tmp[0]) == 2:
#         maxstack.delete()
#     else:
#         maxstack.printMax()

#N = input()

# for i in range(0, N):
#     p = BalancedParen()
#     tmp = raw_input()
#     for c in tmp:
#         p.nextchar(c)
#     
#     p.isBalanced()

#rect
# n = input()
# tmp = raw_input().strip().split(' ')
# i=1
# maxR = MaxRectangle()
# for h in tmp:
#     maxR.insert(int(h), i)
#     i = i+1
# print maxR.getMax(i)
#    
 
# n = input()
# t = TextEditor()
# for x in xrange(n):
#     i = raw_input().strip()
#     t.performCalc(i)

n = input()
p = Poison()
tmp = raw_input().strip().split(' ')
print p.findMaxNumberOfDays(tmp)
