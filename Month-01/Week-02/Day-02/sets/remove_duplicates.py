#1️ Remove Duplicates from a List Using Set

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

unique_numbers = list(set(numbers))
#print(type(set(numbers)))
# we use list because set(numbers) removes duplicate values, but it returns a set, not a list.
print(unique_numbers)
