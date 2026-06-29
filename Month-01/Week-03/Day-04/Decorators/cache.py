def cache(func):
    memory = {}

    def wrapper(x):
        if x not in memory:
            memory[x] = func(x)
        return memory[x]
    return wrapper

@cache
def square(n):
    print("calculating ...")
    return n*n

print(square(5))
print(square(6))


