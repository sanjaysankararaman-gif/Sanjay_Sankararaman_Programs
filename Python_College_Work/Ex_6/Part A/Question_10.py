student_marks = {
 "Arun": 85,
 "Priya": 92,
 "Kavin": 85,
 "Meena": 78,
 "Divya": 92,
 "Rahul": 88}

n = int(input("Enter mark: "))

found = False
for k,v in student_marks.items():
    if n == v:
        print(k)
        found = True

if found == False:
    print("Mark not scored by any student")
    