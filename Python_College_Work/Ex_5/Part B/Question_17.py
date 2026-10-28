t = eval(input("Enter a tuple: "))
t_new = tuple()

a = t[0]
for i in range(1,len(t)):
    if a == t[i]:
        continue
    else:
        t_new += (a,)
        a = t[i]
t_new += (a,)

print(t_new)