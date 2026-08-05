def main():
    print("Welcome to the ATM Machine")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    

main()

balance=1000
choice=int(input("Enter your choice: "))

def check_balance(balance):
    if choice == 1:
        print(f"Your balance is Rs:{balance}")
    return balance
check_balance(balance)

def deposit(balance):
    if choice == 2:
        amount=int(input("Enter amount to deposit: "))
        balance=balance+amount
        print(f"You New balance is Rs:{balance}")
    return balance
balance=deposit(balance)

def withdraw(balance):
    if choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance :
            print("Insufficient balance")
        else:
            balance = balance - amount
            print(f"You New balance is Rs:{balance}")
    return balance
balance=withdraw(balance)

def exit():
    if choice == 4:
        print("Thank you for using our ATM. Goodbye!")
exit()

