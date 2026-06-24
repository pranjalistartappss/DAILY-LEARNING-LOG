#Q10. Implement an infinite iterator that repeatedly cycles through the lowercase English alphabets (a-z).

class AlphabetCycle:

    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        letter = chr(97 + self.index)

        self.index += 1

        if self.index == 26:
            self.index = 0

        return letter


obj = AlphabetCycle()

for _ in range(30):
    print(next(obj))