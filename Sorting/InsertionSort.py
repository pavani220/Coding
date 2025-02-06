def insertion(arr):
    n=0
    for _ in arr:
        n+=1
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
            
arr=[4,1,7,2]
insertion(arr)
print(arr)