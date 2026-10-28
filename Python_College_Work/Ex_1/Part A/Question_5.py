x1 = float(input("Enter x coordinate of the first point:"))
y1 = float(input("Enter y coordinate of the first point:"))

x2 = float(input("Enter x coordinate of the second point:"))
y2 = float(input("Enter y coordinate of the second point:"))


Distance = ((x2-x1)**2 + (y2-y1)**2)**(0.5)

Midpoint_x = (x1 + x2)/2
Midpoint_y = (y1 + y2)/2

print("Distance between the points = ", Distance)
print("Midpoint coordinates = ", "(", Midpoint_x, ",",Midpoint_y, ")")
