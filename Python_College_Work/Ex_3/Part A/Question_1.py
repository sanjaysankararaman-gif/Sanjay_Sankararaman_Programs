def convert_units(value, unit):
    if unit.lower() == "miles":
        miles = 0.62137119 * value
        return miles
    elif unit.lower() == "meter":
        meter =  1000 * value
        return meter

value = float(input("Enter distance ="))
unit = str(input("Enter units of distance to which the value is to be converted to ="))

print(convert_units(value,unit))
