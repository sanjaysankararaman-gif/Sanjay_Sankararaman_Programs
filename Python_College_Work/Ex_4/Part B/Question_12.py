def rep_let_count(s):
    new=''
    d=0
    while d < len(s):
        b = s[d]
        c = 0
        for j in range(d,len(s)):
            if b == s[j]:
                c += 1
            else:
                new += b + str(c)
                d = j
                break
        else:
            d = len(s)
            new += b + str(c)

    print(new)

s = input("Enter a string =")

rep_let_count(s)
