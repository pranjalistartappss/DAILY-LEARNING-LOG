#9. Type Checking
# Write a function that adds two values passed by the user. Handle TypeError if incompatible data types are provided.

def add(a,b):
    try:
        print(a+b)

    except TypeError:
        print("Incompatible data type")

add(10,"Hello")