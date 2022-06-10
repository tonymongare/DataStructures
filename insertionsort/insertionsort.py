def insertionsort(array):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            array[j + 1] = key
array = [2, -4, -6, 2, 1, 10]
insertionsort(array)
print(array)