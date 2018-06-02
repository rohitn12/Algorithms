
def mergeSort(array):
    if (len(array) > 1):
        middle = len(array)//2
        leftHalf = mergeSort(array[:middle])
        rightHalf = mergeSort(array[middle:])
        return merge(leftHalf , rightHalf)
    else:
        return array

def merge(left , right):
    sortedArray = []
    i, j = 0,0
    while (i < len(left)) and (j < len(right)):
        if (left[i] < right[i]):
            sortedArray.append(left[i])
            i += 1
        else:
            sortedArray.append(right[j])
            j += 1
    sortedArray += left[i:]
    sortedArray += right[j:]
    return sortedArray

array = [int(x) for x in input().split()]
print(mergeSort(array))