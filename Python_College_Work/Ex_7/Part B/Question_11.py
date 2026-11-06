f = open('attendance.txt', 'r')
f1 = open('attendance_alerts.txt','w')
g,w,l = 0,0,0
a = f.readline()
while a:
    s = a.rstrip('\n').split(',')
    print('Student Name:', s[0])
    print('Attendance Percentage:',s[-1])
    if s[-1] >= 85:
        g += 1
        c = 'Good'
        
    elif s[-1] >= 75 and s[-1] < 85:
        w += 1
        c = 'Warning'

    elif s[-1] < 75:
        l += 1
        c = 'Low'
        f1.write(a)
        

    print('Attendance Category:', c)
    a = f.readline()

f.close()
f1.close()
print()
print("Number of students with Good attendance: ", g)
print("Number of students with Warning category attendance: ", w)
print("Number of students with Low attendance :",l)



    
        
        
