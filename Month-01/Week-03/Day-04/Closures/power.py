#Write a closure that generates functions for calculating powers, such as square, cube, and fourth power.

def power(n):

    def calculate(x):
        return  x**n
    return calculate

square = power(2)
cube = power(3)

print(square(5))
print(cube(5))

