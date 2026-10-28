def input_coordinates():
    xvals = eval(input("Enter a list of numbers: "))
    yvals = eval(input("Enter a list of numbers: "))
    return xvals, yvals

xvals, yvals = input_coordinates()
print(xvals)
print(yvals)

req_list_1 = []
for i in xvals:
    for j in yvals:
        if (i+j) % 2 == 0:
            req_list_1.append((i,j))

for i in yvals:
    for j in xvals:
        if (i+j) % 2 == 0:
            req_list_1.append((i,j))

req_list = []
for i in req_list_1:
    if i not in req_list:
        req_list.append(i)

print(req_list)
