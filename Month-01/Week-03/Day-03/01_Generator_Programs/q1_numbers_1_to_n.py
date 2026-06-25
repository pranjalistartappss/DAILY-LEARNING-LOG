#Q1. Write a generator that yields numbers from 1 to N.

def number(n):

    for i in range(1, n+1):
        yield i 


for num in number(5):
    print(num)

    
