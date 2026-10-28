def num_words(s):
    import math
    l = s.split()
    print("Number of words =", len(l))

    a = -math.inf
    b = ""
    for i in l:
        if len(i) > a:
            a = len(i)
            b = i

    print("Largest word in the sentence is =",b)


s = input("Enter a string =")

num_words(s)

    
