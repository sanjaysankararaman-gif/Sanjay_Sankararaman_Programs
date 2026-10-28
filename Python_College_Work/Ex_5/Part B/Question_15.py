s = input("Enter a sentence: ")
l = [i.upper() for i in s.split() if len(i) > 3 ]
print(l)