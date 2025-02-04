#reverse of each elements within a word
a=input("")
a=a.split()
res=[]
for i in a:
    b=i[::-1]
    res.append(b)
res=" ".join(res)
print(res) 
#output:man is tall
        #nam si llat