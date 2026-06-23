#Q09. Create a set of unique vowels from a string entered by the user.

text = input("Enter string: ")

vowels = {ch for ch in text if ch.lower() in "aeiou"}

print(vowels)