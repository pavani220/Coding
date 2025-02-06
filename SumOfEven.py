n=int(input("n value")) #4
sum=0
for i in range(1,n+1): #1,2,3,4
    if i%2==0:
        sum=sum+i
print(sum)
#input:10
#output:2,4,6,8,10