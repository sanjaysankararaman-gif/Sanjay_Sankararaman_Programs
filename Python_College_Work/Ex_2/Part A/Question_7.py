n = int(input("Enter number of terms in the series:"))
x = int(input("Enter a number:"))

#Series (a)

print("Series (a)")
series_1 = 0
for i in range(n):
    series += 2

print(series_1)

#Series (b)

print("Series (b)")

series_2 = 1 #initializing the value to 1 because the first term is 1

for i in range(2, n+1):
    series_2 += ((x**i)/i)

print(series_2)

#Series (c)

series_3 = 0

print("Series (c)")

for i in range(1,n+1):
    if i%2 != 0: #when i is a odd number, add the term
        series_3 += ((x**i)/i)
    else: #when i is an even number, subtract the term
        series_3 -= ((x**i)/i)

print(series_3)
