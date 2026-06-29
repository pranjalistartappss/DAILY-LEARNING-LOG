#Q7. Write a generator that produces infinite natural numbers starting from 1.
def infinite_numbers():

    num = 1

    while True:
        yield num
        num += 1


gen = infinite_numbers()

for _ in range(10):
    print(next(gen))