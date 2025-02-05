def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Calculate LCM using the formula
lcm = abs(a * b) // gcd(a, b)

# Output the result
print("LCM is:", lcm)