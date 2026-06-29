# Multiple Exception Handling
# Accept a number from the user and divide 100 by it. Handle both ValueError and ZeroDivisionError.

try:
    num = int(input("Enter an integer:"))
    result  = 100/num
    print("Result:", result)

except ValueError:
    print("Enter a valid  integer")

except ZeroDivisionError:
    print("Cannot divide by Zero")