l=list()
def enter_elements():
    a = True
    while a:
        print("Enter product IDs")
        print("Enter 1 to exit")
        print("Enter any key other than 1 to continue")
        choice = int(input("Enter choice:"))
        if choice == 1:
            a = False
        else:
            i = int(input("Enter product ID:"))
            l.append(i)

enter_elements()

def new_list():
    new = []
    for i in l:
        if count(i) > 1:
            new.append(i)
        else:
            continue
    print(new)

new_list()
            





    
    
    
