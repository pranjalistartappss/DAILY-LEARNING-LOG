def employee(name, salary):
    print("Name:", name)
    print("Salary:", salary)

employee(salary=50000, name="Rahul")

#USING **KWARGS
def employee(**details):

    print("Name:", details["name"])
    print("Salary:", details["salary"])

employee(name="Rahul", salary=50000)