def logger(func):
    def wrapper(*args, **kwargs):
        print("Function:",  func.__name__)
        print("Args:", args)
        print("Kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a,b):
    return a+b

print(add(2,3))
