f = open('secret.txt', 'r')
f1 = open('decoded.txt', 'w+')

a = f.readlines()
for i in a:
    for j in i.rstrip('\n').split():
        f1.write(j+'\n')

b = f1.readline()
while b:
    print(b)
    b = f1.readline()

f.close()
f1.close()


        
