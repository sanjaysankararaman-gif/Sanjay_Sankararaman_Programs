# Inputing the marks obtained in each subject 
Sub_1 = float(input("Enter marks obtained in subject 1:"))
Sub_2 = float(input("Enter marks obtained in subject 2:"))
Sub_3 = float(input("Enter marks obtained in subject 3:"))
Sub_4 = float(input("Enter marks obtained in subject 4:"))

total = Sub_1 + Sub_2 + Sub_3 + Sub_4 #Finding total marks obtained in each subject

percentage = (total/400)*100 #Finding marks percentage, (marks obtained/total marks) x 100

#Finding the student's grade based on percentage
if percentage >= 90:
    print("Grade A")

elif percentage >= 80 and percentage < 90:
    print("Grade B")

elif percentage >= 70 and percentage < 80:
    print("Grade C")

elif percentage >= 60 and percentage < 70:
    print("Grade D")

else:
    print("Fail")
    
