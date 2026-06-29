#Implement a closure that uses the nonlocal keyword to modify an outer variable.

def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5
        print(x)

    return inner

f = outer()
f()
f()