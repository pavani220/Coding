a=[1,2,2,3,1,4,3]
b=[]
for i in a:
    if a.count(i)>1:
        b.append(i)
print(b)