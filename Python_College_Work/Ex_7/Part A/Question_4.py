f = open('t1.txt', 'a+')

def append_lines():
    n = int(input("Enter number of lines to be appended: "))
    for _ in range(n):
        a = input("Enter line: ")
        f.write(a+'\n')


def read_content():
    a = f.read()
    d,u,l = 0,0,0
    for i in a:
        if i.isdigit():
            d += 1
        elif i.isupper():
            u += 1
        elif i.islower():
            l += 1
    return d, u , l

append_lines()
read_content()

f.close()
