num = int(input("Enter a number from 1 to 12:"))

match num: #Matching num with numbers from 1 to 12 and months
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("Novemeber")
    case 12:
        print("December")
    case _: #if num is not in the range(1, 13), it prints invalid month
        print("Invalid Month")

'''
This can also be done

dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

print("Month is", dict[num])

'''
