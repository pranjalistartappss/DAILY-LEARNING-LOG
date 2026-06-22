from functools import reduce

words = ["Python", "is", "awesome"]

sentence = reduce(
    lambda a, b: a + " " + b,
    words
)

print(sentence)