#using for loop
a="hello"
a=a.split()
res=[]
for i in a:
    b=i[::-1]
    res.append(b)
res=" ".join(res)
print(res) 

#output:olleh

