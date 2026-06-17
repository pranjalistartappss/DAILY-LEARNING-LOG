sentence = "python is easy and python is powerful"

words = sentence.split()
#The split() method breaks a string into a list of words using spaces as the default separator.

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)