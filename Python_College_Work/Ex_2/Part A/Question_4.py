year = int(input("Enter a year:")) #Inputiing the year

if year % 4 == 0: #if year is divisible by 4 it is a leap year unless it is a century year
    if year % 100 == 0: #Checking if it is a century
        if year % 400 == 0: #If it is divisible by 400 it is a leap year
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else: #if it is not a century year, then it is a leap year since it is divisible by 4
        print("Leap Year")
else: #if a year is not divisible by 4, it is not a leap year
    print("Not a Leap Year")

