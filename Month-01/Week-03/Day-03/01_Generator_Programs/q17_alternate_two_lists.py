#Q17. Build a generator that alternates between two lists.
def alternate(list1, list2):

    for a, b in zip(list1, list2):
        yield a
        yield b


l1 = [1, 2, 3]
l2 = ["A", "B", "C"]

for value in alternate(l1, l2):
    print(value)