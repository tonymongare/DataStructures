def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        
        mergeSort(L)
        mergeSort(M)
        
        i = j = k = 0
        
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
                
            k += 1
            
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
            
def printSortedArray(array):
    for i in range(len(array)):
        print(array[i], end=",")
    print()
    
if __name__ == '__main__':
    array = [8, 45, 2, 77, 1, 23]
    mergeSort(array)
    
    printSortedArray(array)
    
