# Create a list of 10 numbers and count how many numbers are even and odd.

num = [10, 15, 22, 33, 44, 55, 66, 88, 99, 23]

even_count = 0 
odd_count = 0 

for i in num:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count)
print(odd_count)


