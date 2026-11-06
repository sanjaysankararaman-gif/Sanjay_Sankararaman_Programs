def Find_all(file_name):
    d = dict()
    f = open(file_name, 'r')
    a = f.readline()
    while a:
        a = a.rstrip('\n')
        for i in a.split():
            if i.lower() not in d:
                d[i.lower()] = 1
            else:
                d[i.lower()] += 1
        a = f.readline()

    f.close()
    return d

file_name = input("Enter file name in the below format \neg. file.txt: ")
d = Find_all(file_name)
print(d)
