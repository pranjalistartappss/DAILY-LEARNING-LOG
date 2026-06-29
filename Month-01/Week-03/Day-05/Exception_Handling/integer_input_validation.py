#2. Integer Input Validation
# Take an integer input from the user. If the user enters anything other than an integer, display "Invalid Input".

try:
    num = int(input("Enter an integer:"))
    print(num)

except ValueError:
    print("Invalid Input")

