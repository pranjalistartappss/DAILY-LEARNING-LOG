#Q07. Create a set containing lengths of words.

words = ["apple", "banana", "kiwi", "grapes"]

lengths = {len(word) for word in words}

print(lengths)
