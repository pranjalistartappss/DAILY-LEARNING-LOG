#4. Dictionary Key Lookup
# Given a dictionary of employee names and salaries, ask the user for an employee name and print the salary. Handle KeyError.

employees = {"Rahul": 50000, "Amit": 60000, "Neha": 70000}

try:
    users = input("Enter a employees name:")
    print("Salary:",employees[users])

except KeyError:
    print("User not found.")

