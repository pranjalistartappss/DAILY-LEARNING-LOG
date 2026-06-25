#Q9. Write a generator that yields words from a sentence one by one.

def words(sentence):

    for word in sentence.split():
        yield word


for word in words("I Love Python Programming"):
    print(word)