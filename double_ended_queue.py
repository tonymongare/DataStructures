class Deque:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def addRear(self, item):
        return self.items.append(item)
        
    def addFront(self, item):
        return self.items.insert(0, item)
        
    def removeFront(self):
        return self.items.pop(0)
        
    def removeRear(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)
        
                
class Deque:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def addRear(self, item):
        return self.items.append(item
        
    def addFront(self, item):
        self.items.insert(0, item)
        
    def removeRear(self):
        return self.items.pop()
    def removeFront(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
        
q = Deque()

q.addRear(12)
q.addRear(13)
q.addFront(14)
q.addFront(15)

print(q)
print(q.size())
