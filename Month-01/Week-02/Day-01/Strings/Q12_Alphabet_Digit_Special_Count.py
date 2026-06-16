text = input("Enter a string: ")

alphabets = 0
digits = 0
special = 0

for ch in text:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Alphabets =", alphabets)
print("Digits =", digits)
print("Special Characters =", special)