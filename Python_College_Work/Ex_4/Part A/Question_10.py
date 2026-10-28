def print_tags(s):
    s1 = s
    s1 = s1.strip()
    l = s1.split()
    for i in l:
        if i[0] == "#":
            print(i, end="")

s = input("Enter a string =")
print_tags(s)

