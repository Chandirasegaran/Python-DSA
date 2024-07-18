def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "Not Found"

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 11
    print(binary_search(arr, target))
