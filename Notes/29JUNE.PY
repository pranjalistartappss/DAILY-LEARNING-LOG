#OOPS : object - oriented programming ): it is programming style 
# where we represent real-word things as object 

# for example: student(object) each object has data(Attributes), functions(methods)
#class: a class is a blueprint or template used to create the object
# object : object is a real instance of class
# self = self refers to current object 
# we create multiple object of one class , and object are independent , they not depend on each other 
# INSTANCE Attribute: it isbelong to each object, separate copy
# class atribute class attributes are shared among all  object , shared copy


# class student:
#     def  __init__(self, name, age,roll_number,departement):
#         self.name = name
#         self.age = age
#         self.departement = departement
#         self.roll_number = roll_number
#         print('constructor called')

#     def study():
#         pass

#     def attend_class():
#         pass

# obj1 = student("pranja;i",21,"IT",91,)

#obj1.study()
#print(id(obj1) is id(obj2))

# Backaccount
# attributes :name,account, number, balance, ifsc code, branch
#operation :deposit, withdrawal,total,balance

class BankAccount:

    def __init__(self, name, acc_no, balance, ifsc, branch):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        self.ifsc = ifsc
        self.branch = branch

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def total_balance(self):
        print("Balance:", self.balance)


b1 = BankAccount("Pranjali", 12345, 10000, "SBIN001", "Indore")

b1.deposit(2000)
b1.withdrawal(1000)
b1.total_balance()

b2 = BankAccount("Anjali",23456, 4000, "HDFC0001", "REWA")
b2.deposit(3000)
b2.withdrawal(100)
b2.total_balance()