from functools import reduce

nums = range(1, 7)

fact = reduce(lambda a, b: a * b, nums)

print(fact)