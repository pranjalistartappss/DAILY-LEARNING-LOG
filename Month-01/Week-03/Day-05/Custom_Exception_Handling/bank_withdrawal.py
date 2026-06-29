#13. Bank Withdrawal System
# Given a balance of 10000, ask the user for a withdrawal amount.
# Raise a custom exception if the withdrawal amount exceeds the balance.

class InsufficientBalanceError(Exception):
    pass


balance = 10000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise InsufficientBalanceError("Insufficient Balance.")

    balance -= amount
    print("Remaining Balance:", balance)

except InsufficientBalanceError as e:
    print(e)