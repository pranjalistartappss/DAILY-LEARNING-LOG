#Create a closure representing a bank account with operations to deposit, withdraw, and check balance.

def account():
    balance = 0

    def operation(choice,amount):
        nonlocal balance

        if choice == "deposit":
            balance += amount
        elif choice == "withdraw":
            balance -= amount
        elif choice == "balance":
            return balance

    return operation


acc = account()
acc("deposit", 1000)
acc("withdraw", 200)
print(acc("balance"))