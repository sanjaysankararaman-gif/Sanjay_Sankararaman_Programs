festivals = {
 "Pongal": {"activities": ["Kolam", "Folk Dance", "Cooking Contest"],
 "days": 3, "budget": 25000.0, "location": "Chennai"},
 "Music Festival": {"activities": ["Classical Music", "Light Music", "Dance"],
 "days": 2, "budget": 18000.0, "location": "Coimbatore"},
 "Food Festival": {"activities": ["Cooking Show", "Food Stalls", "Tasting Event"],
 "days": 4, "budget": 30000.0, "location": "Madurai"},
 "Book Festival": {"activities": ["Book Exhibition", "Author Talk", "Quiz"],
 "days": 2, "budget": 12000.0, "location": "Chennai"}
}

def disp_fest_details():
    for k,v in festivals.items():
        print('Festival Name: ',k)
        print("Activities: ",v['activities'])
        print("Number of days: ",v['days'])
        print("Budget: ",v['budget'])
        print("Location: ",v['location'])

def add_new_festival():
    festival = input("Enter festival name: ").title()
    activities = eval(input("Enter list of activities: "))
    days = int(input("Enter the duration of the festival: "))
    budget = float(input("Enter festival budget: "))
    location = input("Enter the city where the festival will be conducted: ").title()
    festivals[festival] = {'activities': activities, 'days': days, 'budget': budget, 'location': location}

def update_budget_duration():
    festival = input("Enter name of the festival: ").title()
    if festival in festivals:
        budget = float(input("Enter the festival budget: "))
        days = int(input("Enter duration of the festival: "))
        festivals[festival]['budget'] = budget
        festivals[festival]['days'] = days
    else:
        print("Festival does not exist")

def budget_below_amount():
    amt = float(input("Enter budget amount: "))
    print('Festivals below ceratin budget: ')
    for k,v in festivals.items():
        if v['budget'] < amt:
            print(k)

def fest_3_act_days():
    print('Festivals that have at least three activities and last no more than three days')
    for k,v in festivals.items():
        if len(v['activities']) >=  3 and v['days'] <= 3:
            print(k)

def high_low_budget():
    import math
    high = -(math.inf)
    low = math.inf
    fest_h = ''
    fest_l = ''
    for k,v in festivals.items():
        if v['budget'] > high:
            high = v['budget']
            fest_h = k

        if v['budget'] < low:
            low = v['budget']
            fest_l = k

    print("Festival with highest budget: ", fest_h)
    print("Festival with lowest budget: ", fest_l)

def total_budget():
    total = 0
    for k,v in festivals.items():
        total += v['budget']
    return total

def add_new_act():
    festival = input("Enter name of the festival: ").title()
    if festival in festivals:
        act = input("Enter name of the new activity: ")
        festivals[festival]['activities'].append(act)
    else:
        print('Festival does not exist')

def fest_in_chennai():
    print("Festivals happening in Chennai")
    for k,v in festivals.items():
        if v['location'].lower() == 'chennai':
            print(k)

a = True
while a:
    print("Enter 1 to display all festivals and their details")
    print("Enter 2 to add a new festival with its activities, duration, budget, and location")
    print("Enter 3 to update the budget and duration of an existing festival")
    print("Enter 4 to display festivals whose budget is below an amount entered by the user")
    print("Enter 5 for festivals that have at least three activities and last no more than three days")
    print("Enter 6 to identify the festivals with the highest and lowest budgets")
    print("Enter 7 to sort festivals by budget in ascending order")
    print("Enter 8 to calculate the total budget of all festivals")
    print("Enter 9 to add a new activity to an existing festival")
    print("Enter 10 to display all festivals conducted in Chennai")
    print("Enter 11 to exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        disp_fest_details()
    elif choice == 2:
        add_new_festival()
    elif choice == 3:
        update_budget_duration()
    elif choice == 4:
        budget_below_amount()
    elif choice == 5:
        fest_3_act_days()
    elif choice == 6:
        high_low_budget()
    elif choice == 7:
        print("Festivals sorted by budget in ascending order: ", dict(sorted(festivals.items(), key = lambda x: x[1]['budget'])))
    elif choice == 8:
        print("Total budget of all festivals: ", total_budget())
    elif choice == 9:
        add_new_act()
    elif choice == 10:
        fest_in_chennai()
    elif choice == 11:
        a = False
    else:
        print("Invalid Choice")











