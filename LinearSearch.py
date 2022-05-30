def linearsearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [23, 12, 14, 7, 78, 1, 15]
x = 7
n = len(array)
result = linearsearch(array, n, x)
if (result == -1):
    print("Element not Found in the array")
else:
    print("Elements found in the array at index", result)
    
//
