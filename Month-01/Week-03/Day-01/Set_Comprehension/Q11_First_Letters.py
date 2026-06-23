#Q11. Create a set of first letters from a list of names.

names = ["Mona", "Riya", "Anjali", "Siya"]

first_letters = {name[0] for name in names}

print(first_letters)