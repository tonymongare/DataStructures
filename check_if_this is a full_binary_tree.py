class Node:
    
    def __init__(self, item):
        self.leftNode = None
        self.rightNode = None
        self.item = item
        
def isFull(root):
    
    if root is None:
        return True
        
    if root.leftNode is None and root.rightNode is None:
        return True
        
    if root.leftNode is not None and root.rightNode is not None:
        return(isFull(root.leftNode) and isFull(root.rightNode))
    return False
    
root = Node(1)
