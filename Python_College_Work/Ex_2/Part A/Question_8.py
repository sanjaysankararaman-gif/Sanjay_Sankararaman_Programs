num = int(input("Enter a number:")) #input number 

backup = num #storing number in another variable for backup

new_num = 0 #creating a new variable for the reversed number

while num > 0: #Till num is 0
    a = num % 10 #Getting the last digit of the number
    num = num //10 #removing the last digit of the number
    new_num = new_num * 10 + a #multiplying 10 to the exisiting value of new_num, and adding a to form the reversed number

if new_num == backup:
    print(num , "is a palindrome")
else:
    print(num, "is not a palindrome")
