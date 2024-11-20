def binarySearch(arr, low, high, x):
    mid = (low + high) // 2
    if low <= high:
        if arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        if arr[mid] < x:
            return binarySearch(arr, mid + 1, high, x)
        else:
            return mid

    else:
        return -1

print(binarySearch([1,2,3,4,5,6,7,8,9,10], 0, 9, 3))