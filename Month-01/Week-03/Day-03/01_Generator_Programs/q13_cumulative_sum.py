#Q13. Write a generator that yields cumulative sum of a list.
def cumulative_sum(numbers):

    total = 0

    for num in numbers:
        total += num
        yield total


nums = [1, 2, 3, 4]

for value in cumulative_sum(nums):
    print(value)