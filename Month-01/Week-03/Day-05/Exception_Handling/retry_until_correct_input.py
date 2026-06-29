#7. Retry Until Correct Input
# Keep asking the user to enter an integer until a valid integer is provided.

while True:
    try:
        num = int(input("Enter number:"))
        print("You entered:", num)
        break 

    except ValueError:
        print("Invalid input. Try again")

