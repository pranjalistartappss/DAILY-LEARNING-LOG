#Q14. Build a generator that yields unique elements from a list.
def unique_elements(numbers):

    seen = set()

    for num in numbers:

        if num not in seen:
            seen.add(num)
            yield num


nums = [1, 2, 2, 3, 4, 4, 5]

for value in unique_elements(nums):
    print(value)