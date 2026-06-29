#Q11. Write a generator that yields factorial of numbers from 1 to N.
def factorial_generator(n):

    fact = 1

    for i in range(1, n + 1):
        fact *= i
        yield fact


for value in factorial_generator(5):
    print(value)
    