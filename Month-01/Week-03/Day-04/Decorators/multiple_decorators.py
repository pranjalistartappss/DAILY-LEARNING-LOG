def d1(func):
    def wrapper():
        print("D1 before")
        func()
        print("D1 after")
    return wrapper

def d2(func):
    def wrapper():
        print("D2 before")
        func()
        print("D2 after")
    return wrapper

@d1
@d2
def hello():
    print("Hello")

hello()