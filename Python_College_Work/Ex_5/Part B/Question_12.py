def input_register():
    workshop1 = eval(input('Enter list of names of people registered to Workshop 1: '))
    workshop2 = eval(input("Enter list of names of people registered to Workshop 2: "))
    return workshop1, workshop2

workshop1, workshop2 = input_register()

req_list = []

for i in workshop2:
    if i not in workshop1:
        req_list.append(i)

print(req_list)