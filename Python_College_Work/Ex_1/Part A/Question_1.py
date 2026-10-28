Principal = float(input("Enter Principal amount:")) 
Number_of_Years = int(input("Enter number of years:"))
Rate = float(input("Enter rate of interest"))

Simple_Interest = (Principal*Number_of_Years*Rate)/100 #formula to calculate Simple Interest
Maturity_Amount = Simple_Interest + Principal

print("Simple Interest:", Simple_Interest) #prints the Simple Interest
print("Maturity Amount:", Maturity_Amount) #Maturity amount is Simple interest + principal amount
