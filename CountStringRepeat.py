#input1: cat batman cat latt latt cat
#input2:3
#output:cat

a=input("enter string")
b=int(input())
a=a.split()
d=dict()
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''output:
enter stringcat cat cat mat
3
{'cat': 3, 'mat': 1}'''