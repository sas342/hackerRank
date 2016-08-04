#!/bin/python



class Node():
    
    
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.ht = 0
        self.freq = 1
        self.leftCnt = 0
        self.rightCnt = 0

class AvlTree():
    
    
    def __init__(self):
        self.root = None

    def size(self):
        if self.root == None:
            return 0
        
        return self.root.leftCnt + self.root.rightCnt + 1 + self.root.freq
    
    
    def search(self, val):
        return self.__searchInner(self.root, val)
        
    def __searchInner(self, node, val):
        if node == None:
            return
         
         
        if node.val == val:
            return node
        lv = self.__searchInner(node.left, val)
        if lv != None:
            return lv
         
        return self.__searchInner(node.right, val)
    
    def findPath(self, val):
        stack = []
        self.__findPath(self.root, val, stack)
        
        return stack
        
        
   
    def __findPath(self, node, val, stack):
        if node == None:
            return
        
        #add self
        stack.append(node)
                
       
        if node.val == val:            
            return node
        
        lv = self.__findPath(node.left, val, stack)
        if lv != None:
            return node
        rv = self.__findPath(node.right,val, stack)
        if rv != None:
            return node
        else:
            stack.pop() #remove this node
           

    def getCount(self, node):
        if node == None:
            return 0
        
        return node.leftCnt + node.rightCnt + node.freq
    
    
    def insert(self, val):
        
                
        newNode = Node(val)
        
        if self.root == None:
            self.root = newNode
            return self.root
        
        stack = []
        self.__insertCore(newNode,self.root,stack)
        
        lowestUnbalanced = self.findLowestUnbalancedNode(stack)
        while lowestUnbalanced != None:
            balancedRoot = self.balance(self.root, lowestUnbalanced)
            
            if self.root == lowestUnbalanced:
                self.root = balancedRoot
            
            lowestUnbalanced = self.findLowestUnbalancedNode(stack)
        
        return self.root

    def numberOfChilden(self, node):
        if node == None:
            return 0
        
        cnt = 0
        if node.left != None:
            cnt = cnt + 1
        if node.right != None:
            cnt = cnt + 1
            
        return cnt
            
    def delete(self, val):
        
       
        pathStack = self.findPath(val)
       
        if len(pathStack) == 0:
            return -1
        
        nodeToDelete = pathStack.pop()     
        
        if nodeToDelete.freq > 1:
            nodeToDelete.freq = nodeToDelete.freq - 1
            #update heights
            try:
                p = nodeToDelete
                while p != None:
                    p = pathStack.pop()
                    p.ht = p.ht - 1
            except:
                pass
            return nodeToDelete
        
        p = None   
        try:
            p = pathStack.pop()
            #add it back
            pathStack.append(p)
        except:
            pass
        
        
        #add node to delete back
        pathStack.append(nodeToDelete)
        
        numChildren = self.numberOfChilden(nodeToDelete)
        
        if numChildren == 2:
            s = self.successor(nodeToDelete)
            #print("successor is ",s.val)
            sp = self.parent(self.root, s)
            nodeToDelete.val = s.val
            
            #successor parent is node to delete
            if sp == nodeToDelete:
                sp.right = None
            else:                       
                sp.left = None
                    
            
        if numChildren == 0 or numChildren == 1:
            if nodeToDelete.left != None:
                nodeToDelete.val = nodeToDelete.left.val
            elif nodeToDelete.right != None:
                nodeToDelete.val = nodeToDelete.right.val
            
            nodeToDelete.left = None
            nodeToDelete.right = None
            nodeToDelete.leftCnt = 0
            nodeToDelete.rightCnt = 0
        
        if numChildren == 0 and p != None:
            if p.left == nodeToDelete:
                p.left = None
                p.leftCnt = 0
            elif p.right == nodeToDelete:
                p.right = None
                p.rightCnt = 0
        
        if numChildren == 0 and p == None:
            self.root = None
            return nodeToDelete
        
        
        #start moving up the tree and balancing all
        lowestUnbalanced = self.findLowestUnbalancedNode(pathStack)
        while lowestUnbalanced != None:
            balancedRoot = self.balance(self.root, lowestUnbalanced)
            
            if self.root == lowestUnbalanced:
                self.root = balancedRoot
            
            lowestUnbalanced = self.findLowestUnbalancedNode(pathStack)
        
        #self.calculateNumberOfChildren(self.root)
            
                
    # assuming right subtree exists 
    def successor(self, x):
        if x.right != None:
            y = x.right
            while y.left != None:
                y = y.left
            return y
        
    def balance(self, root, lowestUnbalanced):
        if lowestUnbalanced == None:
            return root
        
        p = self.parent(root, lowestUnbalanced)
        left = False
        if p != None:
            if p.left == lowestUnbalanced:
                left = True
        
        bf = self.balanceFactor(lowestUnbalanced)
        nodeToReturn = p
        
        if bf > 1:
            
            lbf = self.balanceFactor(lowestUnbalanced.left)
            newRoot = None
            
            if lbf >= 0:
                newRoot = self.rightRotate(lowestUnbalanced)
            else:
                newRoot = self.leftRotate(lowestUnbalanced.left)
                lowestUnbalanced.left = newRoot
                newRoot = self.rightRotate(lowestUnbalanced)
            
            if p != None:
                if left:
                    p.left = newRoot
                else:
                    p.right = newRoot
            else:
                nodeToReturn = newRoot
        
        elif bf < -1:
            
            rbf = self.balanceFactor(lowestUnbalanced.right)
            newRoot = None
            
            if rbf >= 1:
                newRoot = self.rightRotate(lowestUnbalanced.right)
                lowestUnbalanced.right = newRoot
                newRoot = self.leftRotate(lowestUnbalanced)
            
            else:
                newRoot = self.leftRotate(lowestUnbalanced)
            
            if p != None:
                if left:
                    p.left = newRoot
                else:
                    p.right = newRoot
            else:
                nodeToReturn = newRoot
        
        #self.height(nodeToReturn)
        #self.calculateNumberOfChildren(nodeToReturn)
        return nodeToReturn

    def leftRotate(self, root):
        x = root
        z = x.right
        
        b = z.left
        z.left = x
        x.right = b
        
        #update heights
        bht = 0
        if b != None:
            bht = b.ht
        lt = 0
        if x.left != None:
            lt = x.left.ht
        if lt == 0 and bht == 0:
            x.ht = 0
        else:
            x.ht = max(bht, lt) + 1
        
        rt = 0
        if z.right != None:
            rt = z.right.ht
        
        z.ht = max(rt, x.ht) + 1
        
        #update counts
        x.leftCnt = self.getCount(x.left)
        x.rightCnt = self.getCount(x.right)
        z.leftCnt = self.getCount(z.left)
        z.rightCnt = self.getCount(z.right)        
        
        
        return z

    def rightRotate(self, root):
        x = root
        y = x.left
        
        c = y.right
        y.right = x
        x.left = c
        
        #update counts
        
        if x != None:
            x.leftCnt = self.getCount(c)
        
        if y != None:
            y.rightCnt = self.getCount(x)
               
        
        #update height
        lt = 0
        if c != None:
            lt = c.ht
        rt = 0
        if x.right != None:
            rt = x.right.ht   
        if lt == 0 and rt == 0:
            x.ht = 0
        else:  
            x.ht = max(lt, rt) + 1
        
        lt =0
        rt = 0
        if y.left != None:
            lt = y.left.ht
        y.ht = max(lt, y.right.ht) + 1
        
        x.leftCnt = self.getCount(x.left)
        x.rightCnt = self.getCount(x.right)
        y.leftCnt = self.getCount(y.left)
        y.rightCnt = self.getCount(y.right)  
        
        return y
    
   
    def findLowestUnbalancedNode(self, stack):
        n = None
        try:
            n = stack.pop()
            
            while n  != None:
               
                bf = self.balanceFactor(n)
                if bf < -1 or bf > 1:
                    return n
                n = stack.pop()
        except:
            n = None
        
        return n

    def parent(self, node, child):
        if node == None:
            return None
        
        if node.left == child or node.right == child:
            return node
        
        p = self.parent(node.left, child)
        if p == None:
            p = self.parent(node.right, child)
        
        return p
    
    def __insertCore(self, newNode, currentNode, stack):
        stack.append(currentNode)
        
        if currentNode.val == newNode.val:
            currentNode.freq = currentNode.freq + 1
            return
        
        if currentNode.val <= newNode.val:
            
            if currentNode.right == None:
                currentNode.right = newNode
                currentNode.rightCnt = 1
                
            else:
                self.__insertCore(newNode, currentNode.right, stack)
                currentNode.rightCnt = self.getCount(currentNode.right)
        
        elif currentNode.val > newNode.val:
            if currentNode.left == None:
                currentNode.left = newNode
                currentNode.leftCnt = 1
            else:
                self.__insertCore(newNode, currentNode.left, stack)
                currentNode.leftCnt = self.getCount(currentNode.left)
        
        self.height(currentNode)
            
    
    def height(self, node):
        if node == None:
            return -1
       
        lt = 0
        rt = 0
        
        if node.left == None and node.right == None:
            node.ht = 0
            return 0
        
        if node.left != None:
            lt = node.left.ht
        
        if node.right != None:
            rt = node.right.ht
        
        
        ht = max(lt,rt) + 1
        node.ht = ht
        return ht
    
    def calcHeight(self, node):
        if node == None:
            return -1
        
        if node.left == None and node.right == None:
            node.ht = 0
            return 0
        
        ht = max(self.height(node.left), self.height(node.right)) + 1
        node.ht = ht
        return ht

    def balanceFactor(self, node):
        
        lh = -1
        rh = -1
        if node.left != None:
            lh = node.left.ht
        
        if node.right != None:
            rh = node.right.ht
        
        #lh = self.height(node.left);
        #rh = self.height(node.right);
        node.ht = max(lh,rh)+1
        
        lc = self.getCount(node.left)
        rc = self.getCount(node.right)
        self.calculateNumberOfChildren(node)
        
        if lc != node.leftCnt:
            SystemExit
        if rc != node.rightCnt:
            SystemExit
        node.leftCnt = self.getCount(node.left)
        node.rightCnt = self.getCount(node.right)
            
        return lh - rh;

    #calculates all nodes counts node and under
    def calculateNumberOfChildren(self, node):
        if node == None:
            return 0
        #print "calculatenUmberOfChildren for ",node.val
        lc = 0
        rc = 0
        if node.left != None:
            lc = self.calculateNumberOfChildren(node.left)
        if node.right != None:
            rc = self.calculateNumberOfChildren(node.right)
        
        node.leftCnt = lc
        node.rightCnt = rc
       # print node.val," has count left=",lc,",rc=",rc," freq",node.freq
        return lc + rc + node.freq
        
    def printNode(self):
        self.__printNode(self.root)
        
    def __printNode(self, root):
        if root == None:
            return
        bf = None
        #bf = self.balanceFactor(root)
        rf = "null"
        if root.right != None:
            rf = root.right.val
        lf = "null"
        if root.left != None:
            lf = root.left.val
        
        print("current : ",root.val," ht=",root.ht," bf=",bf, " left: ",lf," right: ",rf, " leftCount: ",root.leftCnt," rightCount: ",root.rightCnt," freq: ",root.freq)
        self.__printNode(root.left)
        self.__printNode(root.right)
    


    
def median(actions,values):
    avlTree = AvlTree()
    for i in xrange(len(actions)):
        
        action = actions[i]
        value = values[i]
        #print action," ", value
        if action == 'a':
            avlTree.insert(value)
        elif action == 'r':
            rv = avlTree.delete(value)
            if rv == -1:
                print "Wrong!"
                continue
        
                           
        avlTree.printNode()
        print "\n\n\n"
        #print avlTree.size()
        printMedian(avlTree)    

def findAndPrintMedian(root, pathStack, median, isEven):
    if root == None:
        print "ERROR"
        for i in pathStack:
            print i.val
            
    lc = root.leftCnt
    rc = root.rightCnt
    #print "finding median",median," and isEven=",isEven
    pathStack.append(root)
    
    if lc >= median:
        findAndPrintMedian(root.left, pathStack, median, isEven)
        return
    
    median = median - lc
    if root.freq - median >= 0:
        if isEven:
            #look for right node, if not then need to use parent
            secondVal = findNextMax(root, pathStack).val
            #print "next max = ",secondVal
            med = (root.val + secondVal) / 2.0
            if med.is_integer():
                print int(med)
            else:
                print med
           
            
        else:
            print root.val 
        return
    else:
        findAndPrintMedian(root.right, pathStack, median - root.freq, isEven)
        
   
    
    
def findNextMax(node, pathStack):
    #print "find next max of ",node.val
    if node.right != None:
        n = node.right
        while n.left != None:
            n = n.left
        
        return n
    else:
        try:
            n = pathStack.pop()
            while n.val <= node.val:
                n = pathStack.pop()
            return n
        except:
            pass
         
        
def printMedian(avlTree):
    size = avlTree.getCount(avlTree.root)
    
    #print "tree size is ",size
    if size == 0:
        print "Wrong!"
        return
        
    elif size == 1:
        print avlTree.root.val
        return
    
    if size % 2 == 1:
        median = size / 2
        findAndPrintMedian(avlTree.root, [],median+1, False) #nth node
    
    else:
        median = size / 2
        findAndPrintMedian(avlTree.root, [], median, True) #nth node
    
                
       
        


N = input()
s = []
x = []
for i in range(0, N):
    tmp = raw_input().strip().split(' ')
    s.append(tmp[0])
    x.append(int(tmp[1]))
    
median(s,x)


    
#median(s,x)
