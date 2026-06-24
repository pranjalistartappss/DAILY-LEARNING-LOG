#Q5. Create an iterator class that iterates through a list of employee names one by one.

employees = ["John", "Mike", "Sara", "Alex"]

class EmployeeIterator:
    def __init___(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        return self  
    
    def __next__(self):

        if self.index >= len(self.employees):
            raise StopIteration
        
        value = self.employee[self.index]
        self.index += 1

        return value
    
obj =  EmployeeIterator(employees)

for emp in obj:
    print(emp)

    
        