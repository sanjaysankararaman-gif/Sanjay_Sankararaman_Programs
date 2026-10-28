l = eval(input("Enter nested list of marks of students scored in each of the 3 subjects ="))

total = 0
for i in range(len(l)):
    print("Student", i)
    print("Marks in subject 1:", l[i][0])
    print("Marks in subject 2:", l[i][1])
    print("Marks in subject 3:", l[i][2])
    print("Total Marks:", sum(l[i]))
    print("Average Marks:", sum(l[i])/len(l[i]))
    total += sum(l[i])
print("Average marks =", total/len(l))
