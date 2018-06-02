def bubbleSort(array):
    swap = 0
    for i in range(0 ,len(array) - 1):
        for j in range(i + 1 , len(array) ):
            if (array[i] > array[j]):
                swap += 1
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array , swap
size = int(input())
array = [int(x) for x in input().split()]
returnedValue = bubbleSort(array)
print("Array is sorted in",returnedValue[1] ,"swaps.")
print("Sorted Array" , returnedValue[0])