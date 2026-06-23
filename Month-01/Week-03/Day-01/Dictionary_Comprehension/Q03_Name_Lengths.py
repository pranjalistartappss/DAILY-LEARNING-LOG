#Q03. Create a dictionary from the following list where values are lengths of names.

names = ["Monika", "Riya", "Anjali"]

lengths = {name: len(name) for name in names}

print(lengths)