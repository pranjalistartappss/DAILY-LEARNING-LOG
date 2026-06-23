#Q13. Create a set of unique elements from two lists combined.

list1 = [1, 2, 3]
list2 = [3, 4, 5]

unique = {num for num in list1 + list2}

print(unique)
