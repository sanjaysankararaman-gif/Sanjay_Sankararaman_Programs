def count(n):
    count = 0
    while n > 0:
        a = n%10
        n = n//10
        count += 1
    return count

def is_armstrong(n):
    power = count(n)
    back_up = n
    sum_num = 0

    while n > 0:
        a = n%10
        sum_num += a**power
        n = n//10

    if back_up == sum_num:
        print("Armstorng Number")
    else:
        print("Not an Armstrong Number")
        
        
    
        
