def binary_search(array, x, low, high):

    if high >= low:
        mid = low + (high + low)//2

        if array[mid] == x:
            return mid

        elif array[mid] > x:
            return binary_search(array, x, low, (mid + 1))

        else:
            return binar_search(array, x,high, (mid - 1))

    else:
        return -1


array = [12, 23, 45, 60, 99]
x = 23
result = binary_search(array, x, 0, len(array)-1)

if result != -1:
    print("Element present at index number", result)
else:
    print("Element not found in the array")

#end
