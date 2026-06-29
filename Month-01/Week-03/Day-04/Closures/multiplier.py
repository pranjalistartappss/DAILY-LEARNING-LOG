#Create a closure that returns a multiplier function capable of multiplying any input by a fixed number.

def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)

print(double(10))