def validate(func):
    def wrapper(*args):
        for i in args:
            if not isinstance(i, int) or i <= 0:
                raise ValueError("Only positive integers allowed")
        return func(*args)
    return wrapper

@validate
def add(a, b):
    return a + b

print(add(3, 4))