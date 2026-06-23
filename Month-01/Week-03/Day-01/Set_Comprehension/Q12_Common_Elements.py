#Q12. Create a set of common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = {num for num in list1 if num in list2}

print(common)