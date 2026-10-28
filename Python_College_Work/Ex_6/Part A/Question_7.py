import math
def dict_input():
    d = dict()
    n = int(input("Enter number of entries: "))
    for _ in range(n):
        product = input("Enter product name: ")
        price = int(input("Enter product price: "))
        d[product] = price
    return d


def sort_dict_key_asc_desc(d):
    asc = dict(sorted(d.items()))
    desc = dict(sorted(d.items(), reverse='True'))

    print("Ascending order: ", asc)
    print("Descending order: ", desc)

def sort_dict_value_asc_desc(d):
    ascending  = {}
    new = d.copy()
    while len(new) != 0:
        a = math.inf
        n= ''
        for i in new:
            if new[i] < a:
                a = new[i]
                n = i
        del new[n]
        ascending[n] = a
    print("Ascending order: ")
    print(ascending)
    print()

    descending = {}
    new_1 = d.copy()
    while len(new_1) != 0:
        a = -math.inf
        n = ''
        for i in new_1:
            if new_1[i] > a:
                a = new_1[i]
                n = i
        del new_1[n]
        descending[n] = a
    print("Descending order: ")
    print(descending)

def sort_dict_value_asc_desc_1(d):
    asc =  dict(sorted(d.items(),key=lambda x: x[1]))
    desc = dict(sorted(d.items(), key= lambda x: x[1], reverse = "True"))
    print("Ascending order: ", asc)
    print("Descending order: ", desc)

def most_exp_least_exp(d):
    a = math.inf
    n = ''
    b = -math.inf
    m = ''
    for i in d:
        if d[i] < a:
            n = i
            a = i
        if d[i] > b:
            m = i
            b = i
    print("Most Expensive product: ", m)
    print("Least Expensive product: ", n)
d = dict_input()
sort_dict_key_asc_desc(d)
sort_dict_value_asc_desc(d)
most_exp_least_exp(d)


        
