largest = float('-inf')

for i in range(5):
    num = int(input("Enter number: "))

    if num > largest:
        largest = num

print("Largest =", largest)