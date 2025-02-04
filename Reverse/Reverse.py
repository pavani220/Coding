#3 ways to reverse a string
#while loop:
n=input("")
res=""
count=len(n)
while count>0:
   res=res+n[count-1]
   count-=1
print(res)
#input:cat
#output:tac


#no loops
'''n="cat"
n=n[::-1]
print(n)'''
#output:tac

