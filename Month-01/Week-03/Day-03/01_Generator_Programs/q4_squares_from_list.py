#Q4. Create a generator that yields squares of numbers from a list.

def square_generator(number):

    for num in number:
        yield num ** 2

nums = [1,2,3,4,5]

for value in square_generator(nums):
    print(value)