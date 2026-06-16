# Take 5 names in a list and print them in alphabetical order.
# Example:
# Input:
# ["Ram", "demo", "Mohan"]
# Output:
# ["demo", "Mohan", "Ram"]

names = ["Ram", "demo", "Mohan", "Ajay", "Harsh"]

names.sort()

print(names)

#Python sorts strings using ASCII/Unicode values.

# Capital letters A-Z have ASCII values 65-90
# Small letters a-z have ASCII values 97-122

#Since demo starts with lowercase d and the other names start with uppercase letters, demo is placed after them and appears last in the sorted list.