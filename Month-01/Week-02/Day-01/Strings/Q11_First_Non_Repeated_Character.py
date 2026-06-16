#Method 1
text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First Non-Repeated Character =", ch)
        break

#Method 2 (HASHMAP)

value = input("Enter a string: ")

freq = {}

for ch in value:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Find first non-repeated character
for ch in value:
    if freq[ch] == 1:
        print("First Non-Repeated Character =", ch)
        break
else:
    print("No non-repeated character found")