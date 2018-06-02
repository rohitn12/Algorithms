def linearSearch(array , x):
    for i in range(len(array)):
        if(array[i] == x):
            return i
    return -1
linearSearch([1,4,7,12,16] , 12)