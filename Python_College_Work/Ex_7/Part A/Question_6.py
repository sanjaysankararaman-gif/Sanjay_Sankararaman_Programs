def display_words():
    f = open('ebook.txt', 'r')
    a = f.readline()
    print("Words with less than 4 characters:")
    while a:
        a = a.rstrip('\n')
        for i in a.split():
            if len(i) < 4:
                print(i)
            else:
                continue
        a = f.readline()

    f.close()


display_words()
