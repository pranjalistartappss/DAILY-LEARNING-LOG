#1. Write a closure that remembers a name provided to the outer function and prints a greeting when called.

def greet(name):
    def message():
        print("Hello:", name)
    return message

g = greet("Pranjali")
g()

