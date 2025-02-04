a=input(" ")
numbers=[]
alphabets=[]
for i in a:
    if i.isalpha():
        alphabets.append(i)
    else:
        numbers.append(i)
res=sorted(alphabets)+sorted(numbers)
output=" ".join(res)
print(output)


'''a = "A7V2B1"
numbers = []
alphabets = []

for i in a:
    if i.isalpha():
        alphabets.append(i)
    else:
        numbers.append(i)

res = sorted(alphabets) + sorted(numbers)  # Sorting letters and numbers separately
output = "".join(res)  # Joining as a single string
print(output)
'''