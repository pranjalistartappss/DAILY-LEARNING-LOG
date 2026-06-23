#Q17. Create a set of all unique words from a sentence entered by the user.

sentence = input("Enter sentence: ")

words = {word for word in sentence.split()}

print(words)