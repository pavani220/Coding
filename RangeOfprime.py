'''start=int(input("enter value"))
end=int(input("enter value"))

for num in range(start,end+1):
    if num<2:
        continue
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end=" ")'''
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    if num < 2:
        continue  # Skip numbers less than 2 (not prime)
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to √num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")  # Print the prime number
'''Enter start of range: 10
Enter end of range: 20
11 13 17 19 '''