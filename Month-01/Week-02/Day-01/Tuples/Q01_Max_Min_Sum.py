# Q1. Create a tuple of 10 numbers and find:

# Maximum number
# Minimum number
# Sum of all numbers

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

maximum = numbers[0]
minimum = numbers[0]
total = 0

for num in numbers:

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

    total += num

print(maximum)
print(minimum)
print(total)