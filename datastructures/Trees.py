
class Node(object):
    def __init__(self, data=None, left=None, right=None):
       self.data = data
       self.left = left
       self.right = right
    
    
def preOrder(root):
    if root == None:
        return
    
    print root.data,
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root == None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print root.data,

def inOrder(root):
    if root == None:
        return
    
    inOrder(root.left)
    print root.data,
    inOrder(root.right)
    

def swapNodes():
    None

n = int(raw_input())