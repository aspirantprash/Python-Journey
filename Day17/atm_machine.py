#ATM Machine Simulation
def check_balance(balance):
    print(f"\nYour Balance: ₹{balance}")
    return balance


def deposit(balance):
    amount = int(input("Enter amount to deposit: "))
    balance = balance + amount
    print(f"Deposit Successful!")
    print(f"\nYour Balance: ₹{balance}")

    return balance


def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance = balance - amount
        print("Withdrawal Successful!")
    print(f"\nYour Balance: ₹{balance}")

    return balance


def main():
    balance = 10000

    while True:
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            balance = check_balance(balance)

        elif choice == 2:
            balance = deposit(balance)

        elif choice == 3:
            balance = withdraw(balance)

        elif choice == 4:
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid Choice!")


main()