salary = float(input("Enter employee salary:")) #Input salary 

gender = str(input("Enter employee gender:")) #Input gender

final_salary = 0

if gender.lower() == "male": #Checking whether person is a male. Changing the case of the words to lower to make sure that the program works no matter how the user types in the gender
    final_salary = 0.06 * salary 

elif gender.lower() == "female": #Checking whether person is a female. Changing the case of the words to lower to make sure that the program works no matter how the user types in the gende
    final_salary = 0.12 * salary

if salary < 12000: #Checking whether the salary is less than 12000
        final_salary = 0.03 * salary

print("Final Salary = ", final_salary + salary)
