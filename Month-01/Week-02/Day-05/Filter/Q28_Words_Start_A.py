words = ["apple", "banana", "ant", "cat", "air"]

a_words = list(filter(lambda word: word.startswith("a"), words))

print(a_words)