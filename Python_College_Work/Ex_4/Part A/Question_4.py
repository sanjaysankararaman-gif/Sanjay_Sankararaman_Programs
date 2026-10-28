def count_type_char(s):
    l,u,d,s=0,0,0,0
    for i in s:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i.isdigit():
            d += 1
        elif i.isalpha():
            s += 1
    print("Number of lower case characters =",l)
    print("Number of upper case characters =",u)
    print("Number of digits =",d)
    print("Number of special characters =",s)

s=input("Enter a string =")
count_type_char(s)

