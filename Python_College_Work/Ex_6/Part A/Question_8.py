accounts = { 
    1001: {"name": "Arun", "balance": 5000}, 
    1002: {"name": "Priya", "balance": 8000}, 
    1003: {"name": "Kumar", "balance": 3000}}

def search_accounts(n):
    for i in accounts:
        if i == n:
            print("Account Holder Name:", accounts[i]['name'])
            print("Account balance:", accounts[i]['balance'])
    else:
        print("Invalid Account number")

def deposit_amount(n):
    for i in accounts:
        if i == n:
            if accounts[i]['balance'] > 0:
                a = float(input("Enter amount to be deposited: "))
                accounts[i]['balance'] += a
                print("Current Balance: ", accounts[i]['balance'])
            else:
                print("Negative account balance")
    else:
        print("Invalid Account number")

def withdraw_amount(n):
    for i in accounts:
        if i == n:
            a = float(input("Enter amount to be withdrawn: "))
            if accounts[i]['balance'] >= a:
                accounts[i]['balance'] -= a
                print("Current Balance: ", accounts[i]['balance'])
            else:
                print("Insufficient balance")
    else:
        print("Invalid Account number")

def display_accounts():
    for i in accounts:
        print("Account Number: ",i)
        print("Account Balance: ",accounts[i])

def total_bank_balance():
    sum = 0
    for i in accounts:
        sum += accounts[i]['balance']
    print(sum)

a = True
while a:
    print("Enter 1 to accept an account number and display the account holder's name and balance")
    print("Enter 2 to deposit an amount into an account after checking that the amount is positive")
    print("Enter 3 to withdraw an amount only if sufficient balance is available")
    print("Enter 4 to display all account holders and their current balances")
    print("Enter 5 to calculate the total amount maintained across all bank accounts.")
    print("Enter 6 to exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        n = int(input("Enter account number: "))
        search_accounts(n)
    elif choice == 2:
        n = int(input("Enter account number: "))
        deposit_amount(n)
    elif choice == 3:
        n = int(input("Enter account number: "))
        withdraw_amount(n)
    elif choice == 4:
        display_accounts()
    elif choice == 5:
        total_bank_balance()
    elif choice == 6:
        a = False
    else:
        print("Invalid Choice")


