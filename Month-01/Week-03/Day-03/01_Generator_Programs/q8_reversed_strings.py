#Q8. Create a generator that yields reversed strings from a list.

def reverse_strings(words):

    for word in words:
        yield word[::1]

names = ["Python", "Java", "C++"]

for value in reverse_strings(names):
    print(value)

    
