import keyword

f = open('code.txt', 'r')
a = f.readline()
print("Words that are keywords:")

while a:
    a = a.rstrip('\n')
    for i in a.split():
        if keyword.iskeyword(i):
            print(i)
        else:
            continue
    a = f.readline()

f.close()
