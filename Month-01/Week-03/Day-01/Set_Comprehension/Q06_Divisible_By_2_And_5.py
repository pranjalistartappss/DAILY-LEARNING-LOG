#Q06. Create a set of numbers divisible by both 2 and 5 from 1 to 100.

nums = {num for num in range(1, 101) if num % 2 == 0 and num % 5 == 0}

print(nums)