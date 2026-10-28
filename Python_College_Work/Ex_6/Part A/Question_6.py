d = dict()
def review_freq(s):
    l = s.lower().split()
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1


a = True
while a:
    print("Enter 0 to stop or Enter customer review")
    s = input("Enter customer review: ")
    if s == '0':
        a = False
    else:
        review_freq(s)
print()
print(d)
for i in d:
    if d[i] > 1:
        print(i)
