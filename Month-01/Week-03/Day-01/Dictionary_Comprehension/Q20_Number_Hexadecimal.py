# Q20. Create a dictionary where keys are numbers from 1 to 10 and values are their hexadecimal representations.

hexa = {num: hex(num) for num in range(1, 11)}

print(hexa)