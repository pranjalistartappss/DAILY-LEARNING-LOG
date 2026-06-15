balance = 10000

while True:
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = int(input("Enter Amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    elif choice == 3:
        amount = int(input("Enter Amount: "))
        balance += amount
        print("Deposit Successful")

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")