#Q2. Create a class NumberIterator that iterates over numbers from 1 to 10.

class NumberIterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.num > 10:
            raise StopIteration
        
        value = self.num 
        self.num += 1

        return value
    
obj = NumberIterator()

for i in obj:
    print(i)
