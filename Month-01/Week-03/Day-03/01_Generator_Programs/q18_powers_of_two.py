#Q18. Write a generator that yields powers of 2 up to N terms.
def powers_of_two(n):

    for i in range(n):
        yield 2 ** i


for value in powers_of_two(6):
    print(value)