def bubble_sort(arr):
    n=0
    for _ in arr:
        n=n+1
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
arr=[1,2,3,7,4]
bubble_sort(arr)
print(arr)

'''def bubble_sort(arr):
    n = 0
    for _ in arr:  # Counting elements manually
        n += 1

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # Swap
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

# Example usage
arr = [5, 3, 8, 1, 2]
bubble_sort(arr)
print("Bubble Sorted:", arr)
'''