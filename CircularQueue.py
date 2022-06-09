class CircularQueue:
    
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
        
    def enqueue(self, item):
        if((self.rear + 1) % (self.size) == self.front):
            print("The queue is full")
        #if the circular queue is empty
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] == item
        #if queue is not empty  
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] == item
            
    def dequeue(self):
        if(self.front == -1):
            print("The queue is empty")
            
        elif (self.rear == self.front):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
            
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
            
    def display(self):
        if(self.front == -1):
            print("Queue is empty")
            
        elif (self.front >= self.rear+1):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end="")
            for i in range(0, self.size + 1):
                print(self.queue[i], end = " ")
            print()
            
q = CircularQueue(2)

q.enqueue(12)
q.enqueue(13)

q.display()
 

//////
