a = "A7V2B1"
numbers = []
alphabets = []

for i in a:
    if i.isalpha():
        alphabets.append(i)
    else:
        numbers.append(i)

alphabets.sort()
numbers.sort()

# Merge one alphabet and one number alternately
res = []
i, j = 0, 0

while i < len(alphabets) and j < len(numbers):
    res.append(alphabets[i])
    res.append(numbers[j])
    i += 1
    j += 1
# If extra alphabets left
while i < len(alphabets):
    res.append(alphabets[i])
    i += 1

# If extra numbers left
while j < len(numbers):
    res.append(numbers[j])
    j += 1

# Convert list to string
output = "".join(res)
print(output)

'''
a="AVB216
numbers=[]
alphabets=[]
for i in a:
    if i.isalpha():
        alphabets.append(i)
    else:
        numbers.append(i)
alphabets.sort()
numbers.sort()
res=[]
i=0
j=0
while i<len(alphabets) and j<len(numbers):
    res.append(alphabets[i])
    res.append(j)
    i+=1
    j+=1



'''