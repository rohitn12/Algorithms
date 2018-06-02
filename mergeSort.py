def mergeSort(array):
    #print("splitting" , array)
    if(len(array) > 1):
        middle = len(array) //2
        leftHalf = array[:middle]
        rightHalf = array[middle:]
        
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        
        i = 0
        j = 0
        k = 0
        while i < len(leftHalf) and j < len(rightHalf) :
            if(leftHalf[i] < rightHalf[j]):
                array[k] = leftHalf[i]
                i += 1
            else:
                array[k] = rightHalf[j]
                j += 1
            k += 1
        
        while i < len(leftHalf):
            array[k]  = leftHalf[i]
            i += 1
            k += 1
        
        while(j < len(rightHalf)):
            array[k] = rightHalf[j]
            j += 1
            k += 1
   # print("merging" , array)
mergeSort([7,6,9,1,5])
