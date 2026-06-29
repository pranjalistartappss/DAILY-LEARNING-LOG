#5. List Index Access
# Create a list of five numbers. Ask the user for an index and print the value at that index. Handle IndexError.
numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])

except IndexError:
    print("Index out of range.")