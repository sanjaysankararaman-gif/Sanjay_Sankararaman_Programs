branch1 = {"Rice":20,"Sugar":15,"Oil":10}
branch2 = {"Rice": 12, "Sugar": 8, "Wheat": 18}

dict_new = branch1.copy()
dict_new.update(branch2)

print(dict_new)
print()

d1 = branch1.copy()
for i in branch2:
    if i in d1:
        d1[i] = branch2[i] + branch1[i]
    else:
        d1[i] = branch2[i]

print(d1)
print()

for i in d1:
    print("Product :", i)
    print("Quantity :", d1[i])
    print()
    
