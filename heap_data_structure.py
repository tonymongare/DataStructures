def heapify(array, n, i):
    
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and array[i] < l:
        largest = l
        
    if r < n and array[i] < r:
        largest = r
        
  
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        
        heapify(array, n, largest)
        
def insert(array, newNum):
    
    size = len(array)
    
    if size == 0:
        array.append(newNum)
        
    else:
        array.append(newNum)
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)
            
def delete(array, num):
    size = len(array)
    
    i = 0
    
    for i in range(0, size):
        if array[i] == num:
            break
    array[i], array[size - 1] = array[size - 1], array[i]
    
    array.remove(num)
    
    for i in range((size//2)-1, -1, -1):
        heapify(array, size, i)
        
array = []

insert(array, 99)
insert(array, 98)
insert(array, 97)
insert(array, 96)
insert(array, 95)

print(str(array))

#en
    
    
            
        
