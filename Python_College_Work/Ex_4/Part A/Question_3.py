def man_count(s,x):
    count = 0
    for i in s:
        if i==x:
            count += 1
        else:
            continue
    print(x, "repeats in",s,count,"times")

s = input("Enter a string =")
x = input("Enter a character =")
man_count(s,x)
