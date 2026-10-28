def man_replace(s,x):
    new = ""
    for i in s:
        if i == x:
            new += "*"
        else:
            new += i
    return new

s = input("Enter a string =")
x = input("Enter character to be replaced =")

print(man_replace(s,x))

