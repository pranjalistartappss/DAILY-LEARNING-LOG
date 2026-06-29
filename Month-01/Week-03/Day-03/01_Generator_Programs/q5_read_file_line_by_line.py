#Q5. Write a generator that reads lines from a file one by one.
def read_file(filename):

    with open(filename, "r") as file:

        for line in file:
            yield line.strip()


for line in read_file("sample.txt"):
    print(line)