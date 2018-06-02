
def interpolationSearch(array ,x):
    low  = 0 
    high = len(array) -1
    while(low <= high and array[low] <= x and x <= array[high]):
        max = array[high]
        min = array[low]
        distanceFromxToMin = x - min
        distanceFromMaxtoMin = max - min
        fraction = distanceFromxToMin // distanceFromMaxtoMin
        indexRange = high - low
        estimatedIndex = low + round(fraction * indexRange)
        if(array[estimatedIndex] == x):
            return estimatedIndex
        elif(array[estimatedIndex] > x):
            high = estimatedIndex - 1
        else:
            low = estimatedIndex + 1
    return -1

interpolationSearch( [10, 12, 13, 16, 18, 19, 20, 21,22, 23, 24, 33, 35, 42, 47] , 47)