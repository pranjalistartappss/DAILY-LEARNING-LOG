#Q18. Create a dictionary where keys are words and values are their first letters.
words = ["python", "java", "sql"]

first = {word: word[0] for word in words}

print(first)