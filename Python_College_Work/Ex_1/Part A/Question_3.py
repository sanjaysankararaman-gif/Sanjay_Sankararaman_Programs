initial_temp = float(input("Enter temperature of the newborn in degree Celcius:")) #inputs the temperature in degree Celcius

print("Enter 1 for temperature conversion for International patient records")
print("Enter 2 for temperature conversion for research documentation") 
choice_of_records = int(input("")) #takes users choice for preferred record type

if choice_of_records == 1:
    F = (initial_temp * 9/5) + 32 #Converts Celcius to Farenheit
    print("Temperature in Farenheit = ", F)

elif choice_of_records == 2:
    K = (Initial_temp + 273.15) #Converts Celcius to Kelvin
    print("Temperature in Kelvin = ", K)
