class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        
        self.head = None
        
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        
        new_node.next = self.head
        self.head = new_node
        
    def insertAfter(self, prev_nde, new_data):
        
        if prev_node is None:
            print("prev_node should be in the linked_list")
            return
        
        new_node = Node(new_data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def insertAtEnd(self, new_data):
         new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next
            
        last.next = new_node
        
        
class Node:
    
    def __(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insertAtBegginning(self, new_data):
        
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
        
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("Must be in the Linkedlist")
            return
    
        new_node = Node(new_data)
    
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return 
        
        
        last = self.head
        while(last.next):
            last = last.next
            
        last.next = new_node
        
        
        
        
    
    
        
        
        
