#Create a closure that acts as a counter and returns the next count value each time it is called.

def counter():
    count = 0 

    def  increment():
        nonlocal count
        count += 1
        return count
    
    return increment

c = counter()
print(c())
print(c())