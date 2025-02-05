n=153
temp=n
sum=0
s=len(str(n))
for i in str(n):
    sum+=int(i)**s
if sum==temp:
    print("Armstrong")
else:
    print("not")