f = open('ebook.txt', 'r')

a = f.readline()
while a:
    print(a)
    a = f.readline()

f.close()
