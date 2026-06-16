# Q4. Create a tuple of 10 numbers and count how many numbers are greater than 50.

numbers = (10, 70, 20, 80, 30, 90, 40, 60, 25, 55)

count = 0

for num in numbers:
    if num > 50:
        count += 1

print("Count =", count)