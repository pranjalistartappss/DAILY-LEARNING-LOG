#Q11. Find the frequency of each element in a list.

nums = [1, 2, 3, 2, 1, 4, 2]

freq = {num: nums.count(num) for num in nums}

print(freq)