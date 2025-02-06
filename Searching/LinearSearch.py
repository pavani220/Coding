def search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[1,2,9,3,5,7]
target=5
res=search(arr,target)
print(res)

# returns the index of the array

'''def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Return -1 if not found

# Example usage
arr = [5, 3, 8, 1, 2]
target = 8
result = linear_search(arr, target)
print(f"Element found at index: {result}")
'''