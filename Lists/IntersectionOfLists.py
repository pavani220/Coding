a=[1,2,3]
b=[1,2,6]
c=list(set(a)&set(b))
print(c)

'''[value for value in list1 if value in list2]'''
'''list(filter(lambda x:x in list2,list1))'''