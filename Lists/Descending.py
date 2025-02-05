'''my_list = [5, 2, 9, 1, 5, 6]
my_list.sort(reverse=True)  # Sorts the list in place in descending order
print("Sorted list (descending):", my_list)'''

'''list=[5,2,4,1,2]
list.sort(reverse=True)
print(list)'''

#By length
list = ['apple', 'banana', 'cherry', 'date']
sorted_list = sorted(list, key=len, reverse=True)  # Sort by length in descending order
print(sorted_list)
