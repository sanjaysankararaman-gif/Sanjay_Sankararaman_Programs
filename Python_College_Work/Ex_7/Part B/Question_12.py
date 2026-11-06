f = open('environment.txt', 'r')
f1 = open('environment_alerts.txt', 'w')
a = f.readline()
d = dict()
water = ['rainfall', 'flooding', 'lake', 'water']
air = ['air', 'pollution', 'smoke']
waste = ['plastic', 'waste', 'garbage']
pos_env = ['improved', 'cleanup', 'planting', 'reduced']

while a:
    air, wa, wt, pos = 0,0,0,0
    s = a.rstrip('\n')
    s1 = a.split()
    for i in s1:
        if i.lower() in water:
            wt += 1
        if i.lower() in air:
            air += 1
        if i.lower() in waste:
            wa += 1
        if i.lower() in pos_env:
            pos += 1
    print(s)
    f1.write(s+" ")
    print("Categories: ")
    if air > 0:
        print("Air Pollution")
        f1.write("Air Pollution"+" ")
    if wt > 0:
        print("Water Pollution")
        f1.write("Water Pollution"+" ")
    if wa > 0:
        print("Waste Issues")
        f1.write("Waste Issues"+" ")
    if pos > 0:
        print("Positive Environmental Action")
        f1.write("Positive Environmental Action"+" ")

    f1.write("\n")
    a = f.readline()


    
            
    
    
