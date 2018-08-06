def kadane(array):
    max_current = max_global = array[0]
    for i in range(len(array)):
        max_current = max(max_current + array[i] , array[i])
        if max_current > max_global:
            max_global = max_current
    return max_global