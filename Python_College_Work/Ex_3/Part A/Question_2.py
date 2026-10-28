def calculate_bil(units, rate=8):
    b = rate * units
    if units > 300:
        b += 0.1 * rate * units #10% extra fees
        return b + 50 #additional 50 rupees for meter maintance 

    else:
        return b + 50 #additional 50 rupees for meter maintance 


units = int(input("Enter units of electricity used ="))
rate = float(input("Enter rate ="))

print(calculate_bil(units, rate))
