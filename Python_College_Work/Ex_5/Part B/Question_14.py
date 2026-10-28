t = eval(input("Enter a tuple: "))
k = int(input("Enter number of rotation by right: "))

def right_shift(t):
    a = t[-1]
    l = list(t)
    for i in range(len(t)-1,0,-1):
        l[i] = l[i-1]
    l[0] = a
    return tuple(l)

def number_of_shifts(t,k):
    for _ in range(k):
        t = right_shift(t)
    print(t)

number_of_shifts(t,k)