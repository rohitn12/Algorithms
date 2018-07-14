def binarySearch(array , X, first , last ):
    if(first <= last):
        midPoint = (first + last)//2
        if(array[midPoint] == X):
            return midPoint
        elif(array[midPoint] > X):
            return binarySearch(array ,X , 0 , (midPoint-1))
        else:
            return binarySearch(array , X , (midPoint+1) , last )
    else:
        return -1

def search(self, nums, target):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif (nums[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
    return -1

#test         
binarySearch([ 2, 3, 4, 10, 40 ] , 10 , 0 ,4 )