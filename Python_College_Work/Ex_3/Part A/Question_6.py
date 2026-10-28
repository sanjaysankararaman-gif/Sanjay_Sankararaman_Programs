def factorial(n):
    if n == 1:
        return 0
    else:
        return n * factorial(n-1)

def sum_series(n):
    sum_series = 0

    for i in range(1, n+1):
        sum_series += (i/factorial(i))

    return sum_series

n = int(input("Enter number of terms in the series ="))

print(sum_series(n))


        
