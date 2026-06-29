#Custom Exception - Salary Validation
# Create a custom exception named SalaryError.
# Raise it if the salary entered by the user is less than 20000.

class SalaryError(Exception):
    pass

try:
    salary = int(input("Enter salary: "))

    if salary < 20000:
        raise SalaryError("Salary must be at least 20000.")

    print("Salary Accepted.")

except SalaryError as e:
    print(e)