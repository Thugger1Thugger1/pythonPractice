def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1 
        else:
            return mid
    return -1

print(binarySearch([1,2,3,4,5,6,7,8,9,10], 6))