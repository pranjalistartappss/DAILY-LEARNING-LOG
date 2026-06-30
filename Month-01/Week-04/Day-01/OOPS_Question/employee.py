class Employee:

    def __init__(self, employee_id, name, department, designation, salary, email, joining_date, experience):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary
        self.email = email
        self.joining_date = joining_date
        self.experience = experience

    def login(self):
        print(self.name, "logged in successfully.")

    def apply_leave(self):
        print(self.name, "applied for leave.")

    def calculate_salary(self):
        print("Salary:", self.salary)

    def show_details(self):
        print("\n----- Employee Details -----")
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Designation:", self.designation)
        print("Salary:", self.salary)
        print("Email:", self.email)
        print("Joining Date:", self.joining_date)
        print("Experience:", self.experience, "years")

employee1 = Employee(101,"Pranjali","IT","Python Developer",50000,"pranjali@gmail.com", "10-01-2025",2)

employee1.show_details()
employee1.login()
employee1.apply_leave()
employee1.calculate_salary()