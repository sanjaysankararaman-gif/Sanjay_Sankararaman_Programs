shape_name = input("Enter shape:") #Inputs name of the shape
choice = input("Enter A to calucalte area and P to calculate perimeter:") #Takes choice of whether the user wants to calculate Area of perimeter


if shape_name.lower() == "rectangle": # .lower() ensures there is no error when the user gives the name of the shape in someother case
    length = float(input("Enter length of rectangle:"))
    breadth = float(input("Enter breadth of rectangle:"))

    if choice == "A": #when choice is Area, calculates Area
        Area = length * breadth
        print("Area of rectangle = ", Area)
    else:
        Perimeter = 2*(length + breadth) #when choice is perimeter, calculate perimeter
        print("Perimeter of rectangle = ", Perimeter)
    

elif shape_name.lower() == "square":
    side_length = float(input("Enter side length of square:"))

    if choice == "A": #when choice is Area, calculates Area
        Area = side_length * side_length
        print("Area of square = ", Area)
    else:
        Perimeter = 4 * side_length #when choice is perimeter, calculate perimeter
        print("Perimeter of square = ", Perimeter)

elif shape_name.lower() == "triangle":
    base_length = float(input("Enter length of base:"))
    height_length = float(input("Enter length of height:"))

    if choice == "A": #when choice is Area, calculates Area
        Area = 0.5 * base_length * height_length
        print("Area of triangle = ", Area)

    else:
        side_1 = float(input("Enter length of the first side:")) #input for each side's length
        side_2 = float(input("Enter length of the second side:"))
        side_3 = float(input("Enter length of the third side:"))

        Perimeter = side_1 + side_2 + side_3 #when choice is perimeter, calculate perimeter
        print("Perimeter of triangle = ", Perimeter)
        
