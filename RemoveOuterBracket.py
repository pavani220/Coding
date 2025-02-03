#remove outer bracket example:
# a="(()())(())"
#output:()()()
a=input("enter a string")
j=0
res=" "
for char in a:
    if char==')':
        j=j-1
    if j>0:
        res= res+char
    if char=='(':
        j=j+1
print(res)
