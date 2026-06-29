#Implement a closure that maintains a running total and updates it whenever a new number is passed.

def total():
    s = 0 

    def add(num):
        nonlocal s
        s += num
        return s
    
    return add

t = total()
print(t(5))
print(t(6))