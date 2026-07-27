def linearsearch(arr,n,key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1
arr=[12,78,-90,23,67,54]
n=len(arr)
key=-90
ans=linearsearch(arr,n,key)
print(ans)