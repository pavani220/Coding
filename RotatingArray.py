# Step 1: Input array and k value
arr = input("Enter elements of the array separated by space: ").split()
arr = [int(x) for x in arr]  # Convert the array elements to integers

k = int(input("Enter number of positions to rotate: "))

# Step 2: Calculate the effective rotation value
k = k % len(arr)  # To handle cases when k is greater than the length of the array

# Step 3: Rotate the array
# - The last 'k' elements should come to the front
# - The first 'len(arr) - k' elements should follow the last 'k' elements
rotated_arr = arr[-k:] + arr[:-k]

# Step 4: Output the rotated array
print("Rotated array:", rotated_arr)
