def selectionSort(array):
    lengthOfArray = len(array)
    for i in range(lengthOfArray):
        for j in range(i+1 , lengthOfArray ):
            if(array[j] < array[i] ):
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
          
    return array
#test

selectionSort([64, 25, 12, 22, 11])
