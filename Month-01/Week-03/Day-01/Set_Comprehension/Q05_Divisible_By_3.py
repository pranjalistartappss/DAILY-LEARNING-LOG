#Q05. Create a set of numbers divisible by 3 from 1 to 100.

nums = {num for num in range(1, 101) if num % 3 == 0}

print(nums)

