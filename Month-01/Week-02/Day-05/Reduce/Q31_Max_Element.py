from functools import reduce

nums = [10, 45, 23, 67, 12]

largest = reduce(
    lambda a, b: a if a > b else b,nums)

print(largest)