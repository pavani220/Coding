#Reversing an string using indexing
#a="sky is blue"
#b=a.split()
#b=b[::-1]
#list=" ".join(b)
#print(list)
#output: blue is sky

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

