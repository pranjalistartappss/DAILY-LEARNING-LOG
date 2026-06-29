import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time:", end - start)
    return wrapper

@timer
def work():
    time.sleep(1)

work()