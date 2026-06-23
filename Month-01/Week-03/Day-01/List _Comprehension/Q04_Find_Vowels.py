#Q04. Create a list of vowels present in a string entered by the user.

text = input("Enter a string: ")
vowels = [ch for ch in text if ch.lower() in "aeiou"]

print(vowels)
