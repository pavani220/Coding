#Merging the two lists using 2 ways
#1.a=[1,2,3]
#b=[4,5,6]
#c=a+b
#print(c)
#output:[1,2,3,4,5,6]

#2.zip(a, b) pairs corresponding elements from a and b into tuples.
#a=[1,2,3]
#b=[4,5,6]
#c=list(zip(a,b))
#print(c)
#output:[(1,4),(2,5),(3,6)]

a = [1, 2, 3]
b = [4, 5, 6]

c = list(zip([a, b]))  # Transpose the lists
print(c)