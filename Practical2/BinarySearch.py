def binary_search(arr, n,target):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
n=len(arr)
result = binary_search(arr,n, target)
print(result)