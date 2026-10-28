def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci(n-2)

n = int(input("Enter term of fibonacci series ="))

print(fibonacci_recursive(n))

