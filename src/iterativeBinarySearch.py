def binarySearch(list, value):
    low = 0
    high = len(list) - 1
    mid = high // 2

    while low <= high:
        mid = (low + high) // 2
        if value < list[mid]:
            high = mid - 1
        elif value > list[mid]:
            low = mid + 1
        else:
            return mid

print(binarySearch([1,2,3,4,5,6,7,8,9,10], 6))