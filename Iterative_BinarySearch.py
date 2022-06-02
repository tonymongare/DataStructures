def binary_search(array, x, low, high):
    while low < high:

        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


array = [12, 15, 17, 24, 56, 89, 90]
x = 24
result = binary_search(array, x, 0, len(array)-1)

if result != -1:
    print("Element found at index", str(result))
else:
    print("Element not found in the array")



//
