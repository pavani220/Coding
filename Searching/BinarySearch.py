def search(arr,target):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            low=mid-1
    return -1
arr=[1,2,5,2,9]
target=5
s=search(arr,target)
print(s)
    