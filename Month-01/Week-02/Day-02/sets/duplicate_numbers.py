#Find Duplicate Numbers Using Sets

numbers = [1, 2, 3, 2, 4, 5, 5, 6]

duplicates = set()

for num in numbers:
    if numbers.count(num) > 1:
        duplicates.add(num)

print(duplicates)