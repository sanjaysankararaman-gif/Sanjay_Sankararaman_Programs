def get_trains():
    count = int(input("Enter number of trains: "))
    schedule = ()
    for i in range(count):
        print("Train", i + 1)
        number = int(input("Train number: "))
        name = input("Train name: ")
        destination = input("Destination: ")
        time = input("Departure time (HH:MM): ")
        schedule += ((number, name, destination, time),)
    return schedule


trains = get_trains()
print()

# a) Name and destination of the first train
print("a) Train name:", trains[0][1])
print("Destination:", trains[0][2])

# b) Complete details of the third train
print("b) Third train:", trains[2])

# c) Unpack each train and display
print("c) Train details:")
for train in trains:
    number, name, destination, time = train
    print("Train", number, "-", name, "goes to", destination, "and departs at", time)

# d) Search by destination
place = input("d) Enter a destination: ")
found = False
for train in trains:
    if train[2].lower() == place.lower():
        print("Train number:", train[0])
        print("Train name:", train[1])
        print("Destination:", train[2])
        print("Departure time:", train[3])
        found = True
if not found:
    print("No train found for that destination.")

# e) Train numbers of all trains
print("e) Train numbers:")
for train in trains:
    print(train[0])

# f) Total number of trains
print("f) Total number of trains:", len(trains))