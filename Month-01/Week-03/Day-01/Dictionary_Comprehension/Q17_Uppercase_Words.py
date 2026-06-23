#Q17. Create a dictionary where keys are words and values are uppercase versions of those words.
words = ["python", "java", "sql"]

upper = {word: word.upper() for word in words}

print(upper)