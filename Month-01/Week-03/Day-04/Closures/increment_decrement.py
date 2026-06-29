#Create a closure that returns two functions: one to increment a value and another to decrement it while sharing the same state. give solution of easy and concise

def value():
    x = 0

    def inc():
        nonlocal x
        x += 1
        return x

    def dec():
        nonlocal x
        x -= 1
        return x

    return inc, dec

inc, dec = value()

print(inc())
print(inc())
print(dec())