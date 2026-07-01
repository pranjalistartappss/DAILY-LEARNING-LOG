# encapsulation: it is  the process of wrapping data(attributes) and methods(function)
# into single unit(class).
# it also helps protect  data by controlling how it is accessed or modified 
# benefit = data security, hinding better control, valid  possible

#access modifiers: public, protected, private
#protected(_name): inside class and subclass
#private(_name): inside same class


class student:
    def __init__(self):
        self.name = "abc"

s = student()
print(s.name)

s = student()
print(s.name)
s.name = "xyz"
print(s.name)


class Account:
    def __init__(self):
        self.balance = 1000

acc = Account
#private attribute 

