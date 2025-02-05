def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    '''a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b'''
    return fibonacci(n-1)+fibonacci(n-2)

# Example Usage
n = int(input("Enter a number: "))
print(f"Fibonacci({n}) =", fibonacci(n))
