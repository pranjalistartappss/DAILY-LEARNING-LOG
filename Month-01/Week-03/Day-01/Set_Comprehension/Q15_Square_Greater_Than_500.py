#Q15. Create a set of numbers from 1 to 50 whose square is greater than 500.

nums = {num for num in range(1, 51) if num**2 > 500}

print(nums)