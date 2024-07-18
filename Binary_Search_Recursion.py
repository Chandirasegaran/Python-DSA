def binary_search(low, high, target, array):
    if low > high:
        return "Not Found"
    mid = (low + high)//2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(low, mid-1, target, array)
    else:
        return binary_search(mid + 1, high, target, array)


for i in range(1,11):
    res=binary_search(0, 9, i, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


    print("index ",res)