def assignment_analyser(file_name):
    f = open(file_name, 'r')
    a = f.readlines()
    l = len(a)
    words, char = 0, 0
    for i in a:
            for j in i:
                if i != '\n':
                    char +=1
            for j in i.rstrip('\n').split():
                words += 1
    f.close()
    return char, words, l


                
