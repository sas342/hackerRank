"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
 """

 
class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 

def print_list(head):
    if head == None:
        return;
    
    print head.data;
    print_list(head.next);
    
"""
insert node at tail of list
"""
def Insert(head, data):
    if head == None:
        return Node(data) 
    
    n = head
    while (n.next != None):
        n = n.next

    n.next = Node(data)

    return head

def InsertBeginning(head, data):
    return Node(data, head)

#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head,data,position):
    if head == None:
        return Node(data)
    
    if position == 0:
        return Node(data, head)
    
    n = head
    while position > 1:
        n = n.next
        position = position - 1
    
    tmp = n.next
    n.next = Node(data,tmp)
    
    return head

def Delete(head, position):
    if head == None:
        return None
    
    if position == 0:
        return head.next
    
    # get node before delete node
    n = head
    while position > 1:
        n = n.next
        position = position - 1
        
    nodeToDelete = n.next
    if nodeToDelete != None:
        n.next = nodeToDelete.next
    
    return head

def ReversePrint(head):
    l = list()
    
    if l == None:
        return l
    
    l.append(head.data)
    while (head.next != None):
        head = head.next
        l.append(head.data)
    
    while len(l) > 0:
        print (l.pop())    
        

"""
swap next one with head
"""
def Reverse(head):
    n = head
    while (n.next != None):
        tmp = n.next
        n.next = tmp.next
        tmp.next = head
        head = tmp
    
    return head

def length(head):
    if head == None:
        return 0
    
    cnt = 0
    while head != None:
        head = head.next
        cnt = cnt + 1
    
    return cnt

def CompareLists(headA, headB):
    if length(headA) != length(headB):
        return 0
    
    if (length(headA) == 0 and length(headB) ==0):
        return 1
    
    while headA != None:
       
        if headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next
    
    return 1
    
"""
Merge 2 lists
"""  
def MergeLists(headA,headB):
    if (headA == None):
        return headB
    
    elif (headB == None):
        return headA
    
    if (headA.data <= headB.data):        
        n = headA
        headA = headA.next
    else:
        n = headB
        headB = headB.next
    
    n.next = MergeLists(headA, headB)
    return n

"""
start pointer postion places behind first to get nth node from tail
"""
def GetNode(head, position):
    if (head == None):
        return None
    
    
    p2 = head
    n = head
    while n != None:
        #print p2.data
        #print "position = ",position
        n = n.next
        
        
        if (position < 0):
            p2 = p2.next
        
        position = position - 1
    
    return p2.data

"""
delete duplicates in sorted linked list
"""
def RemoveDuplicates(head):
    prev = None
    n = head
    while (n != None):
        if (prev != None and n.data == prev.data):
            prev.next = n.next
        else:
            prev = n
        n = n.next
    
    return head

"""
determine if list has a cycle.  use two pointers, 1 faster than the other
"""
def has_cycle(head):
    
    if head == None:
        return False
    
    p1 = head.next
    p2 = head
    while (p1 != None):
        if p1 == p2:
            return True
        
        p1 = p1.next
        if (p1 != None):
            p1 = p1.next
        p2 = p2.next
    
    return False

"""
find merge point of two lists
"""
def FindMergeNode(headA, headB):
    l1 = length(headA)
    l2 = length(headB)
    
    if l2 > l1:
        diff = l2 -l1
        for x in range(diff):
            headB = headB.next
        
    elif l1 > l2:
        diff = l1 -l2
        for x in range(diff):
            headA = headA.next
    
    while headA != None:
        if headA.data == headB.data:
            return headA.data
        
        headA = headA.next
        headB = headB.next
 
 
           
    
        
        
        
    
    
    
head = InsertNth(None,5,0)
head = InsertNth(head, 3,0)
head = InsertNth(head, 5,1)
head = InsertNth(head, 4,2)
head = InsertNth(head, 2,4)
head = InsertNth(head,10,1)

#print_list(head)  
head = Node(1,Node(2,Node(3,Node(4))))
head2 = Node(1,Node(2,Node(3,Node(4))))

CompareLists(head,head2)
print_list(head)
print_list(head2)

n = MergeLists(head,head2)
print (GetNode(n, 3))
  
  
  
  
