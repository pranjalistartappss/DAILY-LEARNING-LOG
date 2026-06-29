#14. Using try-except-else-finally
# Write a program that:
# Takes an integer input
# Divides 100 by the number
# Uses except for errors
# Uses else to print the result
# Uses finally to print "Execution Finished

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Execution Finished")