def replace_char(s,x):
    s1 = s
    s1 = s1.strip()
    l = s1.split()
    new = ""

    for i in l:
        if i.lower() == x.lower():
            new += "*" * len(i)+ " "
        else:
            new += i + " "

    return new

s = input("Enter a string =")
x = input("Enter bad character =")

replace_char(s,x)
