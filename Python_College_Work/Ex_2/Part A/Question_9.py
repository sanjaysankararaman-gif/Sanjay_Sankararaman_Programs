for i in range(2, 501):
#The upper limit of range is 501, since the question requires us to print prime numbers from 1 to 500.
#Since 1 is not a prime number, the lower limit is 2 since it is the first prime number
    k = 0
    for j in range(2,i): #The loop is from 2 to i-1 because, every number is divisible by 1 and itself. A prime number should not have any other factors other than these two numbers
        if i % j == 0:
            k+=1
    if k == 0:
        print(i , end=",")

        
    
