def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Pranjali", 21)

# using *args
def student(*details):

    print("Name:", details[0])
    print("Age:", details[1])

student("Pranjali", 21)