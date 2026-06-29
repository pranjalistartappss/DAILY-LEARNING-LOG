def count_calls(func):
    def wrapper():
        wrapper.count += 1
        print("called:",wrapper.count)
        func()
    wrapper.count = 0 
    return wrapper

@count_calls
def hello():
    print("Hi")

hello()
hello()