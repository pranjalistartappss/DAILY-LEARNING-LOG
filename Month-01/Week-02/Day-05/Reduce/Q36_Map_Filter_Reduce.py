from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,10]

even_nums = list(filter(lambda num: num % 2 == 0, nums))

square_nums = list(map(lambda num: num * num, even_nums))

total = reduce(lambda a, b: a + b, square_nums)

print(total)