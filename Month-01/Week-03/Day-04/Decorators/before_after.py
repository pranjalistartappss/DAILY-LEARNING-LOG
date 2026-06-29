#1. Write a decorator that prints "Before Function" before execution and "After Function" after execution of a function.
def decorators(func):
    def wrapper():
        print("After execution")
        func()
        print("Before execution")
    return wrapper

@decorators
def hello():
    print("Hello")

hello()




