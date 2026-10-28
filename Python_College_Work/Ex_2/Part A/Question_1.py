side_1 = float(input("Enter length of first side of the triangle:")) #Input length of side 1
side_2 = float(input("Enter length of the second side of the triangle:")) #Input length of side 2
side_3 = float(input("Enter length of the third side of the triangle:")) #Input length of side 3

if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_3 + side_2 > side_1:   #Checking whether the given triangle is valid
    print("Valid Triangle")

    if side_1 == side_2 and side_2 == side_3:   #Equilateral triangle is has all sides equal
        print("The given triangle is Equilateral")

    elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:  #Isoceles triangle has any two sides equal
        print("The given triangle is Isoceles")

    else:
        print("The given triangle is Scalene")

else:                               #If the given triangle is not valid, the checking for equilateral, isoceles and scalene does not happen
    print("Not a Triangle")

    
