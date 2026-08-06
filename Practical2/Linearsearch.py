def linearsearch(arr,n,key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1
arr = [2, 3, 4, 10, 40]
n = len(arr)
key = 10
result = linearsearch(arr, n, key)
print(result)