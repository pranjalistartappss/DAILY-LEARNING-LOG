class Decorators:
    def __init__(self,func):
        self.func = func

    def __call__(self):
        print("Function Started")
        self.func()
        print("Function Ended")

@Decorators
def hello():
    print("Hello")

hello()


