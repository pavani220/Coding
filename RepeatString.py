n=input(" ")
count=int(input(""))
n=n.split()
d=dict()
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
res=[]
for key in d:
    if d[key]==count:
        res.append(key)
print(res)
    
#output: cat mat cat cat 
# 3
# ['cat']