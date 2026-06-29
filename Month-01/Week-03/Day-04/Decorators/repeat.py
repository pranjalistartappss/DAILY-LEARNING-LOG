#2. Write a decorator that accepts an argument n and executes the decorated function n times.
def repeat(n):
    def decorator(func):
        def  wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()