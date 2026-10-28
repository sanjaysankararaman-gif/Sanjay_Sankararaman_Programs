def statistics(*numbers):
    import math
    count = 0
    sum_num = 0
    for i in numbers:
        count += 1
        sum_num += i

    maxi = -math.inf
    mini = math.inf

    for i in numbers:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    avg = (sum_num/count)

    return sum_num, avg, maxi, mini

#print(statistics(1,2,3,4))


        
