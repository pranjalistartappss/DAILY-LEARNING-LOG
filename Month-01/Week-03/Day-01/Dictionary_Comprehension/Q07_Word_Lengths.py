#Q07. Create a dictionary where keys are words and values are word lengths.

words = ["python", "java", "sql"]

lengths = {word: len(word) for word in words}

print(lengths)