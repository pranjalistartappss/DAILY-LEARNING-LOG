#1. Division Calculator
# Write a program that takes two numbers from the user and performs division. Handle ZeroDivisionError.
try:
    num1 = int(input("Enter a First_number:"))
    num2 = int(input("Enter a Second_number"))
    result = num1/num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by Zero")



