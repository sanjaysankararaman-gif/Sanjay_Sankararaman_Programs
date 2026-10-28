def sum_of_multiples(n, divisor):
    if n == 0:
        return 0
    elif n % divisor == 0:
        return n + sum_of_multiples(n-1, divisor)
    else:
        return sum_of_multiples(n-1, divisor)

n = int(input("Enter a number ="))
divisor = int(input("Enter a divisor ="))

print(sum_of_multiples(n, divisor))