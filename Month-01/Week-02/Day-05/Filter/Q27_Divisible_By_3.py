nums = range(1, 31)

divisible_nums = list(filter(lambda num: num % 3 == 0, nums))

print(divisible_nums)