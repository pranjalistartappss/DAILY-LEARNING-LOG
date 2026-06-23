#Q14. Create a set of numbers from 1 to 100 divisible by 2 but not by 3.

nums = {num for num in range(1, 101) if num % 2 == 0 and num % 3 != 0}

print(nums)