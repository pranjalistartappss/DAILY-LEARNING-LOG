#Q15. Create a generator that simulates a countdown timer from N to 0.
def countdown(n):

    while n >= 0:
        yield n
        n -= 1


for value in countdown(5):
    print(value)