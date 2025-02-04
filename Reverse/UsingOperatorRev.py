n = 123
rev = 0

while n > 0:
    digit = n % 10  # Extract last digit
    rev = (rev * 10) + digit  # Append digit to reversed number
    n = n // 10  # Remove last digit

print(rev)
