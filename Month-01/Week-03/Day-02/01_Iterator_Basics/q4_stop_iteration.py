#Q4. Explain the purpose of the StopIteration exception. When and by whom is it raised?

# StopIteration tells Python that iteration has finished.

# It is raised by:

# Custom iterators
# Generators
# Built-in iterators

class Demo:

    def __init__(self):
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.count > 3:
            raise StopIteration

        value = self.count
        self.count += 1

        return value


obj = Demo()

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))