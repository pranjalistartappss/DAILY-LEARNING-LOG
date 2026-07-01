class Employee:

    def __init__(self, employee_id, salary):
        self.__employee_id = employee_id
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Invalid Salary")

    def show_details(self):
        print("Employee ID :", self.__employee_id)
        print("Salary :", self.__salary)


emp = Employee(101, 30000)

emp.show_details()

emp.set_salary(35000)

print()

emp.show_details()