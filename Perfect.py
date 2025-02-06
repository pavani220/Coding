n=int(input("enter value"))
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum+=i
if sum==n:
    print("yes")
else:
    print("no")