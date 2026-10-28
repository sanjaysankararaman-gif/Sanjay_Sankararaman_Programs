neg = 0
pos = 0
odd = 0
even = 0
count = 0

a = True
while a: #The loop continues till a is declared as False
    num = int(input("Enter a number:"))
    count += 1

    if num % 2 ==0: #Checking whether num is even or odd by divisibilty test
        even += 1
    else:
        odd += 1

    if num >= 0: #Checking whether num is negative or positive or zero
        pos += 1
    else:
        neg +=1

    choice = input("Enter exit to exit and enter any other character to continue:") #asking user whether they want to exit or continue

    if choice.lower() == "exit": #if choice is exit, a is intiliased to False
        a = False
    else:
        a = True

print("Number of counts the loop went on:", count) #printing data
print("Number of odd numbers entered:", odd)
print("Number of even numbers entered:", even)
print("Number of positive numbers entered:", pos)
print("Number of negative numbers entered:", neg)
