a = int(input("Enter a number:"))
b = int(input("Enter a number:"))


print("Enter 1 to compute AND of the given values")
print("Enter 2 to compute OR of the given values")
print("Enter 3 to compute NOT of the given values")
print("Enter 4 to compute XOR of the given values")
print("Enter 5 to find the left shift of the given values")
print("Enter 6 to find the right shift of the given values")
print("Enter 7 to find whether the given numbers are even or odd")
choice = int(input(""))

if choice == 1:
    print(a, "AND", b, "is", bin(a & b), "in binary and", a & b, "in decimal system")

elif choice == 2:
    print(a, "OR", b, "is", bin(a | b), "in binary and", a | b, "in decimal system")

elif choice == 3:
    print("NOT", a, "is", bin(~a), "in binary and", ~ a, "in decimal system")
    print("NOT", b, "is", bin(~b), "in binary and", ~ b, "in decimal system")
    
elif choice == 5:
    shift = int(input("Enter number to shift number by:"))

    print(a, "<<", shift, "=", a << shift)
    print(b, "<<", shift, "=", b << shift)

elif choice == 4:

    print(a, "XOR", b, "=", a^b)

elif choice == 6:
    shift = int(input("Enter number to shift number by:"))

    print(a, ">>", shift, "=", a >> shift)
    print(b, ">>", shift, "=", b >> shift)

elif choice == 7:
    if a & 1 == 0:
        print("Even")
    else:
        print("Odd")

    if b & 1 == 0:
        print("Even")
    else:
        print("Odd")
