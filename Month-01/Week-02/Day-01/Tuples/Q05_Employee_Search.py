# Q5. Create a tuple of employee names and check whether a given employee name exists in the tuple.

# Example:

# Input: demo

# Output:
# Employee Found

employees = ("Ram", "Mohan", "Ajay", "Demo", "Harsh")

search = input("Enter employee name: ")

found = False

for employee in employees:
    if employee == search:
        found = True
        break

if found:
    print("Employee Found")
else:
    print("Employee Not Found")