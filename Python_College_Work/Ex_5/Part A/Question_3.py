l = list()
def enter_elements(l):
    for _ in range(10):
        n = int(input("Enter an integer ="))
        l.append(n)


def disp_list(l):
    print(l)

def small_ele(l):
    s = l[0]
    for i in l:
        if i < s:
            s = i
        else:
            continue
    return s

def large_ele(l):
    l = l[0]
    for i in l:
        if i > l:
            l = i
        else:
            continue
    return l

def search(l,s):
    for i in range(len(l)):
        if l[i] == s:
            print(i)
            break
    else:
        print("Does not exist")

enter_elements(l)
a = True
while a:
    print("Enter 1 to diplay list")
    print("Enter 2 to find the smallest element")
    print("Enter 3 to find the largest element")
    print("Enter 4 to search the element")
    print("Enter 5 to exit")
    choice = int(input("Enter choice = "))

    if choice == 1:
        disp_list(l)
    elif choice == 2:
        print(small_ele)
    elif choice == 3:
        print(large_ele)
    elif choice == 4:
        s = int(input("Enter number to be searched in list:"))
        search(l,s)
    elif choice == 5:
        a = False
    else:
        print("Invalid choice")

 
