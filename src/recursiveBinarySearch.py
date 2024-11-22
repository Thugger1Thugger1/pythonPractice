def binarySearch(list, low, high, value):
    mid = (low + high) // 2
    if low <= high:
        if value < list[mid]:
            return binarySearch(list, low, mid - 1, value)
        elif value > list[mid]:
            return binarySearch(list, mid + 1, high, value)
        else:
            return mid

print(binarySearch([1,2,3,4,5,6,7,8,9,10], 0, 9, 8))