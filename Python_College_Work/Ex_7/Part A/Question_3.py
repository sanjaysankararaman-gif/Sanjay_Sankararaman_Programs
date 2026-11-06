f = open('code.txt', 'r')
f1 = open('recode.txt', 'w')

a = f.readline()
while a:
    if a[0] != '#':
        f1.write(a)
    a = f.readline()

f.close()
f1.close()
