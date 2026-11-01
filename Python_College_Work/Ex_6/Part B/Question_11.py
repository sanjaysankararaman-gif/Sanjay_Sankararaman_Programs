weather = {"Chennai": {"temperature": 34.5, "humidity": 70, "rainfall": 12.5}, "Coimbatore": {"temperature": 31.0, "humidity": 65, "rainfall": 8.0}, "Madurai": {"temperature": 36.2, "humidity": 60, "rainfall": 4.5}, "Ooty": {"temperature": 22.5, "humidity": 80, "rainfall": 25.0}}

def display_weather_details():
    for k,v in weather.items():
        print("City: ",k)
        print("Temperature: ", v['temperature'])
        print("Humidity: ",v['humidity'])
        print("Rainfall: ",v['rainfall'])

def add_weather_info():
    city = input("Enter the name of the city: ").title()
    temp = float(input("Enter temperature of city: "))
    humid = float(input("Enter humidity level of city: "))
    rain = float(input("Enter rainfall level of the city: "))
    weather[city] = {"temperature": temp, "humidity": humid, "rainfall": rain}

def update_information(city):
    city = city.title()
    if city in weather: 
        print("Enter 1 to update the temperature")
        print("Enter 2 to update the humidity")
        print("Enter 3 to update the rainfall")
        choice = int(input("Enter choice: "))

        if choice == 1:
            n = float(input("Enter new temperature: "))
            weather[city]['temperature'] = n
        elif choice == 2:
            n = float(input("Enter new humidity level: "))
            weather[city]['humidity'] = n
        elif choice == 3:
            n = float(input("Enter new rainfall level: "))
            weather[city]['rainfall'] = n
        else:
            print("Invalid Choice. Try Again")
    else:
        print("City not present in dictionary")

def temp_exceeds():
    for i in weather:
        if weather[i]['temperature'] > 33:
            print(i)
    
def highest_temp():
    import math
    temp = -(math.inf)
    city_t = ''
    for i in weather:
        if weather[i]['temperature'] > temp:
            temp = weather[i]['temperature']
            city_t = i
    print("City with highest temperature: ", city_t)

def highest_rainfall():
    rainfall = 0
    city_r = ''
    for i in weather:
        if weather[i]['rainfall'] > rainfall:
            rainfall = weather[i]['rainfall']
            city_r = i
    print("City with highest rainfall: ", city_r)
    
def avg_temp():
    total = 0
    for i in weather:
        total += weather[i]['temperature']

    return sum/len(weather)

def disp_humidity():
    print("Cities with humidity greater than 70:")
    for i in weather:
        if weather[i]['humidity'] > 70:
            print(i)

def total_rainfall():
    sum = 0 
    for i in weather:
        sum += weather[i]['rainfall']
    return sum

a = True
while a:
    print("Enter 1 to display weather details for all cities")
    print("Enter 2 to add weather inforomation for a new city")
    print("Enter 3 to update the temperature, humidity, or rainfall for a city")
    print("Enter 4 to display cities where the temperature exceeds 33°C")
    print("Enter 5 to identify the city with the highest temperature")
    print("Enter 6 to identify the city with the highest rainfall")
    print("Enter 7 to calculate the average temperature across all cities")
    print("Enter 8 to sort cities by temperature in ascending order")
    print("Enter 9 to display cities with humidity above 70%")
    print("Enter 10 to calculate the total recorded rainfall across all cities")
    print("Enter 11 to exit")
    choice = int(input("Enter choice from 1 to 11: "))

    if choice == 1:
        display_weather_details()
    elif choice == 2:
        add_weather_info()
    elif choice == 3:
        city = input("Enter name of the city: ")
        update_information(city)
    elif choice == 4:
        temp_exceeds()
    elif choice == 5:
        highest_temp()
    elif choice == 6:
        highest_rainfall()
    elif choice == 7:
        print(avg_temp())
    elif choice == 8:
        print("Sort cities by temperature in ascending order: ", dict(sorted(weather.items(), key = lambda x: x[1]['temperature'])))
    elif choice == 9:
        disp_humidity()
    elif choice == 10:
        print('Total rainfall: ', total_rainfall())
    elif choice == 11:
        a = False
    else:
        print("Invalid Choice")





