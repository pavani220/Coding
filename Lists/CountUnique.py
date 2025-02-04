a=[1,2,2,3,4,4,4,5]
res=[]
for i in a:
    if a.count(i)==1:
        res.append(i)
print(res)