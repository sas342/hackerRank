class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node
       
"""
insert a node into doubly linked list, keeping sorted order
"""
def SortedInsert(head, data):
    n = head
    while n != None:
        
        if n.next != None and n.next.data > data:
            tmp = n.next
            n.next = Node(data, tmp,n)
            return head
        elif n.next == None:
            n.next = Node(data,None,n)
            return head
        
        n = n.next
    
    return head   

"""
swap next one with head
"""
def Reverse(head):
    n = head
    while (n.next != None):
        tmp = n.next
        n.next = tmp.next
        if (n.next != None):
            n.next.prev = n
        tmp.prev = None
        tmp.next = head
        head.prev = tmp
        head = tmp
    
    return head