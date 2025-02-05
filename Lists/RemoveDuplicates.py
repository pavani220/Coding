a=[1,2,2,4,4,5]
res=[]
for i in a:
    if i not in res:
        res.append(i)
print(res)
'''my_list = [1, 2, 3, 4, 5, 2, 3, 6]
unique_list = list(set(my_list))
print("List after removing duplicates:", unique_list)
'''

'''my_list = [1, 2, 3, 4, 5, 2, 3, 6]
unique_list = list(dict.fromkeys(my_list))
print("List after removing duplicates:", unique_list)
'''