def input_sales():
    l=[]
    for i in range(4):
        g = []
        for j in range(4):
            n = int(input("Enter sale amount for the month: "))
            g.append(n)
        l.append(g)
    return l

l = input_sales
print("Sales made by the second branch in the first month", l[1][0])


def total_monthly_sale(l):
    for i in l:
        a += i[0]
        b += i[1]
        c += i[2]
        d += i[3]
    k = [a,b,c,d]
    print("First Month Sales: ",a)
    print("Second Month Sales: ",b)
    print("Third Month Sales: ",c)
    print("Fourth Month Sales: ",d)
    print()
    print("Highest Individual Sales: ", max(k))
    return k



