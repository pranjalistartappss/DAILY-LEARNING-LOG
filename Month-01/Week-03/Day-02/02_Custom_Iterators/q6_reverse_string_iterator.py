#Q6. Implement a custom iterator that traverses a string in reverse order.

class ReverseString:

    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.index < 0:
            raise StopIteration

        value = self.text[self.index]
        self.index -= 1

        return value


obj = ReverseString("Python")

for char in obj:
    print(char)
