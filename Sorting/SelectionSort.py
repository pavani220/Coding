def selection(arr):
    n=0
    for _ in arr:
        n+=1
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        temp=arr[i]
        arr[i]=arr[min_index]
        arr[min_index]=temp
arr=[1,4,2,9,1]
selection(arr)
print(arr)
'''def selection_sort(arr):
    n = 0
    for _ in arr:  # Counting elements manually
        n += 1

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Find min element
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp  # Swap

# Example usage
arr = [5, 3, 8, 1, 2]
selection_sort(arr)
print("Selection Sorted:", arr)
'''