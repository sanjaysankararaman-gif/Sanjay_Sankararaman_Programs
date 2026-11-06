#We are assuming that each student name in student.txt is in a seperate line

def sort_studentname():
    f = open('student.txt', 'r')
    f1 = open('sortstudent.txt', 'w')

    a = f.readlines()
    a = sorted(a)
    for i in a:
        f1.write(i)

    f.close()
    f1.close()


sort_studentname()
