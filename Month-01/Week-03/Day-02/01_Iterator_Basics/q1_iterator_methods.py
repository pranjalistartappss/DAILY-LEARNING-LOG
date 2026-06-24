#Q1. What methods must a class implement to become an iterator in Python?

# A class must implement:
# __iter__()
# __next__()

# __iter__() returns the iterator object.
# __next__() returns the next value.

# When no values remain, __next__() raises StopIteration.
class Demo:

    def __iter__(self):
        return self

    def __next__(self):
        return 10


obj = Demo()

print(next(obj))