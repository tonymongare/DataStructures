class Node:
    
    def __init__(self, item):
        self.right = None
        self.left = None
        self.data = item
        
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end="")
        
        if self.right:
            self.righ.iorder()
            
    def preorder(self):
        print(self.data, end="")
        if self.left:
            self.left.preorder();
        if self.right:
                self.right.preorder()
                
    def postorder(self):
        if self.left:
            self.left.postorder
        if self.right:
            self.right.postorder
        print(self.data, end="")
        
root = Node(23)
root.left = Node(24)
root.right = Node(25)
root.left.left = Node(4)
root.left.right = Node(5)


//
                
