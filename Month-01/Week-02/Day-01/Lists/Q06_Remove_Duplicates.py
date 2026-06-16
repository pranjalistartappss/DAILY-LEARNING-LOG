#Create a list with duplicate values and remove duplicates without using set().
# Example:
# Input: [1,2,2,3,4,4,5]

# Output: [1,2,3,4,5]

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print(unique)